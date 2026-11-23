The independent reference uses unordered scalar Cartesian pairs and an exact
finite six-source octahedral configuration. The latter qualifies the DIRECT
REFERENCE only; it is not a separate production-FMM golden-target run.
Actual FMM fields are compared with independent direct sums at all64particles,
including adaptive and rigid-transform probes. This is3D free-space -G/r,
not the old2D-log FMM and not FMM3D's+1/(4pi r) normalization.

Tensor-Chebyshev source weights W_abc=sum_j m_j La(yjx)Lb(yjy)Lc(yjz).
Parent weights are formed from child weights using parent basis values at
child nodes. M2L uses K(x_target_node,y_source_node)=-1/distance.
Parent local fields are interpolated to child nodes before leaf evaluation.
Acceleration differentiates the SAME local polynomial, including1/halfwidth.
Node-coincident derivative limits are explicit barycentric differentiation.
M2M/L2L use three separable contractions; M2L stays dense with p^6 entries.
Each source-target owner is counted once; production never constructs a global
dense particle-kernel matrix. The N-by-N integer ownership audit is not a kernel.

The standard64particle problem forces actual levels2and3, regardless of leaf
capacity. The separate adaptive configuration uses capacity8/maxdepth3 and
keeps overfull capped buckets. A nonzero potential contribution using an
internal-source M2M, internal-target M2L and descendant L2L is propagated
separately to final particles. This avoids an all-direct or unused-pass claim.
Far acceptance requires summed circumsphere radii/distance<=.5, which separates
all accepted interpolation-node pairs. References/citations state exactly the
selected Fong--Darve sections read; SVD compression/timings were not reproduced.
