# Small quantum and coupled-dynamics representatives

This packet defines fixed small educational models, mathematical references and acceptance goals. Actual execution status is recorded in `verification.json` and `results/result.json`. The scoped names and explicit remaining limitations in `cards.json` do not imply general material calculations.

## 95: a real electronic/nuclear coupling in a two-state model

The authored electronic Hamiltonian is

\[
H_e(Q)=\frac{kQ^2}{2}I+\begin{pmatrix}-\Delta&gQ\\gQ&\Delta\end{pmatrix},\quad
\psi(\theta)=(\cos\theta,\sin\theta)^T.
\]

Thus \(E(Q,\theta)=kQ^2/2-\Delta\cos2\theta+gQ\sin2\theta\). It contains an actual electronic degree of freedom, not a prescribed classical harmonic force. Its BO minimum is \(E_-(Q)=kQ^2/2-\sqrt{\Delta^2+g^2Q^2}\), with \(\theta_0=-\operatorname{atan2}(gQ,\Delta)/2\). The BO nuclear force is \(-kQ+g^2Q/\sqrt{\Delta^2+g^2Q^2}\).

The explicitly chosen CP-type action is \(L=M\dot Q^2/2+\mu\dot\theta^2/2-E\). Since the orbital has unit norm identically, its Euler–Lagrange equations are

\[
M\ddot Q=-kQ-g\sin2\theta,\quad
\mu\ddot\theta=-2\Delta\sin2\theta-2gQ\cos2\theta.
\]

Here \(\mu\) is the declared angle-coordinate fictitious mass. It is not silently equated to a particular production code's orbital-mass convention. The conserved model energy contains **both** nuclear and fictitious electronic kinetic energies. The nuclear BO energy alone is not a CP conserved quantity. Initial \(\dot\theta\) follows the derivative of the BO angle times nuclear velocity.

Three fixed dyadic steps compare BO and \(\mu=0.04\) CP integration against fixed RK4 companions with 4096 and 8192 steps. The companion difference must be at most \(10^{-10}\), well below the \(10^{-5}\) state-comparison goal; this is an observed reference sensitivity check, not a rigorous global-error bound. The additional \(\mu=0.01\) trajectory receives energy diagnostics only, with no separately qualified state-reference claim.

One nuclear OU update uses \(v'=av+bz\), \(a=e^{-\gamma h}\), \(b^2=(T/M)(1-a^2)\), fixed Gaussian seed and one short trajectory. Its conditional variance identity \(a^2+b^2M/T=1\) qualifies the thermostat transition, not sampled equilibration. Each OU update saves its actual heat \(\Delta K_n\). We compare \(E_{extended}(t)-E_{extended}(0)-\sum\Delta K_n\), retain raw kinetic-temperature histories, and make no canonical-distribution, ergodic or transport claim. This is a limited coupled BO/CP-type educational representative, not first-principles or long-time CPMD validation.

## 96: unchanged atomic references

Hydrogenic atomic units, \(u=rR\), \(\int |u|^2dr=1\), \(E_n=-Z^2/(2n^2)\), orbital degeneracy and finite Dirichlet-grid limits follow the earlier selected DLMF/source reading. For the helium one-spatial-orbital model, \(p=2|u|^2\), \(n=p/(4\pi r^2)\), \(\int p\,dr=2\). Positive interior nodes avoid a sampled division by zero. HF cancellation \(E_x=-E_H/2\) is special to this two-electron model; exchange-only LDA is a different approximation, not exact correlated helium. The packet copies exactly three stored energy rows, each with 40 uncontracted s functions; it computes no SCF or independent reference anew.

## 97: finite differences, continuum formulas and roundoff

For \(M\) box intervals, \(h=1/M\), the central-difference matrix has diagonal \(h^{-2}\) and off-diagonal \(-1/(2h^2)\). Sine substitution gives

\[
\lambda_j=2h^{-2}\sin^2(j\pi/(2M)),\quad q_i=\sqrt2\sin(j\pi i/M),\quad h\sum q_i^2=1.
\]

The independent scalar oracle uses Decimal precision90, Machin's identity for pi with an alternating next-term stopping criterion, and 100 sine-series terms. Its fixed arguments satisfy \(0<z<1/6\); truncation is far below binary64 rounding and the unchanged \(2\times10^{-12}\) relative comparison goal. The final Decimal-to-binary64 rounding contributes at most half an ULP. This is separate from the primary NumPy/LAPACK error.

The box relative continuum error satisfies \(e(z)=1-(\sin z/z)^2\), \(z^2/3-2z^4/45\le e(z)\le z^2/3\). These inequalities establish the draft finest \(10^{-3}\) goal and doubling-ratio interval [3.5,4.5] for the selected real-valued grids, independently of results.

For the HO, \(\psi_0=\pi^{-1/4}e^{-x^2/2}\), \(\psi_1=\sqrt2x\psi_0\), \(\psi_2=(2x^2-1)\psi_0/\sqrt2\), \(E_n=n+1/2\). Direct substitution and Gaussian moments establish these low-state formulas, parity and nodes. Whole-line functions remain raw for field error; no renormalization hides their omitted tails. Finite-wall and finite-difference shifts can cancel. Fixed-domain mesh changes and fixed-mesh domain changes are sensitivities, not separately certified error bounds. The unchanged HO0.003 target is an accuracy goal, not a rigorous finite-h guarantee.

The eight full NumPy eigensolves return824 native eigenpairs;24 low pairs are selected. All824 native eigenpairs are saved before conversion. The Euclidean norm gate applies to the24 selected native vectors before multiplying them by \(h^{-1/2}\); it does not qualify the other800 vectors. Scaling and sign errors are distinguished. Thresholded nodes, their masks and the predeclared HO physical window are diagnostics because the scaled backward residual does not certify pointwise signs near exact nodes or tiny tails.

## 98–99: finite molecular spaces

All nuclei are clamped point H nuclei, positions in bohr, energies in hartree, with the exact explicit H STO-3G contraction already stored in the atlas. There is one **contracted** s AO per H, with three primitives; this differs from the40 uncontracted helium functions. No angular-momentum basis, basis scan or external library is added.

RHF/UHF use \(F_\alpha=h+J[P_\alpha+P_\beta]-K[P_\alpha]\) and its beta counterpart, exact overlap orthogonalization without discarding eigenvectors, and fixed damping/stopping rules. The reported spin square for one alpha and one beta electron is \(1-|c_\alpha^TSc_\beta|^2\). A zero SCF commutator alone is not a stability or global-minimum proof.

For the orthonormal spatial-orbital product basis with one alpha and one beta electron,

\[
\mathcal H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs).
\]

This4x4 H2 or9x9 H3+ matrix is independently assembled again using signed fermion creation/annihilation operators. The common integral data are shared; this checks many-body assembly, not an independent external integral engine. The ground vector's spatial coefficient matrix must be symmetric for the H3+ singlet.

H2 at1.4 and3.0 bohr additionally uses the unchanged independently stored PySCF RHF values. With gerade/ungerade orbitals \(g,u\), put \(A=(gg|gg), B=(uu|uu), J=(gg|uu), K=(gu|gu)\). The paired broken-spin ansatz has \(x=\sin^2\theta\), orbitals \(c_\alpha=\sqrt{1-x}g+\sqrt{x}u\), \(c_\beta=\sqrt{1-x}g-\sqrt{x}u\), and energy

\[
E(x)=2h_{gg}+A+E_{NN}+[2(h_{uu}-h_{gg})-2A+2J-4K]x+[A+B-2J+4K]x^2.
\]

The minimum on [0,1] is an independent scalar variational oracle in this explicitly symmetric paired family. The even-singlet FCI2x2 block has diagonal \(2h_{gg}+A,2h_{uu}+B\) and off-diagonal K, giving a separate closed-form ground energy. Finite-basis FCI is not continuum exact chemistry; broken-spin UHF is not a pure singlet.

The distinct99 representative is fixed triangular H3+ with two electrons and3 AOs. Canonical two-electron RHF MP2 simplifies to

\[
E_{MP2}^{corr}=\sum_{a,b>0}\frac{(0a|0b)^2}{2\epsilon_0-\epsilon_a-\epsilon_b}.
\]

This is checked independently from reference-to-double-excitation entries of the many-electron Hamiltonian and their Moller–Plesset denominators. MP2 is not variational; no MP2/FCI ordering is required. General molecular DFT, CC, general multireference methods and chemical-accuracy claims remain outside the implemented representative.

## 100–101: saved He audit versus a new authored periodic model

The existing He cell, local-only GTH potential, XC identifiers, engine versions, six-coordinate finite differences and independent Gaussian/PW values are copied unchanged. The audit recomputes arithmetic from stored values and applies original bounds; no electronic calculation, basis/k/cutoff refinement or independent reference regeneration is repeated.

The new101 model has only \(G=-1,0,1\), two fixed k values, kinetic diagonal \((G+k)^2/2\), \(V_{G-G'}=-0.1\) for neighbor waves, and \(\eta\beta\beta^\dagger\), where \(\beta_G=e^{-(G+k)^2/(2\sigma^2)}e^{-i(G+k)R}\). The latter is a genuine nonlocal rank-one kernel, but not an element-fitted norm-conserving potential.

At fixed **mean** electron number, spin-degenerate \(f=2/[1+e^{(\epsilon-\mu)/T}]\). The chosen N=1.5 is an independent-particle Fermi occupation count, not an integer-particle canonical many-body distribution. Stable positive/negative exponential branches avoid exponent clipping; exact binary64 endpoint occupations are recorded. Entropy evaluates \(x\log x=0\) at x=0 without artificial floors. We retain \(U=\sum wf\epsilon\), \(S=-\sum w[f\log(f/2)+(2-f)\log(1-f/2)]\), and \(F=U-TS\). The force is \(-\sum wf\langle u|\partial_RH|u\rangle=-\partial_RF|_{\langle N\rangle}\); differentiating U alone would omit the entropy response and is a tested negative control. The cubic Hermitian3x3 spectral oracle records any roundoff-domain clamp; the fixed center cases require no clamp activation. This model does not establish real-metal, material, self-consistent Hartree/XC or long-MD accuracy.
