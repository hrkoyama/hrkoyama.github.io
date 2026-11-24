# Boundary repair: independently derived fixed candidate, not yet executed

All primary source scopes remain honest: the2003Lallemand/Luo original article
was read as selected extracted text via the author-content mirror at
https://www.academia.edu/126173532/Lattice_Boltzmann_method_for_moving_boundaries
(sec3printed410–414, Eq12/13/15 discussion). No local primaryPDF or rendered
symbol audit is claimed. The2001BFL full text remains unread.

For NEE, the official abstract was actually read at
https://cpb.iphy.ac.cn/en/article/doi/10.1088/1009-1963/11/4/310 . The author-upload
ResearchGate page exposes the same abstract; clicking its fullPDF link returned404.
Thus the fullNEEoriginal equations were not inspected. The adopted all-nine
poststream variant below is independently derived, not falsely identified as the
exact author-paper implementation or copied source.

## Quadratic curved links

Let c point from fluid node x toward the wall at x+q*c; f_o is the outgoing
postcollision population and f_b its opposite. Coordinates along c are normalized
by one link. Following the reflected characteristic:

- If0<q<1/2, interpolate the outgoing polynomial at s=2q−1 from s=0,−1,−2.
  Lagrange weights are q(1+2q),1−4q²,−q(1−2q).
- If1/2<q<=1, interpolate the incoming polynomial at s=0 from
  s=2q−1,−1,−2. Weights are1/[q(2q+1)],(2q−1)/q,−(2q−1)/(2q+1).
  The three values are f_o(x),f_b(x),f_b(x−c), since streaming relocates the
  opposite-direction values by−c.

This recovers the quadratic form of the selected Eq12 under the declared
outgoing-coordinate convention. Atq=.5 use exact halfway reversal, not a
near-singular branch or a repaired value. Moving-wall correction is
−6*w*(c.u_w) for the short branch and that quantity/[q(2q+1)] for the long
branch, with rho_ref1. The sign follows equilibrium reflection: for uniform
tangential translation f_eq,o−6*w*c.u_w=f_eq,b. On the long branch this
correction carries the first interpolation weight. This independently checks
the paper's alternative indexing/weight conventions rather than trusting OCR.

Weights include negative values. Positivity or unconditional stability is NOT
guaranteed. No density/population floor, clipping, silent SBB fallback or omitted
neighbor exists. Required back/back2 indices are validated; actual fixed main
geometries must pass support enumeration before any new flow. Grazing outer-wall
links deserve explicit enumeration, not an unsupported general availability claim.

The independent scalar oracle forms generic Lagrange products from the three
node locations, instead of duplicating the expanded native coefficients.
Degree0/1/2 goldens, qnear0/.5/1, stationary and uniformly moving-wall equilibrium,
q=.5 linear/quad reduction, original linear negative controls and failure guards
are frozen before execution.

## All-nine NEE outlet

At a fixed outlet wet node b, let a be its adjacent interior node in the same
row AFTER collision/streaming/wall/inlet handling. Compute rho_a,u_a directly
from all nine streamed f_a. Then set rho_b=1,u_b=u_a and

    f_i,b = f_i,eq(1,u_a) + f_i,a − f_i,eq(rho_a,u_a), i=0..8.

Equilibrium moment identities imply sum f_b=1 and sum c_i*f_i,b=u_a, without
renormalizing any interior node or modifying the prescribed inlet. This is an
explicit finite reservoir BC, not FEATflow's do-nothing condition. The original
1996benchmark allows a user-selected outflow. The complete outlet wet node,
including the first/last row next to the halfway walls, belongs to NEE; the
adjacent interior node has the actual wall closure. There is no periodic wrap.

Streaming first subtracts the three lost outgoing populations. For EVERY newly
assigned outlet population add delta=f_new−f_streamed to the open ledger:
dM+=delta, dP+=c_i*delta. This includes the six already-known streamed values;
accounting only for the three missing values is wrong and is a frozen negative
control. No collision is evaluated at nonpositive interior density.

## Scope and unchanged conditions

Original8run curved main failed; all arrays/logs/contracts are retained. The
saved-data audit locates instability at outlet-adjacent x2.19 and shows the
annular pointwise pressure error is predominantly azimuthal. Radial averaging
or fitted pressure scaling is not an acceptance replacement.

Only this separate curved candidate changes boundaries. BGK collision,
Ui/nu/tau/grid/T, true circlegeometry, reference field/pointwise pressure gate,
force units and all original acceptance thresholds stay fixed. Successful
cavity/TGVsources stay byte-identical. Component qualification is not main
success: no new physical trajectory is authorized by writing this proposal.
