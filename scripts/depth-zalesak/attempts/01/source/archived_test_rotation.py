"""Twenty-six checks of the limited 2D update and its independent geometry."""
import hashlib
import json
from pathlib import Path
import tempfile
import numpy as np
import pytest
import rotation as s
from references import geometry as g
import run as runner


def smooth(n=8):
    x = (np.arange(n)+.5)/n
    return .5+.2*np.sin(2*np.pi*x[None, :])*np.cos(2*np.pi*x[:, None])


def test_01_discrete_velocity_divergence_is_zero():
    assert s.flow(16)['divergence_max'] == 0
    assert s.flow(16, (.5+1/32, .5+1/32))['divergence_max'] == 0


def test_02_opposite_normal_periodic_faces_agree():
    f = s.flow(16)
    assert np.array_equal(f['u'][:, 0], f['u'][:, -1])
    assert np.array_equal(f['v'][0], f['v'][-1])


def test_03_velocity_turns_upper_disk_leftward():
    f = s.flow(32)
    assert f['u'][23, 15] < 0
    assert f['v'][23, 15] < 0 < f['v'][23, 16]


def test_04_minmod_keeps_smaller_common_sign():
    assert np.array_equal(s.minmod(np.array([1., -2., 4.]), np.array([3., -1., 2.])), [1., -1., 2.])


def test_05_minmod_flattens_extrema():
    assert np.array_equal(s.minmod(np.array([1., -2., 0.]), np.array([-3., 1., 2.])), [0., 0., 0.])


def test_06_four_reconstruction_faces_preserve_mean():
    q = smooth()
    assert np.max(abs(sum(s.reconstruct(q, 'muscl-minmod'))/4-q)) < 5e-16


def test_07_reconstruction_faces_remain_in_neighbor_bounds():
    q = smooth();neighbors = [q, np.roll(q, 1, 0), np.roll(q, -1, 0), np.roll(q, 1, 1), np.roll(q, -1, 1)]
    for face in s.reconstruct(q, 'muscl-minmod'):
        assert np.all(face >= np.minimum.reduce(neighbors))
        assert np.all(face <= np.maximum.reduce(neighbors))


def test_08_constant_field_is_preserved():
    q = np.full((8, 8), .7);f = s.flow(8)
    for method in ['donor-cell', 'muscl-minmod']:
        out, stats = s.forward_euler(q, f, .001, method)
        assert np.array_equal(out, q)


def test_09_shared_periodic_flux_conserves_mass():
    q = smooth();out, stats = s.forward_euler(q, s.flow(8), .001)
    assert abs((out-q).sum()/64) < 2e-17
    assert stats['fe_mass_defect'] < 2e-16


def test_10_out_of_band_state_is_rejected_without_repair():
    q = smooth();q[2, 3] = -.01
    with pytest.raises(s.StageFailure) as failure:
        s.forward_euler(q, s.flow(8), .001)
    assert np.array_equal(failure.value.state, q)


def test_11_nonfinite_state_is_rejected():
    q = smooth();q[0, 0] = np.nan
    with pytest.raises(s.StageFailure):s.forward_euler(q, s.flow(8), .001)


def test_12_excessive_face_courant_is_rejected():
    with pytest.raises(ValueError):s.forward_euler(smooth(), s.flow(8), 1.)


def test_13_unknown_reconstruction_is_rejected():
    with pytest.raises(ValueError):s.reconstruct(smooth(), 'unimplemented-fct')


def test_14_fe_positive_convex_decomposition_matches_shared_flux():
    q = smooth();f = s.flow(8);dt = .01;z = dt/f['h']
    for method in ['donor-cell', 'muscl-minmod']:
        l, r, d, u = s.reconstruct(q, method)
        own = ((.25-z*np.maximum(-f['u'], 0))*l
               +(.25-z*np.maximum(f['u'], 0))*r
               +(.25-z*np.maximum(-f['v'], 0))*d
               +(.25-z*np.maximum(f['v'], 0))*u)
        incoming = z*(f['up']*np.roll(r, 1, 1)-f['um']*np.roll(l, -1, 1)
                       +f['vp']*np.roll(u, 1, 0)-f['vm']*np.roll(d, -1, 0))
        actual, stats = s.forward_euler(q, f, dt, method)
        assert np.max(abs(actual-(own+incoming))) < 5e-16
        coefficient_sum = (1-z*(abs(f['u'])+abs(f['v']))
                           +z*(f['up']-f['um']+f['vp']-f['vm']))
        assert np.max(abs(coefficient_sum-1)) < 5e-16


def test_15_all_ssp_fe_and_convex_stages_are_recorded():
    out = s.solve(smooth(), final_time=.001)
    assert out['stage_data'].shape == (3*out['steps'], len(s.STAGE_COLUMNS))
    columns = dict(zip(s.STAGE_COLUMNS, out['stage_data'].T))
    assert set(columns['stage']) == {1., 2., 3.}
    assert np.array_equal(out['snapshot_times'], np.linspace(0., .001, 5))


def test_16_ssp_preserves_mass_and_bounds():
    out = s.solve(smooth(), final_time=.001)
    assert abs(out['final_mass']-out['initial_mass']) < 2e-15
    assert out['q'].min() >= 0 and out['q'].max() <= 1


def test_17_zero_state_remains_zero_with_no_state_clipping():
    out = s.solve(np.zeros((8, 8)), final_time=.001)
    assert not np.any(out['q'])
    assert out['state_clip_count'] == out['retries'] == out['rejected_steps'] == 0


def test_18_quarter_grid_rotation_covariance_of_the_update():
    q = smooth();f = s.flow(8)
    for method in ['donor-cell', 'muscl-minmod']:
        a, _ = s.forward_euler(q, f, .001, method)
        b, _ = s.forward_euler(np.rot90(q, -1), f, .001, method)
        assert np.max(abs(np.rot90(a, -1)-b)) < 3e-16


def test_19_short_evolution_moves_the_upper_centroid_left():
    q = np.zeros((8, 8));q[5:7, 3:5] = 1
    out = s.solve(q, final_time=.002)
    centroid = runner.discrete_centroid(out['q'], 1/8)
    assert centroid[0] < .4996 and abs(centroid[1]-.75) < 1e-5


def test_20_slot_probe_has_exact_area_and_a_projection_baseline():
    edges = np.linspace(0., 1., 33)
    args = dict(rotation_center=(.5, .5), shape_center=(.5, .75),
                radius=.15, slot_width=.05, slot_top=.85)
    w = runner.slot_probe(edges, 0., args)
    assert abs(w.sum()/32**2-.025*.175) < 2e-15
    q = g.cell_averages(edges)
    # An exact geometric projection can already fill a cell-mean probe:
    # reporting numerical probe q without this baseline would be misleading.
    assert np.sum(q*w)/w.sum() > 0


def test_21_circle_enclosed_by_polygon_has_analytic_area():
    polygon = np.array([[-1., -1.], [1., -1.], [1., 1.], [-1., 1.]])
    assert abs(g.circle_polygon_area(polygon, .15)-np.pi*.15**2) < 2e-16


def test_22_circle_quadrant_has_quarter_area():
    polygon = np.array([[0., 0.], [1., 0.], [1., 1.], [0., 1.]])
    assert abs(g.circle_polygon_area(polygon, .15)-np.pi*.15**2/4) < 2e-16


def test_23_rotated_and_shifted_cell_areas_match_total_area():
    edges = np.linspace(0., 1., 17)
    area = g.total_area()
    for angle, delta in [(0., 0.), (np.pi/4, 0.), (0., 1/32)]:
        q = g.cell_averages(edges, angle, (.5+delta, .5+delta),
                            (.5+delta, .75+delta), .15, .05, .85+delta)
        assert 0 <= q.min() <= q.max() <= 1
        assert abs(q.sum()/16**2-area) < 3e-12


def test_24_exact_quarter_and_full_rotation_return_geometry():
    edges = np.linspace(0., 1., 17);q = g.cell_averages(edges)
    assert np.max(abs(g.cell_averages(edges, np.pi/2)-np.rot90(q, -1))) < 3e-12
    assert np.max(abs(g.cell_averages(edges, 2*np.pi)-q)) < 3e-12


def test_25_modified_frozen_input_is_rejected_before_execution():
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary);p = root/'inputs.json';p.write_text('{}\n')
        digest = hashlib.sha256(p.read_bytes()).hexdigest()
        (root/'pre-run-contract.json').write_text(json.dumps({'files_sha256': {'inputs.json': digest}}))
        runner.check_frozen_sources(root)
        p.write_text('{"changed":true}\n')
        with pytest.raises(ValueError):runner.check_frozen_sources(root)


def test_26_true_centroid_rotates_counterclockwise():
    a, b = g.centroid(), g.centroid(angle=np.pi/2)
    assert a[1] > .75 and abs(a[0]-.5) < 3e-15
    expected = np.array([.5-(a[1]-.5), .5+(a[0]-.5)])
    assert np.max(abs(b-expected)) < 3e-15
