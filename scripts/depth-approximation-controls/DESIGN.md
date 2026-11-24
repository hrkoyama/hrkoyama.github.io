# Independent formulas and pre-run reasoning

All claims here specify the fixed protocol, not observed successful outcomes.

## Barycentric rounding certificate

At a certificate probe z let exact stored-input terms be
`t_j=w_j/(z-x_j)`, `D=sum(t_j)`, `N=sum(t_j*y_j)`, `R=N/D`.
The primary path explicitly rounds subtraction, division, multiplication,
sequential additions, then the final quotient. For binary64 `u=2^-53`, m terms
and `gamma=(m-1)*u/(1-(m-1)*u)`, set

```
e_t = (1+u)/(1-u)-1
e_D = (1+e_t)*(1+gamma)-1
e_N = (1+e_t)*(1+u)*(1+gamma)-1
E_D = e_D*sum(abs(t_j))
E_N = e_N*sum(abs(t_j*y_j))
B_0 = (E_N+abs(R)*E_D)/(abs(D)-E_D)
B = (1+u)*B_0+u*abs(R)
```

Exact Fraction arithmetic checks `E_D<abs(D)` and the actual evaluation defect
against B. The saved trace also checks normal-or-exact-zero arithmetic scope;
the fixed problem has no overflow or subnormal regime. A node hit returns the
stored datum directly, outside the divided expression. The weighted Lebesgue
ratio `sum(abs(t_j))/abs(D)` is a conditioning diagnostic, not an error estimate
for the original function. P/R and C/P representation defects are computed as
exact Fraction differences before their final scalar serialization.

For Clenshaw, use full coefficients, not DLMF's primed-series c0 convention:
`b_k=a_k+2*z*b_(k+1)-b_(k+2)` for k=n..1, then
`C=a_0+z*b_1-b_2`. Each stage has rounded product p, difference m and sum b.
An absolute local bound is
`u*(abs(2*z*b1)+abs(p-b2)+abs(m+a_k))`.
Propagate `E=2*abs(z)*E1+E2+local` and use the analogous final three-operation
bound. Scaling z by two is exact for these normal dyadic probes. Independent
Fraction T_k forward recurrence evaluates the exact stored series. These
operation-based bounds need not be tight near poorly conditioned evaluations.

The Decimal110 node check uses Machin's pi formula and alternating atan/cosine
series with last term below 1e-105; for |angle|<=pi/2 the decreasing alternating
tail is bounded by the next term. Decimal rounding is over ninety digits below
the declared 2^-50 table-accuracy condition. This qualifies a supplied node table;
it does not claim correctly rounded trigonometric generation or an exact DCT.

## Rational spline reference

With h_i=x_(i+1)-x_i, m_i=(y_(i+1)-y_i)/h_i and nodal second derivatives M,
the interior equation is
`h_(i-1)*M_(i-1)+2*(h_(i-1)+h_i)*M_i+h_i*M_(i+1)=6*(m_i-m_(i-1))`.
Natural boundary rows set M0=Mn=0. Clamped rows are
`2*h0*M0+h0*M1=6*(m0-dleft)` and
`h_last*M_(n-1)+2*h_last*Mn=6*(dright-m_last)`.
Each interval's ascending power coefficients are
`[y_i, m_i-h_i*(2*M_i+M_(i+1))/6, M_i/2, (M_(i+1)-M_i)/(6*h_i)]`.
All arithmetic uses Fraction conversions of actual stored values. This path
shares no B-spline basis, collocation matrix or de Boor recurrence with primary.
Derivative and continuity checks distinguish natural/clamped C2 from PCHIP C1.

For the equally spaced plateau, the natural M/(b-a) vector is
`[0,-6/11,24/11,-24/11,6/11,0]`; the zero-clamped vector is
`[6/19,-12/19,42/19,-42/19,12/19,-6/19]`.
At x=1.5 these yield the two documented negative witnesses. Since a<1/64 and
b-a>1/2, both are strictly negative for the actual binary64 inputs.

PCHIP uses zero interior slope for a zero or opposite-sign adjacent secant;
otherwise it uses the weighted harmonic mean. A one-sided raw slope is reset
when its sign disagrees with the first secant, or capped at three times that
secant when adjacent signs disagree and the raw magnitude is too large.
The seven explicit fixtures exercise retained, reset, positive/negative cap,
opposite-sign uncapped, leading-zero and constant branches on both ends.

## Haar matrix and padding reference

The primary normalized pair acts on [a,b] by [(a+b)/sqrt(2),(a-b)/sqrt(2)].
The reference separately constructs low/high matrices with explicit duplicate
columns for odd padding, then multiplies level matrices using einsum. Synthesis
uses independent coefficient selector matrices and cropped inverse pairs;
`S*A=I` is checked even when A is rectangular. A second reference keeps all
unnormalized pair sums/differences in Fraction and divides each level by
`sqrt(2)^level` in Decimal80.

The squared-energy ledger telescopes with the actual appended sample at every
level. For critical length32 the transform is square orthogonal, so Parseval
also applies to an arbitrary thresholded coefficient difference. At length17,
redundancy and cropping invalidate that inference. The explicit padding-energy
ledger replaces the unsupported orthogonality claim. Shift-back discrepancies
are measured for fixed one-sample cyclic shifts, not required to vanish.
