Selected sources and exact read scope are recorded in citations.json/source-review.json. No third-party solver was run or source copied. Derived analytic/manufactured fields are explicitly distinguished from historical benchmark reproduction.

The L-shaped domain removes quadrant IV from [-1,1]^2. The angle is
atan2 modulo 2pi, restricted to 0..3pi/2. Its harmonic field is
r^(2/3) sin(2theta/3), with Cartesian gradient
(2/3)r^(-1/3)[sin(-theta/3),cos(-theta/3)]. The singular vertex is
never a quadrature point. Triangles touching it are rotated so that
the Duffy map (lambda0,lambda1,lambda2)=(1-s,s(1-t),st) has Jacobian s
at that vertex. Gauss48 and96 are compared there; ordinary triangles
use8 and12. This explicitly resolves a fractional singularity instead
of silently applying a low-order smooth-polynomial rule.

For the annulus define s=x^2+y^2,D=x^2-y^2,
A(s)=(s-1)(4-s),B=A'=5-2s,C=A''=-2. Our derived exact Cartesian
velocity is [A(1+xy),AD/2]. The first component contains a radial
Cartesian contribution so that the global traction budget is nonzero;
the xy/D terms make this a genuine two-dimensional vector problem.
mu=1+s/5. If G=grad(u), tau=mu(G+G^T), the body force is -div(tau).
references/fields.py expands these derivatives; a separate Cartesian
central difference of tau qualifies f at fixed off-axis points.
The exact rational-point golden at x=y=1 is u=[4,0],
G=[[6,6],[2,-2]], f=[128/5,104/5]. This is derived here, not a number
attributed to an external CFD package.

For x=r cos(theta),y=r sin(theta), the physical Q1 gradient is
[cos(theta) d_r-sin(theta)/r d_theta,
 sin(theta) d_r+cos(theta)/r d_theta]. The volume Jacobian is r,
and circular face measure is r dtheta. With engineering strain
[u_x,v_y,u_y+v_x], the element coefficient is mu diag(2,2,1).
This gives the actual Cartesian block weak form and viscous work.
The radial A e_x contribution integrates to total outward traction
3pi sum_r sign(r) mu(r) A_r(r) r = -756pi/5; angular xy/D
contributions integrate to zero. Thus integral(f)=[756pi/5,0],
checked separately from the algebraic boundary reaction and numerical
one-sided physical traction. r>=1; no axis stencil, pressure equation,
incompressibility constraint or Navier--Stokes claim is made.

The Neumann and Robin manufactured fields are cos(2pi x)cos(2pi y)
and cos(pi x)cos(2pi y)+x+y respectively, with sources8pi^2 times
the first cosine product and5pi^2 times the second. For -Delta u=f,
the outward-gradient compatibility is integral(f)+integral(d_n u)=0.
Robin elimination uses u_b=u_i+(h/2)d_n u and therefore
d_n u=(g-alpha u_i)/(beta+alpha h/2). The boundary relation's
algebraic residual is reported separately from its continuous flux
error. The pure Neumann mean constraint uses volume weights; a source+1
is rejected, not projected. Compatible CG checks the same matrix and
is not an independently discretized PDE reference.
