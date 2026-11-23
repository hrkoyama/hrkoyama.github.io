The binary has r=x2-x1, m1=.6,m2=.4,G=M=a=1,e=.4,epsilon0.
Its exact eccentric anomaly solves E-e sin(E)=n t with n=sqrt(GM/a^3).
The bracket[M-e,M+e] is valid and the derivative1-e cos(E) is positive.
r=a[cos(E)-e,sqrt(1-e²)sin(E),0],
v=an/(1-e cos(E))[-sin(E),sqrt(1-e²)cos(E),0].
COM splitting is x1=-m2 r/M,x2=m1 r/M, likewise velocities.
Exact energy=-Gm1m2/(2a); Lz=mu sqrt(GMa(1-e²)).
JPL supplies context for Kepler-equation/plane conversion only; no fitted
planet elements or approximate planetary ephemeris are used here.

The cold32body initial positions are deterministic radial quantiles of a
Plummer-density CDF truncated at r3, with16 Fibonacci directions and their
antipodal partners. Explicit coordinates, not a mutable sampler, are inputs.
All initial velocities are0: this is NOT an equilibrium Plummer DF or an
exact continuum orbit. Density scalea1 and pair softeningepsilon.05 differ.
The exact physical finite-N Hamiltonian uses the same softened pair potential
as the force, and is evaluated with synchronized full-step velocities.

The DOP853 reference uses a separately coded unordered scalar pair loop,
the same physical ODE, two frozen tolerance pairs and all81finest time nodes.
It is a temporal/numerical reference, not an analytic32body solution.
Time error compares direct KDK with this reference. Tree trajectory error
compares equal dt. Pure force error compares BH/direct at IDENTICAL held
direct-path positions at five fixed times. No force floor is used.

Errors use fixed position/velocity scales1; momentum is scaled byMv0,
angular momentum byMa0v0,COM bya0,energy byabs(E0),all nonzero.
Do not divide by initial cold velocity/P/L/COM,which arezero.
Antipodal symmetry can hide general BH momentum errors; a separate asymmetric
static probe records net force without recentering. Targetwise MAC force is
not claimed globally reciprocal, Hamiltonian or symplectic. KDK composition
is independently derived; unavailable original Verlet/Plummer paper access
is explicitly not promoted in the scoped source records.
