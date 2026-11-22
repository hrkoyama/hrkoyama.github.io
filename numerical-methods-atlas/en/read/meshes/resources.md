# Structured, unstructured, and triangular meshes

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/meshes/

A geometry/connectivity demonstration for structured, unstructured and triangular meshes. Links identify its source and focused checks; FEM, ALE, SPH and flow executions in other chapters are not inherited as this demonstration's governing equations, exact solutions or PDE validation.

## Methods

No chapter-specific association is registered. Atlas-wide index: [Methods and code reference](https://hrkoyama.github.io/numerical-methods-atlas/methods/?lang=en)

## Equations

No chapter-specific association is registered. Atlas-wide index: [Equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en)

## Problem figures

No chapter-specific association is registered. Atlas-wide index: [Test problems by name and figure](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=en)

## Exact / reference solutions

No chapter-specific association is registered. Atlas-wide index: [Exact and reference solutions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en)

## Code and validation

- [Source for mesh geometry and connectivity](<https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/geometry.py>)
  availability: source

  The relevant routines are example_meshes, mesh_topology and polygon_area. They construct areas and face-sharing adjacency for structured quadrilaterals, split-lattice triangles and a deterministic irregular triangulation. The shared module also contains SPH and moving-volume routines; this association covers mesh geometry and connectivity only.
- [Unit-square mesh area, topology and adjacency checks](<https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py>)
  availability: source

  From the extracted distribution, run python -m pytest -q tests/test_time_geometry.py -k test_mesh_areas_topology_and_neighbors_cover_unit_square. Checks cover positive cell areas, unit total area, reciprocal face adjacency, connectivity and V−E+F_cells=1. Other time-integration/SPH/ALE checks in the file and finite-element or unstructured-flow solver verification retain their separate scopes.
- [Existing shared code distribution / ZIP](<https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip>)
  availability: source

  The existing shared distribution contains the source and tests linked above. Run the focused check commands from the extracted distribution folder. The archive also contains other chapters’ code; the notes on each link identify the scope checked here.
