"""Actual backward-Euler evolution and reverse/checkpoint derivatives."""
import json
import struct
from pathlib import Path
import numpy as np
from operators import TriFactor, BufferLedger, laplace, dot
from io_contract import save_json, save_npz


def model(n, steps, kappa, theta, T):
    x = np.arange(1, n+1, dtype=float)/(n+1)
    u0 = np.sin(np.pi*x)+.2*np.sin(2*np.pi*x)
    b = np.sin(np.pi*x)-.1*np.sin(3*np.pi*x)
    d = .5*np.sin(np.pi*x)
    dt, a = T/steps, (n+1)**2
    factor = TriFactor(np.full(n-1, -dt*kappa*a),
                       np.full(n, 1+2*dt*kappa*a), np.full(n-1, -dt*kappa*a))
    transpose = factor.transpose()
    fixed = {'x': x, 'u0': u0, 'b': b, 'target': d}
    fixed.update(factor.arrays('B')); fixed.update(transpose.arrays('BT'))
    return dt, u0, b, d, factor, transpose, fixed


def objective(u, d, kappa, theta):
    return .5*dot(u-d, u-d)/(len(u)+1)+.005*kappa*kappa+.01*theta*theta


def advance(factor, u, b, dt, theta, out, rhs, scratch):
    np.multiply(b, dt*theta, out=rhs)
    np.add(u, rhs, out=rhs)
    factor.solve(rhs, out=out, scratch=scratch)


def full_window(n, steps, kappa, theta, T, directory):
    """Returned metadata has no ndarray/closure alias of the trajectory."""
    directory = Path(directory); directory.mkdir(parents=True, exist_ok=True)
    dt, u0, b, d, factor, trans, fixed = model(n, steps, kappa, theta, T)
    states = np.empty((steps+1, n)); states[0] = u0
    rhs, scratch, p, z, Au = [np.empty(n) for _ in range(5)]
    ledger = BufferLedger()
    live = {'states': states, 'rhs': rhs, 'Thomas_scratch': scratch,
            'p': p, 'z': z, 'Au': Au}
    ledger.observe(live, fixed)
    try:
        for k in range(steps):
            advance(factor, states[k], b, dt, theta, states[k+1], rhs, scratch)
            save_npz(directory/'current-full.npz', {'state': states[k+1], 'step': k+1})
        np.save(directory/'full-states.npy', states, allow_pickle=False)
        np.subtract(states[-1], d, out=Au)
        J = .5*dot(Au, Au)/(n+1)+.005*kappa*kappa+.01*theta*theta
        np.subtract(states[-1], d, out=p); p /= n+1
        gk, gt = .01*kappa, .02*theta
        for k in range(steps-1, -1, -1):
            trans.solve(p, out=z, scratch=scratch)
            laplace(states[k+1], out=Au)
            gk -= dt*dot(z, Au); gt += dt*dot(z, b)
            p[:] = z
        result = {'objective': J, 'gradient': [gk, gt], 'primal_solves': steps,
                  'transpose_solves': steps, 'replay_solves': 0, 'ledger': ledger.report()}
        save_json(directory/'full-summary.json', result)
        return result
    except BaseException:
        save_npz(directory/'failed-full.npz', live)
        raise


def checkpoint_window(n, steps, kappa, theta, T, block, directory):
    """Only checkpoints+one replay block are resident; stream replay evidence."""
    if steps % block:
        raise ValueError('Fixed checkpoint block must divide steps')
    directory = Path(directory); directory.mkdir(parents=True, exist_ok=True)
    dt, u0, b, d, factor, trans, fixed = model(n, steps, kappa, theta, T)
    checkpoints = np.empty((steps//block+1, n))
    replay = np.empty((block+1, n))
    u, rhs, scratch, p, z, Au = [np.empty(n) for _ in range(6)]
    u[:] = u0; checkpoints[0] = u
    live = {'checkpoints': checkpoints, 'replay_block': replay, 'current': u,
            'rhs': rhs, 'Thomas_scratch': scratch, 'p': p, 'z': z, 'Au': Au}
    ledger = BufferLedger(); ledger.observe(live, fixed)
    completed, replay_count = 0, 0
    try:
        for k in range(steps):
            advance(factor, u, b, dt, theta, u, rhs, scratch)
            completed = k+1
            if completed % block == 0:
                checkpoints[completed//block] = u
            save_npz(directory/'current-checkpoint.npz', {'state': u, 'step': completed})
        np.subtract(u, d, out=p); p /= n+1
        gk, gt = .01*kappa, .02*theta
        with (directory/'replayed-states.npy-stream').open('wb') as evidence:
            for start in range(steps-block, -1, -block):
                replay[0] = checkpoints[start//block]
                for j in range(block):
                    advance(factor, replay[j], b, dt, theta, replay[j+1], rhs, scratch)
                    replay_count += 1
                    evidence.write(struct.pack('<q', start+j+1))
                    np.save(evidence, replay[j+1], allow_pickle=False)
                for j in range(block-1, -1, -1):
                    trans.solve(p, out=z, scratch=scratch)
                    laplace(replay[j+1], out=Au)
                    gk -= dt*dot(z, Au); gt += dt*dot(z, b)
                    p[:] = z
                save_npz(directory/'current-checkpoint.npz',
                         {'state': u, 'adjoint': p, 'replay_block': replay,
                          'completed_primal': completed, 'completed_replay': replay_count})
        result = {'gradient': [gk, gt], 'primal_solves': steps,
                  'transpose_solves': steps, 'replay_solves': replay_count,
                  'ledger': ledger.report(), 'resident_full_trajectory': False,
                  'streamed_replay_file': 'replayed-states.npy-stream'}
        save_json(directory/'checkpoint-summary.json', result)
        return result
    except BaseException:
        save_npz(directory/'failed-checkpoint.npz', live)
        raise


def compare_replay(directory, states):
    seen = set(); equal = True
    with (Path(directory)/'replayed-states.npy-stream').open('rb') as stream:
        while stream.peek(1):
            index = struct.unpack('<q', stream.read(8))[0]
            replay = np.load(stream, allow_pickle=False)
            equal &= index not in seen and states[index].dtype == replay.dtype and states[index].tobytes() == replay.tobytes()
            seen.add(index)
    return bool(equal and seen == set(range(1, len(states))))


def tangent(n, steps, kappa, theta, T, partial=None):
    dt, u, b, d, factor, _, _ = model(n, steps, kappa, theta, T)
    u = u.copy(); sk, st = np.zeros(n), np.zeros(n)
    rhs, scratch, out, Au = [np.empty(n) for _ in range(4)]
    def save(step, state_step, kappa_step, theta_step):
        if partial is not None:
            save_npz(partial, state=u, tangent_kappa=sk, tangent_theta=st,
                     completed_coupled_steps=step, state_step=state_step,
                     tangent_kappa_step=kappa_step, tangent_theta_step=theta_step)
    save(0, 0, 0, 0)
    for k in range(steps):
        advance(factor, u, b, dt, theta, out, rhs, scratch); u[:] = out
        save(k, k+1, k, k)
        laplace(u, out=Au)
        np.multiply(Au, -dt, out=rhs); rhs += sk
        factor.solve(rhs, out=sk, scratch=scratch)
        save(k, k+1, k+1, k)
        np.multiply(b, dt, out=rhs); rhs += st
        factor.solve(rhs, out=st, scratch=scratch)
        save(k+1, k+1, k+1, k+1)
    q = (u-d)/(n+1)
    return {'gradient': np.array([dot(q, sk)+.01*kappa, dot(q, st)+.02*theta]),
            'sk': sk, 'st': st, 'state': u, 'RHS_solves': 2*steps}


def forward_objective(n, steps, kappa, theta, T, partial=None):
    dt, u, b, d, factor, _, _ = model(n, steps, kappa, theta, T)
    u = u.copy(); rhs, scratch = np.empty(n), np.empty(n)
    if partial is not None: save_npz(partial, state=u, completed_steps=0)
    for k in range(steps):
        advance(factor, u, b, dt, theta, u, rhs, scratch)
        if partial is not None: save_npz(partial, state=u, completed_steps=k+1)
    return objective(u, d, kappa, theta), u
