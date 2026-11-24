"""Small dense Newton solves with a declared scaled maximum-norm line search."""
import numpy as np


class NewtonFailure(ArithmeticError):
    def __init__(self,status,x,residual,jacobian,trials,iterations):
        super().__init__(status)
        self.status=status
        self.arrays={'candidate':np.array(x,copy=True),'residual':np.array(residual,copy=True),
                     'jacobian':np.array(jacobian,copy=True),'trials':np.array(trials,dtype=float).reshape((-1,4))}
        self.iterations=iterations


def solve(fun,jac,x0,scale,target,max_iterations=16,halvings=12,armijo=1e-4,progress=None):
    x=np.array(x0,dtype=float,copy=True);scale=np.asarray(scale,dtype=float)
    trials=[];residual_evaluations=0;jacobian_evaluations=0;linear_solves=0
    for iteration in range(max_iterations+1):
        if progress is not None:progress(candidate=x,trials=np.array(trials).reshape((-1,4)))
        r=np.array(fun(x),copy=True);residual_evaluations+=1
        norm=float(np.max(np.abs(r/scale)))
        if progress is not None:progress(candidate=x,residual=r,trials=np.array(trials).reshape((-1,4)))
        j=np.array(jac(x),copy=True);jacobian_evaluations+=1
        if progress is not None:progress(candidate=x,residual=r,jacobian=j,trials=np.array(trials).reshape((-1,4)))
        if not np.isfinite(x).all() or not np.isfinite(r).all() or not np.isfinite(j).all():
            raise NewtonFailure('nonfinite_newton_candidate',x,r,j,trials,iteration)
        if norm<=target:
            return x,{'iterations':iteration,'residual_evaluations':residual_evaluations,'jacobian_evaluations':jacobian_evaluations,'linear_solves':linear_solves,'scaled_residual':norm},np.array(trials).reshape((-1,4))
        if iteration==max_iterations:raise NewtonFailure('newton_iteration_budget',x,r,j,trials,iteration)
        try:
            direction=np.linalg.solve(j,-r);linear_solves+=1
        except BaseException as exc:
            error=NewtonFailure('newton_linear_solve_failed',x,r,j,trials,iteration)
            raise error from exc
        accepted=False
        for power in range(halvings+1):
            alpha=2.**(-power);candidate=x+alpha*direction
            if progress is not None:progress(candidate=candidate,jacobian=j,direction=direction,trials=np.array(trials).reshape((-1,4)))
            rr=np.array(fun(candidate),copy=True);residual_evaluations+=1
            value=float(np.max(np.abs(rr/scale)))
            ok=bool(np.isfinite(rr).all() and value<=(1-armijo*alpha)*norm)
            trials.append((iteration,alpha,value,int(ok)))
            if progress is not None:progress(candidate=candidate,residual=rr,jacobian=j,direction=direction,trials=np.array(trials))
            if ok:x=candidate.copy();accepted=True;break
        if not accepted:raise NewtonFailure('newton_line_search_budget',candidate,rr,j,trials,iteration)
    raise AssertionError('Unreachable Newton exit')
