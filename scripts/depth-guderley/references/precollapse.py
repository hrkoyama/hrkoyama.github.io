"""Pre-collapse-only dense adapter to pinned LANL ExactPack Guderley routines.

The nonlinear exponent and the similarity ODE are actual ExactPack code.  This
adapter changes evaluation/caching and coordinates, not the ODE.  It is not an
independently implemented semi-analytic solution.  The finite-volume Euler
evolution is a separate numerical method.
"""
from functools import lru_cache
import numpy as np
from scipy.integrate import solve_ivp
from .exactpack_guderley import eexp as exponent_module
from .exactpack_guderley import ramsey


GAMMA = 1.4
RHO0 = 1.0
SHOCK_SCALE = 0.6
TIME0 = -1.0
TIME1 = -0.85
OUTER_RADIUS = 0.75
MAX_SIMILARITY_RADIUS = 1.42
EXACTPACK_FACTOR_C = 0.750024322
TABULATED_LAMBDA = 1.3943607838
TABULATED_ALPHA = 0.717174501


@lru_cache(maxsize=1)
def eigenvalue():
    """Compute (do not hardcode) the spherical gamma=1.4 exponent."""
    value = float(exponent_module.eexp(3, GAMMA))
    if not np.isfinite(value) or value <= 1:
        raise RuntimeError("invalid Guderley similarity eigenvalue")
    return value


class GuderleyReference:
    """Cold upstream, spherical gamma=1.4 branch on a fixed pre-collapse box.

    Lazarus time t<0 is used and R_s(t)=0.6*(-t)**alpha.  Radius divided
    by0.6 maps to upstream ExactPack coordinates.  Public ExactPack time for
    that coordinate is t_C=0.750024322*(t+1); physical velocities and sound
    speeds are0.6 times the public routine's Lazarus-time values, pressures
    are0.6**2 times those values.  There is no reflected-shock B solve.
    """

    gamma = GAMMA
    rho0 = RHO0
    shock_scale = SHOCK_SCALE

    def __init__(self):
        self.lambda_ = eigenvalue()
        self.alpha = 1.0 / self.lambda_
        self.x_end = -MAX_SIMILARITY_RADIUS ** (-self.lambda_)
        self.jump = np.array([-2.0 / (GAMMA + 1.0),
                              np.sqrt(2 * GAMMA * (GAMMA - 1)) / (GAMMA + 1),
                              (GAMMA + 1) / (GAMMA - 1)])
        self._set_rhs_parameters()
        # Same RK45 tolerances as ExactPack ramsey.state's pre-collapse solve.
        self.solution = solve_ivp(ramsey.g, (-1.0, self.x_end), self.jump,
                                  method="RK45", rtol=5e-11, atol=6e-12,
                                  dense_output=True)
        if not self.solution.success or self.solution.t[-1] != self.x_end:
            raise RuntimeError("ExactPack pre-collapse ODE failed: " + self.solution.message)
        if not np.all(np.isfinite(self.solution.y)):
            raise RuntimeError("nonfinite Guderley similarity solution")

    def _set_rhs_parameters(self):
        # Pinned upstream routines use module globals, as in the public solver.
        ramsey.gamma = GAMMA
        ramsey.lambda_ = self.lambda_
        ramsey.nu = 2

    def _time(self, t):
        t = float(t)
        if not np.isfinite(t) or t < TIME0 or t > TIME1:
            raise ValueError("reference time must lie in [-1,-0.85]")
        return t

    def shock_radius(self, t):
        t = self._time(t)
        return SHOCK_SCALE * (-t) ** self.alpha

    def shock_speed(self, t):
        t = self._time(t)
        return self.alpha * self.shock_radius(t) / t

    def similarity(self, x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)) or np.any(x < -1-2e-14) or np.any(x > self.x_end+2e-14):
            raise ValueError("similarity point outside qualified shocked branch")
        # Only remove coordinate roundoff at the two already-qualified limits.
        return self.solution.sol(np.clip(x, -1.0, self.x_end))

    def point_state(self, r, t):
        """Return primitive rho,u,p at radii; the shock itself uses downstream."""
        t = self._time(t)
        r = np.asarray(r, dtype=float)
        if np.any(~np.isfinite(r)) or np.any(r < 0) or np.any(r > OUTER_RADIUS + 1e-14):
            raise ValueError("radius outside fixed physical domain")
        rho = np.full_like(r, RHO0)
        u = np.zeros_like(r)
        p = np.zeros_like(r)
        shocked = r >= self.shock_radius(t)
        if np.any(shocked):
            rr = r[shocked]
            x = t * (SHOCK_SCALE / rr) ** self.lambda_
            V, C, R = self.similarity(x)
            factor = -rr / (self.lambda_ * t)
            rho[shocked] = RHO0 * R
            u[shocked] = factor * V
            p[shocked] = rho[shocked] * (factor * C) ** 2 / GAMMA
        return rho, u, p

    def conserved_point(self, r, t):
        rho, u, p = self.point_state(r, t)
        return np.stack([rho, rho * u, p / (GAMMA - 1) + .5 * rho * u*u], axis=-1)

    def cell_means(self, edges, t, order=8):
        """Volume-average conserved states, splitting quadrature at the shock.

        Return qbar and p(qbar), not volume-averaged primitive pressure.  The
        geometric4pi factor cancels between integral and shell volume.
        """
        t = self._time(t)
        edges = np.asarray(edges, dtype=float)
        if edges.ndim != 1 or len(edges) < 2 or np.any(~np.isfinite(edges)) or np.any(np.diff(edges) <= 0):
            raise ValueError("strictly increasing finite shell edges required")
        if edges[0] < 0 or edges[-1] > OUTER_RADIUS + 1e-14:
            raise ValueError("shell edges outside fixed domain")
        if int(order) != order or not 2 <= order <= 32:
            raise ValueError("quadrature order must be an integer2..32")
        rs = self.shock_radius(t)
        a, b = edges[:-1], edges[1:]
        volume = (b**3 - a**3) / 3
        upstream_right = np.maximum(a, np.minimum(b, rs))
        integral = np.zeros((len(a), 3))
        integral[:, 0] = RHO0 * (upstream_right**3 - a**3) / 3
        lo = np.maximum(a, rs)
        active = b > lo
        if np.any(active):
            z, w = np.polynomial.legendre.leggauss(int(order))
            aa, bb = lo[active], b[active]
            rr = (aa[:, None] + bb[:, None]) / 2 + (bb-aa)[:, None] * z / 2
            qq = self.conserved_point(rr, t)
            integral[active] += np.einsum("nq,nqk,q->nk", rr**2, qq, w) * (bb-aa)[:, None] / 2
        q = integral / volume[:, None]
        p = (GAMMA - 1) * (q[:, 2] - .5 * q[:, 1]**2 / q[:, 0])
        return q, p

    def metadata(self):
        return {"geometry":3, "gamma":GAMMA, "rho0":RHO0, "lambda":self.lambda_,
                "alpha":self.alpha, "shock_scale":SHOCK_SCALE,
                "lazarus_times":[TIME0,TIME1], "domain":[0,OUTER_RADIUS],
                "similarity_x_end":self.x_end,
                "max_similarity_radius":MAX_SIMILARITY_RADIUS,
                "ode_success":bool(self.solution.success),
                "ode_steps":len(self.solution.t)-1,
                "ode_nfev":self.solution.nfev,
                "exactpack_public_times":[EXACTPACK_FACTOR_C*(t+1) for t in [TIME0,TIME1]],
                "reflected_branch_executed":False,
                "source_independence":"actual pinned ExactPack eexp and RHS with a pre-collapse dense adapter"}


PrecollapseReference = GuderleyReference
