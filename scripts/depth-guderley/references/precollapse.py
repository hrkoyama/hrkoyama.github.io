"""Pre-collapse-only dense adapter to pinned LANL ExactPack Guderley routines.

The exponent was actually computed with ExactPack and is reused from a
hash-qualified receipt by default. The unchanged similarity ODE is freshly
integrated. Full eigenvalue shooting is explicit opt-in work. This adapter is
not an independently implemented semi-analytic solution; the finite-volume
Euler evolution is a separate numerical method.
"""
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path
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
REFERENCE_DIR = Path(__file__).resolve().parent
EIGENVALUE_CACHE_SHA256 = "1a03ece09d775587d95bc4cdaf159d4fc4e3e12416e6caf3bb1d1b58f8eccb30"
EXACTPACK_COMMIT = "9bacc477eb791e959c9621e771fc7a725db755fa"


def _safe_path(base, name):
    relative = Path(name)
    if relative.is_absolute() or ".." in relative.parts:
        raise RuntimeError("reference receipt path is not relative")
    path = (base/relative).resolve()
    if not path.is_relative_to(base.resolve()):
        raise RuntimeError("reference receipt path escapes its directory")
    return path


def _hashed_bytes(path, digest, label):
    payload = path.read_bytes()
    if hashlib.sha256(payload).hexdigest() != digest:
        raise RuntimeError("changed Guderley " + label)
    return payload


def load_eigenvalue_cache(cache_path=None, reference_dir=None):
    """Validate the original computation, its inputs, and unchanged sources.

    The cache contains an executed result, not a replacement table constant.
    Its literal SHA binds the receipt/contract descriptors. The original twelve
    source files are retained and checked in the historical bundle; current
    upstream modules must still match those original bindings. Only this
    adapter and the explicit regeneration driver are intentionally revised.
    Optional paths support failure-path checks without mutating released data.
    """
    base = REFERENCE_DIR if reference_dir is None else Path(reference_dir)
    path = base/"eigenvalue-cache.json" if cache_path is None else Path(cache_path)
    try:
        payload = _hashed_bytes(path, EIGENVALUE_CACHE_SHA256, "eigenvalue cache")
        cache = json.loads(payload)
        if (cache["schema_version"] != 1 or cache["geometry"] != 3
                or cache["gamma"] != GAMMA or cache["source_commit"] != EXACTPACK_COMMIT):
            raise RuntimeError("cached Guderley eigenvalue has incompatible fixed inputs")
        qdesc, cdesc = cache["qualification"], cache["original_reference_contract"]
        qualification = json.loads(_hashed_bytes(_safe_path(base, qdesc["file"]),
                                                  qdesc["sha256"], "original qualification"))
        contract = json.loads(_hashed_bytes(_safe_path(base, cdesc["file"]),
                                             cdesc["sha256"], "original reference contract"))
        if (contract["geometry"] != 3 or contract["fixed_gamma"] != GAMMA
                or contract["declared_before_reference_execution"] is not True
                or contract["no_PDE_evolution"] is not True):
            raise RuntimeError("original eigenvalue contract has incompatible inputs")
        archived = _safe_path(base, cache["original_source_prefix"])
        for name, digest in contract["files_sha256"].items():
            _hashed_bytes(_safe_path(archived, name), digest, "archived source: " + name)
        expected_current = {name:digest for name,digest in contract["files_sha256"].items()
                            if name not in {"precollapse.py", "qualify_reference.py"}}
        if cache["current_sources_sha256"] != expected_current:
            raise RuntimeError("incomplete current Guderley source bindings")
        for name, digest in expected_current.items():
            _hashed_bytes(_safe_path(base, name), digest, "current upstream source: " + name)
        meta, checks = qualification["metadata"], qualification["checks"]
        if (qualification["passed"] is not True or len(checks) != 8
                or not all(value is True for value in checks.values())
                or meta["geometry"] != 3 or meta["gamma"] != GAMMA
                or meta["rho0"] != RHO0 or meta["shock_scale"] != SHOCK_SCALE
                or meta["lazarus_times"] != [TIME0,TIME1]
                or meta["domain"] != [0,OUTER_RADIUS]
                or qualification["reflected_branch_executed"] is not False):
            raise RuntimeError("original Guderley qualification does not cover fixed inputs")
        value, alpha = float(cache["lambda"]), float(cache["alpha"])
        cdiff = float(cache["stored_Cdiff"])
        if (not all(math.isfinite(x) for x in [value,alpha,cdiff])
                or value != meta["lambda"] or alpha != meta["alpha"]
                or cdiff != qualification["eigenvalue"]["Cdiff"]
                or value <= 1 or not 0 < alpha < 1
                or abs(alpha*value-1) > 2e-15
                or abs(value/TABULATED_LAMBDA-1) >= 2e-9
                or abs(cdiff) >= 2e-7):
            raise RuntimeError("cached Guderley exponent failed its original qualification")
        return {"lambda":value, "alpha":alpha,
                "cache_sha256":EIGENVALUE_CACHE_SHA256,
                "qualification_sha256":qdesc["sha256"],
                "contract_sha256":cdesc["sha256"],
                "stored_Cdiff":cdiff, "current_sources_sha256":expected_current,
                "original_source_files_checked":len(contract["files_sha256"]),
                "mode":"hash-qualified reused ExactPack eigenvalue",
                "eigenvalue_recomputed":False}
    except (OSError, KeyError, TypeError, ValueError) as error:
        raise RuntimeError("invalid Guderley eigenvalue cache: " + str(error)) from error


@lru_cache(maxsize=2)
def eigenvalue(recompute=False):
    """Reuse qualified work by default; full ExactPack shooting is opt-in."""
    if not recompute:
        return load_eigenvalue_cache()["lambda"]
    value = float(exponent_module.eexp(3, GAMMA))
    if not np.isfinite(value) or value <= 1:
        raise RuntimeError("invalid Guderley similarity eigenvalue")
    return value


@lru_cache(maxsize=1)
def critical_phase_residual():
    """One fresh Cdiff evaluation at the qualified alpha, without root search."""
    # Upstream Cdiff reads these globals even though it accepts dummy arguments.
    exponent_module.n = 3
    exponent_module.g = GAMMA
    value = float(exponent_module.Cdiff(1.0/eigenvalue(), 3, GAMMA))
    if not math.isfinite(value):
        raise RuntimeError("nonfinite Guderley critical-phase residual")
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

    def __init__(self, *, recompute_eigenvalue=False):
        self.lambda_ = eigenvalue(recompute=recompute_eigenvalue)
        self.eigenvalue_provenance = (
            {"mode":"fresh ExactPack nonlinear eigenvalue shooting", "eigenvalue_recomputed":True}
            if recompute_eigenvalue else load_eigenvalue_cache())
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
                "eigenvalue_provenance":self.eigenvalue_provenance,
                "source_independence":"qualified ExactPack eigenvalue reused; unchanged pre-collapse RHS freshly integrated"}


PrecollapseReference = GuderleyReference
