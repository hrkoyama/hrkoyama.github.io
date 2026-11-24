import cmath,hashlib,json,math,tempfile,unittest
from pathlib import Path
import lab

class FoundationsLabTests(unittest.TestCase):
    def test_contract_matches_frozen_bytes(self):
        base=Path(__file__).parent;c=json.loads((base/'contract.json').read_text())
        self.assertEqual(hashlib.sha256((base/'inputs.json').read_bytes()).hexdigest(),c['input_sha256'])
        self.assertEqual(hashlib.sha256((base/'review.json').read_bytes()).hexdigest(),c['review_sha256'])
    def test_weighted_norm_and_rms_are_distinct(self):
        v=[1.,-1.,0.,2.];self.assertAlmostEqual(lab.norm(v,.5),math.sqrt(2)*math.sqrt(sum(x*x for x in v)/4))
    def test_thomas_matches_known_nonsymmetric_system(self):
        x=lab.tridiagonal([-2.,-1.],[4.,5.,3.],[-1.,-2.],[2.,2.,7.])
        for a,b in zip(x,[1.,2.,3.]):self.assertAlmostEqual(a,b)
    def test_thomas_rejects_singular_system(self):
        with self.assertRaises(ValueError):lab.tridiagonal([-1.],[1.,1.],[-1.],[0.,0.])
    def test_forward_euler_stability_boundary(self):
        self.assertEqual(lab.R('forward',-2.),-1.);self.assertGreater(abs(lab.R('forward',-2.01)),1.)
    def test_backward_euler_damps_stiff_modes(self):self.assertLess(abs(lab.R('backward',-1e8)),1e-7)
    def test_trapezoidal_stiff_limit_does_not_damp_to_zero(self):self.assertAlmostEqual(lab.R('trapezoidal',-1e8),-1.,places=6)
    def test_astable_rational_methods_on_left_half_plane_samples(self):
        for x in [-100.,-2.,-.1,0.]:
            for y in [-30.,-1.,0.,7.]:
                for m in ['backward','trapezoidal']:self.assertLessEqual(abs(lab.R(m,complex(x,y))),1+1e-14)
    def test_periodic_upwind_preserves_constant_and_mass(self):
        u=[1.,2.,-1.,3.];v=lab.advect(u,.6,'upwind');self.assertAlmostEqual(sum(v),sum(u));self.assertEqual(lab.advect([2.]*8,.6,'upwind'),[2.]*8)
    def test_upwind_courant_one_is_exact_grid_shift(self):
        u=[2.,-1.,3.,7.];self.assertEqual(lab.advect(u,1.,'upwind'),[u[-1],*u[:-1]])
    def test_modal_amplification_matches_independent_one_step(self):
        for m in ['upwind','lax-wendroff','ftcs']:
            n=32;k=3;theta=2*math.pi*k/n;u=[cmath.exp(1j*theta*j) for j in range(n)];v=lab.advect(u,.6,m)
            self.assertLess(max(abs(a-lab.symbol(m,theta,.6)*b) for a,b in zip(v,u)),1e-13)
    def test_spectral_group_velocity_matches_phase_derivative(self):
        for m in ['upwind','lax-wendroff']:
            theta=.7;nu=.6;e=1e-6;g=lab.symbol(m,theta,nu);gp=-1j*nu*cmath.exp(-1j*theta) if m=='upwind' else -1j*nu*math.cos(theta)-nu**2*math.sin(theta)
            numerical=-(cmath.phase(lab.symbol(m,theta+e,nu))-cmath.phase(lab.symbol(m,theta-e,nu)))/(2*e*nu)
            self.assertAlmostEqual(numerical,-(gp/g).imag/nu,places=8)
    def test_heat_discrete_sine_eigenvalue(self):
        n=20;r=.4;u=[math.sin(math.pi*j/n) for j in range(n+1)];u[0]=u[-1]=0;v=lab.heat_step(u,r);G=1-4*r*math.sin(math.pi/(2*n))**2
        self.assertLess(max(abs(x-G*y) for x,y in zip(v,u)),1e-14)
    def test_poisson_manufactured_fields_converge(self):
        for kind in ['dirichlet','neumann','robin','mixed-good']:
            errors=[]
            for n in [16,32]:
                x,u,v,res=lab.poisson(n,kind);errors.append(max(abs(a-b) for a,b in zip(u,v)));self.assertLess(res,1e-10)
            self.assertGreater(math.log2(errors[0]/errors[1]),1.8)
    def test_pure_neumann_zero_mean_and_all_rows(self):
        x,u,v,res=lab.poisson(32,'neumann');self.assertAlmostEqual((sum(u)-.5*(u[0]+u[-1]))/32,0.,places=13);self.assertLess(res,1e-12)
    def test_robin_rejects_nonpositive_boundary_parameters(self):
        with self.assertRaises(ValueError):lab.poisson(16,'robin',alpha=-1.)
    def test_symplectic_euler_modified_quadratic(self):
        q,p=.7,-.4;h=.1;a=lab.modified_energy(q,p,h,'symplectic');qn,pn=lab.oscillator_step(q,p,h,'symplectic');self.assertAlmostEqual(lab.modified_energy(qn,pn,h,'symplectic'),a,places=14)
    def test_verlet_modified_quadratic(self):
        q,p=.7,-.4;h=.1;a=lab.modified_energy(q,p,h,'verlet');qn,pn=lab.oscillator_step(q,p,h,'verlet');self.assertAlmostEqual(lab.modified_energy(qn,pn,h,'verlet'),a,places=14)
    def test_symplecticity_is_not_exact_physical_energy(self):
        for m in ['symplectic','verlet']:
            q,p=lab.oscillator_step(1.,0.,.2,m);self.assertGreater(abs((q*q+p*p)/2-.5),1e-6)
    def test_verlet_is_time_symmetric(self):
        q,p=lab.oscillator_step(.7,-.4,.15,'verlet');q,p=lab.oscillator_step(q,p,-.15,'verlet');self.assertAlmostEqual(q,.7,places=14);self.assertAlmostEqual(p,-.4,places=14)
    def test_general_symplectic_euler_is_not_time_symmetric(self):
        q,p=lab.oscillator_step(.7,-.4,.15,'symplectic');q,p=lab.oscillator_step(q,p,-.15,'symplectic');self.assertGreater(math.hypot(q-.7,p+.4),1e-4)
    def test_symplectic_matrices_have_unit_determinant_in_one_dof(self):
        for m in ['symplectic','verlet']:
            a=lab.oscillator_step(1,0,.1,m);b=lab.oscillator_step(0,1,.1,m);self.assertAlmostEqual(a[0]*b[1]-a[1]*b[0],1,places=14)
    def test_all_fixed_acceptance_checks(self):
        p=json.loads((Path(__file__).parent/'inputs.json').read_text());metrics,checks,rows=lab.experiment(p);self.assertTrue(all(checks.values()),[k for k,v in checks.items() if not v]);self.assertEqual(len(rows),15)
    def test_nonempty_output_is_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t);(p/'existing.txt').write_text('keep')
            with self.assertRaises(ValueError):lab.run(Path(__file__).parent/'inputs.json',p)
            self.assertEqual((p/'existing.txt').read_text(),'keep')

if __name__=='__main__':unittest.main()
