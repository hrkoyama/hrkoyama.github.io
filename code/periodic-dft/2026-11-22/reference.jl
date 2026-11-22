#!/usr/bin/env julia
# Independent plane-wave reference. Run in the pinned Project/Manifest environment.
# julia --project=reference-environment reference.jl inputs.json reference.json [He.gth]
using DFTK, LinearAlgebra, JSON3, SHA, Dates, Pkg
BLAS.set_num_threads(1)
length(ARGS) in (2,3) || error("Expected inputs.json output.json [He.gth]")
input_path, output_path = ARGS[1:2]
pseudo_path = length(ARGS) == 3 ? ARGS[3] : joinpath(@__DIR__, "He.gth")
input_text = read(input_path, String)
spec = JSON3.read(input_text, Dict{String,Any})
cell = spec["cell"]
# This small reference deliberately accepts only the audited local He potential.
cell["element"] == "He" || error("The audited reference requires He")
cell["charge"] == 0 && cell["spin"] == 0 || error("Neutral spin-restricted model required")
p = cell["pseudopotential"]
psp = PspHgh(pseudo_path; identifier="atlas/He-GTH-PADE-q2")
@assert psp.Zion == sum(p[1]) == 2
@assert psp.rloc == p[2] && p[3] == length(p[4])
@assert collect(psp.cloc)[1:p[3]] == p[4]
@assert all(iszero, collect(psp.cloc)[p[3]+1:end])
@assert p[5] == 0 && psp.lmax == -1 && isempty(psp.h)
functionals = Symbol.(spec["xc"]["libxc"])
@assert functionals == [:lda_x, :lda_c_vwn]
# Input lists lattice vectors as rows (PySCF convention); DFTK uses columns.
lattice = reduce(hcat, [Float64.(v) for v in cell["lattice_bohr"]])
position = lattice \ Float64.(cell["position_bohr"])
model = model_DFT(lattice, [ElementPsp(:He, psp)], [position];
                  functionals, n_electrons=2, spin_polarization=:none,
                  temperature=0.0, symmetries=false)
versions = Dict(dep.name => string(dep.version) for dep in values(Pkg.dependencies())
                if dep.name in ["DFTK", "JSON3", "Libxc", "Libxc_jll", "DftFunctionals"])
records = Any[]
previous_records = Any[]
if isfile(output_path) && get(ENV, "ATLAS_REFERENCE_RESUME", "0") == "1"
    previous = JSON3.read(read(output_path,String),Dict{String,Any})
    @assert previous["engine_version"] == string(pkgversion(DFTK))
    @assert previous["cell"] == cell
    @assert previous["xc"] == spec["xc"]["libxc"]
    @assert previous["pseudopotential_sha256"] == bytes2hex(sha256(read(pseudo_path)))
    append!(previous_records,previous["cutoff_convergence"]["records"])
end
comparisons = Any[]
last_changes = Any[]
cutoff_target = 1e-4 # Eh/cell. Never apply a fitted energy shift.
function save_result()
    envpath = dirname(Base.active_project())
    result = Dict(
        "schema_version"=>1,
        "engine"=>"DFTK", "engine_version"=>string(pkgversion(DFTK)),
        "julia_version"=>string(VERSION), "package_versions"=>versions,
        "generated_utc"=>string(now(UTC)),
        "input_sha256"=>bytes2hex(sha256(input_text)),
        "script_sha256"=>bytes2hex(sha256(read(@__FILE__))),
        "pseudopotential_sha256"=>bytes2hex(sha256(read(pseudo_path))),
        "project_sha256"=>bytes2hex(sha256(read(joinpath(envpath,"Project.toml")))),
        "manifest_sha256"=>bytes2hex(sha256(read(joinpath(envpath,"Manifest.toml")))),
        "cell"=>cell, "xc"=>spec["xc"]["libxc"],
        "energy_unit"=>"hartree/cell", "energy_offset_applied"=>0.0,
        "independence"=>"Independent DFTK plane-wave Hamiltonian, SCF and Ewald implementation; Libxc XC formulas shared with PySCF.",
        "electrostatics"=>"Native neutral-cell Ewald plus native GTH pseudopotential G=0 correction; no fitted energy shift.",
        "scf"=>Dict("density_tolerance"=>1e-9,"maximum_iterations"=>100,
                     "mixing"=>"SimpleMixing with Anderson fixed-point solver","damping"=>0.6,
                     "converged_bands"=>2,"computed_bands"=>5,"random_seed"=>1234),
        "comparisons"=>comparisons,
        "cutoff_convergence"=>Dict("target_hartree_per_cell"=>cutoff_target,
            "target_reached"=>length(last_changes)==length(spec["reference"]["kmeshes"]) && all(r["target_reached"] for r in last_changes),
            "last_changes"=>last_changes,"records"=>records))
    open(output_path,"w") do io
        JSON3.pretty(io,result); println(io)
    end
end
for n in spec["reference"]["kmeshes"]
    ks = [Float64.(v) for v in spec["kpoint_meshes"][string(n)]]
    weights = fill(1.0 / length(ks), length(ks))
    mesh_records = Any[]
    for cutoff in spec["reference"]["ecut_hartree"]
        existing = findfirst(r -> r["k_n"] == n && r["ecut_hartree"] == cutoff &&
            r["kpoints_fractional"] == ks, previous_records)
        if !isnothing(existing)
            record = previous_records[existing]
            push!(records,record); push!(mesh_records,record)
            println("REUSED_REFERENCE kmesh=",n," cutoff=",cutoff); flush(stdout)
            continue
        end
        basis = PlaneWaveBasis(model; Ecut=Float64(cutoff),
            kgrid=ExplicitKpoints(ks,weights), use_symmetries_for_kpoint_reduction=false)
        started = time()
        r = self_consistent_field(basis; tol=1e-9, maxiter=100,
            nbandsalg=FixedBands(n_bands_converge=2,n_bands_compute=5),
            mixing=SimpleMixing(), damping=0.6, seed=1234)
        occupied_max = maximum(e[1] for e in r.eigenvalues)
        unoccupied_min = minimum(e[2] for e in r.eigenvalues)
        record = Dict("k_n"=>n,"n_kpoints"=>length(ks),
            "kpoints_fractional"=>ks,"kpoint_weights"=>weights,
            "ecut_hartree"=>cutoff,"energy_per_cell"=>r.energies.total,
            "energy_components"=>Dict(pairs(r.energies)),
            "converged"=>r.converged,"scf_iterations"=>r.n_iter,
            "density_residual"=>last(r.history_Δρ),
            "scf_last_energy_change"=>abs(r.history_Etot[end]-r.history_Etot[end-1]),
            "electron_count"=>sum(r.ρ)*basis.dvol,
            "max_orthogonality_error"=>maximum(norm(ψ'ψ-I,Inf) for ψ in r.ψ),
            "sampled_ks_gap_hartree"=>unoccupied_min-occupied_max,
            "eigenvalues_hartree"=>r.eigenvalues,
            "fft_size"=>collect(basis.fft_size),
            "plane_wave_counts"=>[length(k.G_vectors) for k in basis.kpoints],
            "elapsed_seconds"=>time()-started)
        r.converged || error("Independent SCF failed at kmesh=$n Ecut=$cutoff")
        push!(records,record); push!(mesh_records,record)
        save_result()
        println("REFERENCE_RECORD ", JSON3.write(record)); flush(stdout)
    end
    final = last(mesh_records)
    push!(comparisons,Dict("k_n"=>n,"kpoints_fractional"=>ks,
        "kpoint_weights"=>weights,"ecut_hartree"=>final["ecut_hartree"],
        "energy_per_cell"=>final["energy_per_cell"],
        "sampled_ks_gap_hartree"=>final["sampled_ks_gap_hartree"]))
    change = abs(mesh_records[end]["energy_per_cell"] - mesh_records[end-1]["energy_per_cell"])
    push!(last_changes,Dict("k_n"=>n,"from_ecut_hartree"=>mesh_records[end-1]["ecut_hartree"],
        "to_ecut_hartree"=>final["ecut_hartree"],"energy_change"=>change,
        "target_reached"=>change<cutoff_target))
    save_result()
end
println("REFERENCE_COMPLETE ", output_path)
