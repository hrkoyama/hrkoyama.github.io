"""Numerical/reference tests independent of the frozen full-case gates."""
import unittest

import numpy as np

import noh_reference as reference
import noh_solver as solver


class NohReferenceTests(unittest.TestCase):
    def test_known_gamma53_states_and_jump(self):
        for d, rho, p in [(1, 4, 4 / 3), (2, 16, 16 / 3), (3, 64, 64 / 3)]:
            par = reference.parameters(d)
            self.assertAlmostEqual(par["rho_post"], rho)
            self.assertAlmostEqual(par["pressure_post"], p)
            self.assertAlmostEqual(par["shock_density_jump"], 4)
            self.assertAlmostEqual(par["shock_speed"], 1 / 3)

    def test_exact_cell_averages_against_split_point_quadrature(self):
        for d in (1, 2, 3):
            edges = np.array([0.0, 0.035, 0.17, 0.23, 0.6, 1.0])
            exact, _ = reference.cell_averages(edges, 0.6, d)
            quadrature = reference.integrate_reference_by_gauss(edges, 0.6, d)
            np.testing.assert_allclose(exact, quadrature, rtol=3e-14, atol=3e-14)

    def test_crossing_cell_pressure_average_is_not_pressure_of_average(self):
        gamma = 5 / 3
        q, mean_p = reference.cell_averages(np.array([0.17, 0.23]), 0.6, 2)
        pressure_of_mean = solver.primitive(q, gamma)[2]
        self.assertGreater(pressure_of_mean[0], mean_p[0])
        # Total energy is half the mass in the true cold Noh solution.
        self.assertAlmostEqual(q[0, 2], 0.5 * q[0, 0])

    def test_global_integrals_include_time_dependent_radial_inflow(self):
        for d in (1, 2, 3):
            edges = np.linspace(0, 1, 38)
            q, _ = reference.cell_averages(edges, 0.6, d)
            volume = np.diff(edges**d) / d
            mass, energy = reference.exact_integrals(1, 0.6, d)
            self.assertAlmostEqual(float(np.dot(q[:, 0], volume)), mass, places=13)
            self.assertAlmostEqual(float(np.dot(q[:, 2], volume)), energy, places=13)


class NohSolverTests(unittest.TestCase):
    def test_cold_state_is_not_replaced_by_positive_pressure_floor(self):
        q = solver.conservative(np.ones(8), -np.ones(8), np.zeros(8), 5 / 3)
        before = q.copy()
        rho, velocity, pressure, sie, sound = solver.primitive(q, 5 / 3)
        np.testing.assert_array_equal(q, before)
        np.testing.assert_array_equal(pressure, 0)
        np.testing.assert_array_equal(sie, 0)
        np.testing.assert_array_equal(sound, 0)

    def test_geometric_static_pressure_cancellation(self):
        for d in (1, 2, 3):
            edges = np.linspace(0, 1, 17)
            q = solver.conservative(np.ones(16), np.zeros(16), np.full(16, 2.0), 5 / 3)
            rhs, _, _, _ = solver.operator(q, 0.0, edges, d, 5 / 3, 1.0, -1.0)
            # The outer prescribed cold inflow intentionally differs here;
            # exclude its last cell while testing geometry + origin balance.
            np.testing.assert_allclose(rhs[:-1], 0, atol=3e-14, rtol=0)

    def test_origin_generates_heat_without_injecting_mass_or_energy(self):
        edges = np.linspace(0, 1, 33)
        q = solver.conservative(np.ones(32), -np.ones(32), np.zeros(32), 5 / 3)
        for d in (1, 2):
            rhs, net, source, _ = solver.operator(q, 0.0, edges, d, 5 / 3, 1.0, -1.0)
            volume = np.diff(edges**d) / d
            np.testing.assert_allclose(np.sum(rhs * volume[:, None], axis=0), net + source, atol=2e-14)
            self.assertEqual(source[0], 0)
            self.assertEqual(source[2], 0)
            stage = q + 0.001 * rhs
            self.assertGreater(solver.primitive(stage, 5 / 3)[2][0], 0)

    def test_cylindrical_outer_boundary_density_grows_in_time(self):
        state = solver.inflow(0.6, 1.0, 2, 5 / 3, 1.0, -1.0)
        np.testing.assert_allclose(state, [1.6, -1.6, 0.8], rtol=1e-15)

    def test_rejects_genuinely_negative_internal_energy(self):
        with self.assertRaises(FloatingPointError):
            solver.primitive(np.array([[1.0, -1.0, 0.49]]), 5 / 3)


if __name__ == "__main__":
    unittest.main()
