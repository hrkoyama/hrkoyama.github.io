"""Private state-only expanded iterate; ordinary float64 Arnoldi/Thomas/norm."""
import math
import numpy as np
from krylov import dot, norm
from state_expansion import reconstruct


def gmres(direction, b, preconditioner, restart, maxiter, rtol, remainder, observe=None):
    n = len(b); hi, lo = np.zeros(n), np.zeros(n)
    target = max(1e-14, rtol*norm(b)); history, estimates = [norm(b)], []
    iterations, restart_count = 0, 0
    def note(stage, environment, extra=None):
        if observe is not None:
            arrays = {k:v for k,v in environment.items() if isinstance(v,np.ndarray)}
            if extra is not None: arrays.update(extra)
            observe(stage, arrays, {'iterations':iterations,'target':target,'restart_count':restart_count,
                                   'true_history':history[:],'estimated_history':estimates[:]})
    try:
        while history[-1] > target and iterations < maxiter:
            environment = dict(locals())
            if iterations == 0:
                r = b.copy()
            else:
                r = remainder(hi, lo, lambda stage,extra:note('restart-residual-'+stage,environment,extra))
                restart_count += 1
            del environment
            beta = norm(r); base_hi, base_lo = hi.copy(), lo.copy()
            m = min(restart, maxiter-iterations, n)
            V, Z, H = np.zeros((n,m+1)), np.zeros((n,m)), np.zeros((m+1,m))
            cs, sn, g = np.zeros(m), np.zeros(m), np.zeros(m+1)
            V[:,0] = r/beta; g[0] = beta
            note('cycle-start',locals())
            for k in range(m):
                Z[:,k] = preconditioner(V[:,k]); w = np.array(direction(Z[:,k]),copy=True)
                for _ in range(2):
                    for i in range(k+1):
                        coefficient = dot(V[:,i],w); H[i,k] += coefficient; w -= coefficient*V[:,i]
                H[k+1,k] = norm(w)
                breakdown = H[k+1,k] <= 32*np.finfo(float).eps*max(1,norm(H[:k+1,k]))
                if not breakdown: V[:,k+1] = w/H[k+1,k]
                for i in range(k):
                    a,bv = H[i,k],H[i+1,k]
                    H[i,k] = cs[i]*a+sn[i]*bv; H[i+1,k] = -sn[i]*a+cs[i]*bv
                length = math.hypot(H[k,k],H[k+1,k])
                if length == 0: raise ArithmeticError('Expanded GMRES singular small triangular factor')
                cs[k], sn[k] = H[k,k]/length, H[k+1,k]/length
                H[k,k], H[k+1,k] = length, 0.
                g[k+1] = -sn[k]*g[k]; g[k] *= cs[k]
                y = np.zeros(k+1)
                for i in range(k,-1,-1): y[i] = (g[i]-dot(H[i,i+1:k+1],y[i+1:]))/H[i,i]
                environment = dict(locals())
                hi,lo = reconstruct(base_hi,base_lo,Z[:,:k+1],y,
                    lambda stage,extra:note('reconstruct-'+stage,environment,extra))
                del environment
                environment = dict(locals())
                true_vector = remainder(hi,lo,lambda stage,extra:note('true-residual-'+stage,environment,extra))
                del environment
                true = norm(true_vector); history.append(true); estimates.append(abs(float(g[k+1]))); iterations += 1
                note('completed-iteration',locals())
                if not np.isfinite(true): raise FloatingPointError('Nonfinite expanded true residual')
                if true <= target:
                    return {'hi':hi,'lo':lo,'passed':True,'iterations':iterations,'residuals':np.array(history),
                            'estimates':np.array(estimates),'restart_count':restart_count,'target':target}
                if breakdown:
                    return {'hi':hi,'lo':lo,'passed':False,'iterations':iterations,'residuals':np.array(history),
                            'estimates':np.array(estimates),'restart_count':restart_count,'target':target}
                if abs(g[k+1]) <= target: break
        return {'hi':hi,'lo':lo,'passed':history[-1]<=target,'iterations':iterations,'residuals':np.array(history),
                'estimates':np.array(estimates),'restart_count':restart_count,'target':target}
    except BaseException:
        note('exception',locals()); raise
