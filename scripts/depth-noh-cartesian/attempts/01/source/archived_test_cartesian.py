import json
from pathlib import Path
import unittest
from unittest.mock import patch
import numpy as np
import cartesian_solver as s
import cartesian_reference as r
from run import parity_error, decisions


class CartesianNohTests(unittest.TestCase):
    def test_true_zero_pressure_is_not_replaced(self):
        q = s.cold_state(np.array([.2, .3]), np.array([.1, .4]), 0)
        before = q.copy()
        np.testing.assert_allclose(s.primitive(q)[3], 0, atol=2e-16)
        np.testing.assert_array_equal(q, before)

    def test_negative_internal_energy_rejected(self):
        with self.assertRaises(FloatingPointError):
            s.primitive(np.array([1., 2., 0., .5]))

    def test_nonfinite_and_nonpositive_density_rejected(self):
        for q in [np.array([0.,0.,0.,1.]), np.array([1.,0.,0.,np.nan])]:
            with self.assertRaises(FloatingPointError): s.primitive(q)

    def test_equal_state_flux_and_wave_speed(self):
        q = np.array([[2., 1., -.5, 4.]])
        pressure = (s.GAMMA-1)*(4-.5*(1+.25)/2)
        expected = np.array([[1., .5+pressure, -.25, .5*(4+pressure)]])
        f, speed = s.rusanov(q, q, 0)
        np.testing.assert_allclose(f, expected, rtol=2e-15)
        np.testing.assert_allclose(speed, .5+np.sqrt(s.GAMMA*pressure/2), rtol=2e-15)

    def test_axis_rotation_exchanges_both_momenta(self):
        q = np.array([[2., 1., -.5, 4.]])
        fx, _ = s.flux(q, 0)
        fy, _ = s.flux(q[..., [0,2,1,3]], 1)
        np.testing.assert_allclose(fx, fy[..., [0,2,1,3]], rtol=0, atol=0)

    def test_outer_face_flux_against_independent_gauss_integration(self):
        nodes, weights = np.polynomial.legendre.leggauss(24)
        edges = np.array([-.5, -.23, .12, .5])
        for x in [-.5, .5]:
            for time in [0., .37, .6]:
                y = .5*(edges[:-1,None]+edges[1:,None])+.5*np.diff(edges)[:,None]*nodes
                q = s.cold_state(np.full_like(y,x), y, time)
                expected = .5*np.einsum('ijk,j->ik',s.flux(q,0)[0],weights)
                np.testing.assert_allclose(s.cold_x_face_flux(x,edges,time),expected,rtol=3e-14,atol=3e-15)

    def test_cartesian_operator_telescopes_all_four_conserved_quantities(self):
        e = np.linspace(-.5,.5,9);c=.5*(e[:-1]+e[1:]);x,y=np.meshgrid(c,c)
        q=s.cold_state(x,y,0);q[...,0]*=1+.03*np.cos(3*x)*np.sin(5*y)
        # Independent nonsymmetric, admissible warm field; no radial projection.
        q[...,1]=.2*q[...,0];q[...,2]=-.13*q[...,0];q[...,3]=2+.5*(.2**2+.13**2)*q[...,0]
        rhs, net, rate=s.operator(q,.2,e)
        np.testing.assert_allclose(np.sum(rhs,axis=(0,1))*(e[1]-e[0])**2,net,atol=3e-14,rtol=3e-14)
        self.assertGreater(rate,0)

    def test_transverse_coupling_is_present_in_both_directions(self):
        q=np.zeros((8,8,4));q[...,0]=1;q[...,3]=2;q[4,4,3]=3
        rhs,_,_=s.operator(q,0,np.linspace(-.5,.5,9))
        self.assertNotEqual(rhs[4,3,1],0)  # x pressure gradient
        self.assertNotEqual(rhs[3,4,2],0)  # y pressure gradient

    def test_invalid_mesh_or_budget_rejected(self):
        for kw in [{'n':9},{'n':True},{'n':8,'cfl':.6},{'n':8,'final_time':2.},{'n':8,'maximum_seconds':0}]:
            with self.assertRaises(ValueError):s.solve(**kw)

    def test_short_full_square_update_has_closed_budgets_and_d4_parity(self):
        z=s.solve(8,final_time=.01)
        np.testing.assert_allclose(z['final_integral']-z['initial_integral'],z['boundary_net_integral'],atol=3e-15,rtol=1e-13)
        self.assertLess(parity_error(z['q']),2e-14)
        self.assertEqual(z['state_floor_count'],0)
        self.assertEqual(z['time'],.01)

    def test_invalid_predictor_is_retained_without_retry_or_repair(self):
        def invalid(q,time,edges):
            rhs=np.zeros_like(q);rhs[...,0]=-1000
            return rhs,np.zeros(4),1.
        with patch.object(s,'operator',side_effect=invalid) as mock:
            with self.assertRaises(FloatingPointError) as caught:s.solve(8,final_time=.01)
            self.assertEqual(mock.call_count,1)
            self.assertTrue(np.any(caught.exception.failed_state[...,0]<0))
            self.assertEqual(caught.exception.failed_context['stage'],'Euler predictor')

    def test_radial_point_values_match_reused_pinned_exactpack(self):
        data=json.loads((Path(__file__).parent/'exactpack-snapshot.json').read_text())
        self.assertEqual(data['commit'],'9bacc477eb791e959c9621e771fc7a725db755fa')
        rows=[x for x in data['point_cases'] if x['geometry']==2]
        self.assertEqual(len(rows),4)
        for row in rows:
            rho,p,u=r.points(row['radius'],row['time'])
            mask=abs(np.array(row['radius'])-row['time']/3)>1e-12
            self.assertGreaterEqual(int(mask.sum()),4)
            for actual,expected in [(rho,row['density']),(p,row['pressure']),(u,row['radial_velocity'])]:
                np.testing.assert_allclose(actual[mask],np.array(expected)[mask],rtol=2e-14,atol=2e-14)

    def test_inverse_radius_rectangle_has_known_square_integral(self):
        self.assertAlmostEqual(float(r.inverse_radius_rectangle(-.5,.5,-.5,.5)),4*np.arcsinh(1),places=14)

    def test_inverse_radius_rectangle_matches_independent_quadrature_away_from_origin(self):
        x,w=np.polynomial.legendre.leggauss(32)
        xx=.45+.15*x[:,None];yy=.25+.1*x[None,:]
        quad=.015*np.sum(w[:,None]*w[None,:]/np.hypot(xx,yy))
        self.assertAlmostEqual(float(r.inverse_radius_rectangle(.3,.6,.15,.35)),quad,places=14)

    def test_initial_density_reference_is_uniform(self):
        rho,p=r.cell_means(np.linspace(-.5,.5,17),0)
        np.testing.assert_array_equal(rho,np.ones((16,16)));np.testing.assert_array_equal(p,np.zeros_like(rho))

    def test_cut_cell_reference_is_bounded_and_resolves_disk_area(self):
        e=np.linspace(-.5,.5,33);rho,p=r.cell_means(e,.6,64)
        dx=e[1]-e[0]
        self.assertTrue(np.isfinite(rho).all());self.assertGreater(rho.min(),0)
        self.assertLess(abs(np.sum(p)*dx**2-(16/3)*np.pi*.2**2),2e-7)
        self.assertLess(abs(np.sum(rho)*dx**2/r.total_mass(.6)-1),5e-8)
        np.testing.assert_allclose(rho,rho.T,atol=3e-6,rtol=0)

    def test_reference_quadrature_refinement_is_far_below_pde_error(self):
        e=np.linspace(-.5,.5,33);a,_=r.cell_means(e,.6,64);b,_=r.cell_means(e,.6,128)
        self.assertLess(np.sum(abs(a-b))/np.sum(abs(b)),1e-5)

    def test_global_mass_formula_and_flux_rate(self):
        t=.37;h=1e-5
        derivative=(r.total_mass(t+h)-r.total_mass(t-h))/(2*h)
        self.assertAlmostEqual(derivative,4*np.arcsinh(1)+2*np.pi*t,places=9)
        self.assertEqual(r.total_mass(0),1.)

    def test_missing_grid_cannot_be_reported_as_pass(self):
        self.assertFalse(decisions([],{'limits':{}},{'grids':[32,64,128]})[0]['passed'])


if __name__ == '__main__':unittest.main()
