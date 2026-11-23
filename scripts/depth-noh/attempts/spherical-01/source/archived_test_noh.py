"""Numerical/reference tests independent of the frozen full-case gates."""
import hashlib
import json
import math
from pathlib import Path
import unittest
from unittest import mock

import numpy as np

import noh_reference as reference
import noh_solver as solver
import run as runner


class NohReferenceTests(unittest.TestCase):
    def test_pinned_independent_exactpack_snapshot(self):
        root = Path(__file__).resolve().parent
        payload = (root / "exactpack-reference-snapshot.json").read_bytes()
        receipt = json.loads((root / "exactpack-reference-receipt.json").read_text())
        self.assertEqual(hashlib.sha256(payload).hexdigest(), receipt["snapshot_sha256"])
        self.assertTrue(receipt["passed"])
        snapshot = json.loads(payload)
        for case in snapshot["cell_average_cases"]:
            q, p = reference.cell_averages(case["edges"], case["time"], case["geometry"])
            np.testing.assert_allclose(q, case["conserved_cell_averages"], rtol=2e-12, atol=2e-12)
            np.testing.assert_allclose(p, case["pressure_cell_averages"], rtol=2e-12, atol=2e-12)
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
            for rho in [np.ones(16), 1 + np.linspace(0, 1, 16)]:
                q = solver.conservative(rho, np.zeros(16), np.full(16, 2.0), 5 / 3)
                rhs, _, _, _ = solver.operator(q, 0.0, edges, d, 5 / 3, 1.0, -1.0)
                # The outer prescribed cold inflow intentionally differs here;
                # density contacts may diffuse, but radial momentum stays zero.
                np.testing.assert_allclose(rhs[:-1, 1], 0, atol=3e-14, rtol=0)

    def test_uniform_velocity_cold_density_gradient_has_no_geometric_stress(self):
        edges = np.linspace(0, 1, 17)
        rho = 1 + np.linspace(0, 1, 16)
        q = solver.conservative(rho, -np.ones(16), np.zeros(16), 5 / 3)
        for d in (1, 2, 3):
            rhs, _, source_integral, _ = solver.operator(q, 0, edges, d, 5 / 3, 1, -1)
            # Exclude origin and imposed outer boundary. At constant u=-1,
            # zero numerical stress means momentum RHS = -density RHS.
            np.testing.assert_allclose(rhs[1:-1, 1], -rhs[1:-1, 0], atol=4e-14, rtol=0)
            if d == 1:
                np.testing.assert_array_equal(source_integral, 0)

    def test_origin_generates_heat_without_injecting_mass_or_energy(self):
        edges = np.linspace(0, 1, 33)
        q = solver.conservative(np.ones(32), -np.ones(32), np.zeros(32), 5 / 3)
        for d in (1, 2, 3):
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

    def test_spherical_outer_boundary_matches_independent_constants(self):
        state = solver.inflow(0.6, 1.0, 3, 5 / 3, 1.0, -1.0)
        np.testing.assert_allclose(state, [2.56, -2.56, 1.28], rtol=1e-15, atol=0)
        mass, energy = reference.exact_integrals(1.0, 0.6, 3)
        self.assertAlmostEqual(mass, 512 / 375, places=14)
        self.assertAlmostEqual(energy, 256 / 375, places=14)

    def test_dt_cubed_diagnostic_tracks_every_actual_step(self):
        # Observe both stage times independently of the solver's accumulator.
        # Multiple steps exercise CFL changes and the shortened final step.
        with mock.patch.object(solver, "operator", wraps=solver.operator) as traced:
            result = solver.solve(16, 3, final_time=0.02)
        stage_times = [call[0][1] for call in traced.call_args_list]
        self.assertEqual(len(stage_times), 2 * result["steps"])
        self.assertGreater(result["steps"], 1)
        steps = [stage_times[i + 1] - stage_times[i] for i in range(0, len(stage_times), 2)]
        self.assertTrue(all(step > 0 for step in steps))
        independent = math.fsum(step**3 for step in steps)
        self.assertAlmostEqual(result["dt_cubed_sum"], independent, delta=1e-14 * independent)
        self.assertEqual(result["history"][-1]["dt_cubed_sum"], result["dt_cubed_sum"])

    def test_spherical_trapezoidal_boundary_bias_on_nonuniform_steps(self):
        # Independent integration of prescribed quadratic boundary influx,
        # not a comparison of a formula with the same solver accumulator.
        times = [0.0, 0.07, 0.2, 0.6]
        dt_cubed = math.fsum((b - a)**3 for a, b in zip(times[:-1], times[1:]))
        trapezoidal_mass_influx = math.fsum(
            0.5 * ((1 + a)**2 + (1 + b)**2) * (b - a)
            for a, b in zip(times[:-1], times[1:])
        )
        mass_difference = 1 / 3 + trapezoidal_mass_influx - 512 / 375
        energy_difference = 1 / 6 + 0.5 * trapezoidal_mass_influx - 256 / 375
        expected_mass, expected_energy = runner.spherical_boundary_bias(dt_cubed)
        self.assertGreater(expected_mass, 0)
        self.assertAlmostEqual(mass_difference, expected_mass, places=14)
        self.assertAlmostEqual(energy_difference, expected_energy, places=14)
        self.assertAlmostEqual(expected_mass, dt_cubed / 6, places=14)
        self.assertAlmostEqual(expected_energy, dt_cubed / 12, places=14)

    def test_rejects_genuinely_negative_internal_energy(self):
        with self.assertRaises(FloatingPointError):
            solver.primitive(np.array([[1.0, -1.0, 0.49]]), 5 / 3)

    def test_rejects_invalid_and_boundary_overtaking_inputs(self):
        for kwargs in [{"gamma": float("nan")}, {"rho0": float("inf")},
                       {"cfl": 0}, {"final_time": 4}, {"n": 16.5}]:
            options = {"n": 16, "dimension": 2}
            options.update(kwargs)
            with self.assertRaises(ValueError):
                solver.solve(**options)


if __name__ == "__main__":
    unittest.main()
