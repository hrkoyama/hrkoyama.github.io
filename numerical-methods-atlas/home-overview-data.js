/** Navigation model: areas overlap; scientific inventories remain in their catalogs. */
export const homeAreas = [
  {
    "id": "foundations",
    "name": "home-map.areas.0.name",
    "hint": "home-map.areas.0.hint",
    "question": "home-map.areas.0.question",
    "description": "home-map.areas.0.description",
    "groups": [
      [
        {
          "name": "home-map.areas.0.groups.0.0.name",
          "route": "/read/stability",
          "kind": "reading"
        },
        {
          "name": "home-map.areas.0.groups.0.1.name",
          "route": "/time-integration",
          "kind": "interactive"
        }
      ],
      [
        {
          "name": "home-map.areas.0.groups.1.0.name",
          "route": "/read/stability",
          "kind": "reading"
        },
        {
          "name": "ui.a-l-stability-error-norms.9e1533",
          "route": "/read/accuracy-stability",
          "kind": "reading"
        },
        {
          "name": "autodiff.home-title",
          "route": "/read/automatic-differentiation",
          "kind": "reading"
        },
        {
          "name": "sensitivity.home-title",
          "route": "/read/adjoint",
          "kind": "reading"
        },
        {
          "name": "inverse.home-title",
          "route": "/read/bratu-inverse",
          "kind": "reading"
        },
        {
          "name": "multinverse.home-title",
          "route": "/read/bratu-multi-inverse",
          "kind": "reading"
        }
      ],
      [
        {
          "name": "home-map.areas.0.groups.2.0.name",
          "route": "/experiments",
          "kind": "interactive"
        },
        {
          "name": "home-map.areas.0.groups.2.1.name",
          "route": "/convergence",
          "kind": "interactive"
        }
      ]
    ],
    "entry": "/experiments",
    "overview": "/read/stability",
    "execution": [
      {
        "name": "home-map.execution.advection-sine",
        "route": "/numerical-methods-atlas/code-and-data/examples/advection-sine/",
        "kind": "execution"
      },
      {
        "name": "home-map.execution.harmonic-oscillator",
        "route": "/numerical-methods-atlas/code-and-data/examples/harmonic-oscillator/",
        "kind": "execution"
      },
      {
        "name": "home-map.execution.stiff-cosine",
        "route": "/numerical-methods-atlas/code-and-data/examples/stiff-cosine/",
        "kind": "execution"
      }
    ]
  },
  {
    "id": "waves",
    "name": "home-map.areas.1.name",
    "hint": "home-map.areas.1.hint",
    "question": "home-map.areas.1.question",
    "description": "home-map.areas.1.description",
    "groups": [
      [
        {
          "name": "home-map.areas.1.groups.0.0.name",
          "route": "/equations",
          "kind": "interactive"
        },
        {
          "name": "home-map.areas.1.groups.0.1.name",
          "route": "/read/benchmarks",
          "kind": "reading"
        }
      ],
      [
        {
          "name": "home-map.areas.1.groups.1.0.name",
          "route": "/read/advanced",
          "kind": "reading"
        },
        {
          "name": "home-map.areas.1.groups.1.1.name",
          "route": "/reconstruction",
          "kind": "interactive"
        }
      ],
      [
        {
          "name": "home-map.areas.1.groups.2.0.name",
          "route": "/shock-robustness",
          "kind": "interactive"
        },
        {
          "name": "home-map.areas.1.groups.2.1.name",
          "route": "/read/nasa-2d",
          "kind": "reading"
        }
      ]
    ],
    "entry": "/equations",
    "overview": "/read/benchmarks",
    "execution": [
      {
        "name": "home-map.execution.sod",
        "route": "/numerical-methods-atlas/code-and-data/examples/sod/",
        "kind": "execution"
      },
      {
        "name": "home-map.execution.shu-osher",
        "route": "/numerical-methods-atlas/code-and-data/examples/shu-osher/",
        "kind": "execution"
      }
    ]
  },
  {
    "id": "diffusion",
    "name": "home-map.areas.2.name",
    "hint": "home-map.areas.2.hint",
    "question": "home-map.areas.2.question",
    "description": "home-map.areas.2.description",
    "groups": [
      [
        {
          "name": "home-map.areas.2.groups.0.0.name",
          "route": "/read/elliptic",
          "kind": "reading"
        },
        {
          "name": "home-map.areas.2.groups.0.1.name",
          "route": "/read/hyperbolic-diffusion",
          "kind": "reading"
        }
      ],
      [
        {
          "name": "home-map.areas.2.groups.1.0.name",
          "route": "/read/elliptic",
          "kind": "reading"
        },
        {
          "name": "home-map.areas.2.groups.1.1.name",
          "route": "/read/sparse-nonlinear",
          "kind": "reading"
        }
      ],
      [
        {
          "name": "home-map.areas.2.groups.2.0.name",
          "route": "/poisson-comparison",
          "kind": "interactive"
        },
        {
          "name": "home-map.areas.2.groups.2.1.name",
          "route": "/exact-solutions",
          "kind": "interactive"
        }
      ]
    ],
    "entry": "/poisson-comparison",
    "overview": "/read/elliptic",
    "execution": [
      {
        "name": "home-map.execution.poisson-1d-dirichlet",
        "route": "/numerical-methods-atlas/code-and-data/examples/poisson-1d-dirichlet/",
        "kind": "execution"
      },
      {
        "name": "home-map.execution.poisson-2d-sine",
        "route": "/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/",
        "kind": "execution"
      },
      {
        "name": "home-map.execution.bratu",
        "route": "/numerical-methods-atlas/code-and-data/examples/bratu/",
        "kind": "execution"
      }
    ]
  },
  {
    "id": "approximation",
    "name": "home-map.areas.3.name",
    "hint": "home-map.areas.3.hint",
    "question": "home-map.areas.3.question",
    "description": "home-map.areas.3.description",
    "groups": [
      [
        {
          "name": "home-map.areas.3.groups.0.0.name",
          "route": "/meshes",
          "kind": "interactive"
        },
        {
          "name": "home-map.areas.3.groups.0.1.name",
          "route": "/read/geophysical-grids",
          "kind": "reading"
        }
      ],
      [
        {
          "name": "home-map.areas.3.groups.1.0.name",
          "route": "/read/fem",
          "kind": "reading"
        },
        {
          "name": "home-map.areas.3.groups.1.1.name",
          "route": "/read/history",
          "kind": "reading"
        }
      ],
      [
        {
          "name": "home-map.areas.3.groups.2.0.name",
          "route": "/basis",
          "kind": "interactive"
        },
        {
          "name": "home-map.areas.3.groups.2.1.name",
          "route": "/cip",
          "kind": "interactive"
        }
      ]
    ],
    "entry": "/basis",
    "overview": "/read/fem",
    "execution": [
      {
        "name": "home-map.execution.smooth-function-projection",
        "route": "/numerical-methods-atlas/code-and-data/examples/smooth-function-projection/",
        "kind": "execution"
      }
    ]
  },
  {
    "id": "particles",
    "name": "home-map.areas.4.name",
    "hint": "home-map.areas.4.hint",
    "question": "home-map.areas.4.question",
    "description": "home-map.areas.4.description",
    "groups": [
      [
        {
          "name": "home-map.areas.4.groups.0.0.name",
          "route": "/read/particle-gravity",
          "kind": "reading"
        },
        {
          "name": "home-map.areas.4.groups.0.1.name",
          "route": "/read/lattice-boltzmann",
          "kind": "reading"
        }
      ],
      [
        {
          "name": "home-map.areas.4.groups.1.0.name",
          "route": "/read/gsph",
          "kind": "reading"
        },
        {
          "name": "term.concept.chapman-enskog",
          "route": "/read/chapman-enskog",
          "kind": "reading"
        }
      ],
      [
        {
          "name": "home-map.areas.4.groups.2.0.name",
          "route": "/hamiltonian",
          "kind": "interactive"
        },
        {
          "name": "home-map.areas.4.groups.2.1.name",
          "route": "/read/gravity-boundaries",
          "kind": "reading"
        }
      ]
    ],
    "entry": "/hamiltonian",
    "overview": "/read/particle-gravity",
    "execution": [
      {
        "name": "home-map.execution.barnes-hut",
        "route": "/numerical-methods-atlas/code-and-data/examples/barnes-hut/",
        "kind": "execution"
      },
      {
        "name": "home-map.execution.periodic-particles",
        "route": "/numerical-methods-atlas/code-and-data/examples/periodic-particles/",
        "kind": "execution"
      }
    ],
    "plans": [
      {
        "name": "home-map.planned.ewald",
        "route": "/numerical-methods-atlas/methods/ewald/",
        "kind": "planned"
      },
      {
        "name": "home-map.planned.pme",
        "route": "/numerical-methods-atlas/methods/pme/",
        "kind": "planned"
      },
      {
        "name": "home-map.planned.spme",
        "route": "/numerical-methods-atlas/methods/spme/",
        "kind": "planned"
      }
    ]
  },
  {
    "id": "coupled",
    "name": "home-map.areas.5.name",
    "hint": "home-map.areas.5.hint",
    "question": "home-map.areas.5.question",
    "description": "home-map.areas.5.description",
    "groups": [
      [
        {
          "name": "home-map.areas.5.groups.0.0.name",
          "route": "/read/mhd",
          "kind": "reading"
        },
        {
          "name": "home-map.areas.5.groups.0.1.name",
          "route": "/read/biological-models",
          "kind": "reading"
        }
      ],
      [
        {
          "name": "home-map.areas.5.groups.1.0.name",
          "route": "/read/mhd",
          "kind": "reading"
        },
        {
          "name": "home-map.areas.5.groups.1.1.name",
          "route": "/read/incompressible",
          "kind": "reading"
        }
      ],
      [
        {
          "name": "home-map.areas.5.groups.2.0.name",
          "route": "/mhd-tests",
          "kind": "interactive"
        },
        {
          "name": "home-map.areas.5.groups.2.1.name",
          "route": "/read/relativistic-hydrodynamics",
          "kind": "reading"
        }
      ]
    ],
    "entry": "/mhd-tests",
    "overview": "/read/mhd",
    "execution": [
      {
        "name": "home-map.execution.taylor-green",
        "route": "/numerical-methods-atlas/code-and-data/examples/taylor-green/",
        "kind": "execution"
      },
      {
        "name": "home-map.execution.brio-wu",
        "route": "/numerical-methods-atlas/code-and-data/examples/brio-wu/",
        "kind": "execution"
      }
    ]
  },
  {
    "id": "quantum",
    "name": "home-map.areas.6.name",
    "hint": "home-map.areas.6.hint",
    "question": "home-map.areas.6.question",
    "description": "home-map.areas.6.description",
    "overview": "/read/quantum-chemistry",
    "entry": "/read/quantum-chemistry",
    "groups": [
      [
        {
          "name": "home-map.areas.6.groups.0.0.name",
          "route": "/read/quantum-chemistry",
          "kind": "reading"
        },
        {
          "name": "home-map.areas.6.groups.0.1.name",
          "route": "/read/quantum-atoms",
          "kind": "reading"
        }
      ],
      [
        {
          "name": "home-map.areas.6.groups.1.0.name",
          "route": "/numerical-methods-atlas/methods/hartree-fock/",
          "kind": "reading"
        },
        {
          "name": "home-map.areas.6.groups.1.1.name",
          "route": "/numerical-methods-atlas/methods/kohn-sham-dft/",
          "kind": "reading"
        }
      ],
      [
        {
          "name": "home-map.execution.hydrogenic-atoms",
          "route": "/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/",
          "kind": "execution"
        },
        {
          "name": "home-map.execution.helium-ground-state",
          "route": "/numerical-methods-atlas/code-and-data/examples/helium-ground-state/",
          "kind": "execution"
        },
        {
          "name": "home-map.execution.h2-rhf",
          "route": "/numerical-methods-atlas/code-and-data/examples/h2-rhf/",
          "kind": "execution"
        },
        {
          "name": "home-map.execution.periodic-he-dft",
          "route": "/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/",
          "kind": "execution"
        },
        {
          "name": "home-map.execution.periodic-he-forces",
          "route": "/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/",
          "kind": "execution"
        }
      ]
    ]
  },
  {
    "id": "thermostats",
    "name": "home-map.areas.7.name",
    "hint": "home-map.areas.7.hint",
    "question": "home-map.areas.7.question",
    "description": "home-map.areas.7.description",
    "overview": "/read/thermostats",
    "entry": "/read/thermostats",
    "groups": [
      [
        {
          "name": "home-map.areas.7.groups.0.0.name",
          "route": "/read/thermostats",
          "kind": "reading"
        }
      ],
      [
        {
          "name": "home-map.areas.7.groups.1.0.name",
          "route": "/numerical-methods-atlas/methods/nose-hoover/",
          "kind": "planned"
        },
        {
          "name": "home-map.areas.7.groups.1.1.name",
          "route": "/numerical-methods-atlas/methods/stochastic-velocity-rescaling/",
          "kind": "planned"
        }
      ],
      [
        {
          "name": "home-map.areas.7.groups.2.0.name",
          "route": "/read/thermostats",
          "kind": "reading"
        }
      ]
    ]
  }
];
export const homeCopy = {
  "eyebrow": "home-map.eyebrow",
  "title": "home-map.title",
  "title-em": "home-map.title-em",
  "description": "home-map.description",
  "coverage": "home-map.coverage",
  "models": "ui.equation-model-entries.520a2a",
  "methods": "ui.methods-building-blocks.608614",
  "papers": "ui.journal-conference-papers.104ddb",
  "counting": "home-map.counting",
  "equation": "home-map.equation",
  "discretize": "home-map.discretize",
  "solve": "home-map.solve",
  "verify": "home-map.verify",
  "map-title": "home-map.map-title",
  "map-description": "home-map.map-description",
  "map-label": "home-map.map-label",
  "models-label": "home-map.models-label",
  "methods-label": "home-map.methods-label",
  "verify-label": "home-map.verify-label",
  "reading": "home-map.reading",
  "interactive": "home-map.interactive",
  "scope": "home-map.scope",
  "start-area": "home-map.start-area",
  "inspect-scope": "home-map.inspect-scope",
  "selected": "home-map.selected",
  "start-title": "home-map.start-title",
  "start-description": "home-map.start-description",
  "first-tag": "home-map.first-tag",
  "first-title": "home-map.first-title",
  "first-description": "home-map.first-description",
  "first-wave": "home-map.first-wave",
  "first-step": "home-map.first-step",
  "first-read": "home-map.first-read",
  "compare-tag": "home-map.compare-tag",
  "compare-title": "home-map.compare-title",
  "compare-description": "home-map.compare-description",
  "compare-shocks": "home-map.compare-shocks",
  "compare-poisson": "home-map.compare-poisson",
  "compare-time": "home-map.compare-time",
  "sources-tag": "home-map.sources-tag",
  "sources-title": "home-map.sources-title",
  "sources-description": "home-map.sources-description",
  "sources-history": "ui.historical-atlas.a36c4b",
  "sources-bibliography": "home-map.sources-bibliography",
  "sources-books": "home-map.sources-books",
  "evidence-title": "home-map.evidence-title",
  "evidence-description": "home-map.evidence-description",
  "inventory": "home-map.inventory",
  "gallery": "home-map.gallery",
  "glossary": "home-map.glossary",
  "future": "home-map.future",
  "roadmap": "home-map.roadmap",
  "sod-summary": "home-map.sod-summary",
  "sod-description": "home-map.sod-description",
  "execution": "home-map.execution",
  "planned": "home-map.planned",
  "planned-label": "home-map.planned-label",
  "area-reading": "home-map.area-reading",
  "related-exhibits": "home-map.related-exhibits",
  "browse-map": "home-map.browse-map",
  "run-examples": "home-map.run-examples",
  "share-label": "home-map.share-label",
  "primary-actions": "home-map.primary-actions",
  "static-map-note": "home-map.static-map-note",
  "static-directory": "home-map.static-directory",
  "map-eyebrow": "home-map.map-eyebrow"
};
export const homePaths = [
  {
    "tag": "home-map.first-tag",
    "title": "home-map.first-title",
    "description": "home-map.first-description",
    "links": [
      [
        "/equations",
        "home-map.first-wave"
      ],
      [
        "/experiments",
        "home-map.first-step"
      ],
      [
        "/read/accuracy-stability",
        "home-map.first-read"
      ]
    ]
  },
  {
    "tag": "home-map.compare-tag",
    "title": "home-map.compare-title",
    "description": "home-map.compare-description",
    "links": [
      [
        "/reconstruction",
        "home-map.compare-shocks"
      ],
      [
        "/poisson-comparison",
        "home-map.compare-poisson"
      ],
      [
        "/time-integration",
        "home-map.compare-time"
      ]
    ]
  },
  {
    "tag": "home-map.sources-tag",
    "title": "home-map.sources-title",
    "description": "home-map.sources-description",
    "links": [
      [
        "/atlas",
        "ui.historical-atlas.a36c4b"
      ],
      [
        "/references",
        "home-map.sources-bibliography"
      ],
      [
        "/read/textbooks",
        "home-map.sources-books"
      ]
    ]
  }
];
/** Existing reading editions used here; unknown chapters fall back to English. */
export const homeReadingLanguages = {
  "accuracy-stability": [
    "ja",
    "en"
  ],
  "adjoint": [
    "ja",
    "en"
  ],
  "advanced": [
    "ja",
    "en"
  ],
  "advanced-limiters": [
    "ja",
    "en"
  ],
  "ale": [
    "ja",
    "en"
  ],
  "amg": [
    "ja",
    "en"
  ],
  "automatic-differentiation": [
    "ja",
    "en"
  ],
  "basis-functions": [
    "ja",
    "en"
  ],
  "benchmarks": [
    "ja",
    "en"
  ],
  "biological-models": [
    "ja",
    "en"
  ],
  "bratu-inverse": [
    "ja",
    "en"
  ],
  "bratu-multi-inverse": [
    "ja",
    "en"
  ],
  "carbuncle": [
    "ja",
    "en"
  ],
  "chapman-enskog": [
    "ja",
    "en"
  ],
  "chebyshev": [
    "ja",
    "en"
  ],
  "cip": [
    "ja",
    "en"
  ],
  "coordinates-viscosity": [
    "ja",
    "en"
  ],
  "dae": [
    "ja",
    "en"
  ],
  "double-mach": [
    "ja",
    "en"
  ],
  "dsmc": [
    "ja",
    "en"
  ],
  "eigensolvers": [
    "ja",
    "en"
  ],
  "elliptic": [
    "ja",
    "en"
  ],
  "equation-gallery": [
    "ja",
    "en"
  ],
  "ewald": [
    "ja",
    "en"
  ],
  "experiments": [
    "ja",
    "en"
  ],
  "fdtd": [
    "ja",
    "en"
  ],
  "fem": [
    "ja",
    "en"
  ],
  "geophysical-grids": [
    "ja",
    "en"
  ],
  "gravity-boundaries": [
    "ja",
    "en"
  ],
  "gsph": [
    "ja",
    "en"
  ],
  "h2-hf": [
    "ja",
    "en"
  ],
  "history": [
    "ja",
    "en"
  ],
  "hyperbolic-diffusion": [
    "ja",
    "en"
  ],
  "incompressible": [
    "ja",
    "en"
  ],
  "keep": [
    "ja",
    "en"
  ],
  "lattice-boltzmann": [
    "ja",
    "en"
  ],
  "limiters": [
    "ja",
    "en"
  ],
  "low-mach-preconditioning": [
    "ja",
    "en"
  ],
  "mcmc": [
    "ja",
    "en"
  ],
  "meshes": [
    "ja",
    "en"
  ],
  "mhd": [
    "ja",
    "en"
  ],
  "monte-carlo": [
    "ja",
    "en"
  ],
  "movies": [
    "ja",
    "en"
  ],
  "nasa-2d": [
    "ja",
    "en"
  ],
  "optimization": [
    "ja",
    "en"
  ],
  "particle-gravity": [
    "ja",
    "en"
  ],
  "particles-sph": [
    "ja",
    "en"
  ],
  "periodic-dft": [
    "ja",
    "en"
  ],
  "periodic-forces": [
    "ja",
    "en"
  ],
  "pic": [
    "ja",
    "en"
  ],
  "pinn-operators": [
    "ja",
    "en"
  ],
  "pme": [
    "ja",
    "en"
  ],
  "qr-svd": [
    "ja",
    "en"
  ],
  "quadrature": [
    "ja",
    "en"
  ],
  "quantum-atoms": [
    "ja",
    "en"
  ],
  "quantum-chemistry": [
    "ja",
    "en"
  ],
  "radiation-transport": [
    "ja",
    "en"
  ],
  "reconstruction": [
    "ja",
    "en"
  ],
  "reference-solutions": [
    "ja",
    "en"
  ],
  "references": [
    "ja",
    "en"
  ],
  "relativistic-hydrodynamics": [
    "ja",
    "en"
  ],
  "release-notes-v0.1.0": [
    "ja",
    "en"
  ],
  "roadmap": [
    "ja",
    "en"
  ],
  "roe-memorial": [
    "ja",
    "en"
  ],
  "rotated-hybrid": [
    "ja",
    "en"
  ],
  "runge-kutta": [
    "ja",
    "en"
  ],
  "sde": [
    "ja",
    "en"
  ],
  "shock-expansion": [
    "ja",
    "en"
  ],
  "site-coverage": [
    "ja",
    "en"
  ],
  "slab-ewald": [
    "ja",
    "en"
  ],
  "sparse-nonlinear": [
    "ja",
    "en"
  ],
  "splines": [
    "ja",
    "en"
  ],
  "spme": [
    "ja",
    "en"
  ],
  "stability": [
    "ja",
    "en"
  ],
  "steady-runge-kutta": [
    "ja",
    "en"
  ],
  "stiff-integration": [
    "ja",
    "en"
  ],
  "symplectic": [
    "ja",
    "en"
  ],
  "textbooks": [
    "ja",
    "en"
  ],
  "thermostats": [
    "ja",
    "en"
  ],
  "time-integration": [
    "ja",
    "en"
  ],
  "validation-foundations": [
    "ja",
    "en"
  ],
  "validation-mhd": [
    "ja",
    "en"
  ],
  "validation-models": [
    "ja",
    "en"
  ],
  "validation-particles": [
    "ja",
    "en"
  ],
  "validation-thermostats": [
    "ja",
    "en"
  ],
  "wavelets": [
    "ja",
    "en"
  ]
};
