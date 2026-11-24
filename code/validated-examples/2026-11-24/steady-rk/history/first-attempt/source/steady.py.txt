"""Four base-state residual stages on the actual periodic field."""
import numpy as np


def operator(u, shift=1):
    n = len(u)
    return shift*u+(n/16)*(np.roll(u,-1)-np.roll(u,1))-(n*n/64)*(np.roll(u,-1)-2*u+np.roll(u,1))


def patterns(n=16):
    cosine = np.tile(np.array([1.,0.,-1.,0.]),n//4)
    sine = np.tile(np.array([0.,1.,0.,-1.]),n//4)
    nyquist = np.tile(np.array([1.,-1.]),n//2)
    return cosine, sine, nyquist


def evolve(initial, forcing, dt, steps, shift, progress=None):
    u = np.array(initial, copy=True)
    history = np.empty((steps+1,len(u)))
    stages = np.empty((steps,4,len(u)))
    residuals = np.empty_like(stages)
    history[0] = u
    for k in range(steps):
        base = u.copy()
        stage = base.copy()
        for j, alpha in enumerate((.25,1/3,.5,1.)):
            if progress is not None:
                progress(step=k,stage_index=j,base=base,stage=stage,
                         completed_history=history[:k+1],phase="before_operator")
            residual = operator(stage,shift)-forcing
            if progress is not None:
                progress(step=k,stage_index=j,base=base,stage=stage,residual=residual,
                         completed_history=history[:k+1])
            residuals[k,j] = residual
            stage = base-alpha*dt*residual
            if progress is not None:
                progress(step=k,stage_index=j,base=base,stage=stage,residual=residual,
                         completed_history=history[:k+1],phase="updated_candidate")
            stages[k,j] = stage
            if not np.isfinite(stage).all():
                raise FloatingPointError('Nonfinite residual stage')
        u = stage.copy()
        history[k+1] = u
    return history,stages,residuals
