#!/usr/bin/env julia
# Independent plane-wave analytic forces plus re-converged energy differences.
# julia --project=reference-environment reference.jl inputs.json reference-dftk.json [He.gth]
using DFTK, LinearAlgebra, JSON3, SHA, Dates, Pkg
BLAS.set_num_threads(1)
length(ARGS) in (2,3) || error("Expected inputs.json output.json [He.gth]")
input_path,output_path=ARGS[1:2]
pseudo_path=length(ARGS)==3 ? ARGS[3] : joinpath(@__DIR__,"He.gth")
input_text=read(input_path,String)
spec=JSON3.read(input_text,Dict{String,Any})
cell=spec["cell"]
@assert cell["element"]=="He" && cell["charge"]==0 && cell["spin"]==0
positions=[Float64.(p) for p in cell["positions_bohr"]]
@assert length(positions)==2 && all(length(p)==3 for p in positions)
lattice=reduce(hcat,[Float64.(v) for v in cell["lattice_bohr"]])
@assert lattice==5.0Matrix{Float64}(I,3,3)
psp=PspHgh(pseudo_path;identifier="atlas/He-GTH-PADE-q2")
p=cell["pseudopotential"]
@assert psp.Zion==sum(p[1])==2 && psp.rloc==p[2]
@assert p[3]==length(p[4]) && collect(psp.cloc)[1:p[3]]==p[4]
@assert all(iszero,collect(psp.cloc)[p[3]+1:end])
@assert p[5]==0 && psp.lmax==-1 && isempty(psp.h)
functionals=Symbol.(spec["xc"]["libxc"])
@assert functionals==[:lda_x,:lda_c_vwn]
ref=spec["reference"]
cutoffs=Float64.(ref["ecut_hartree"])
@assert length(cutoffs)>=3 && issorted(cutoffs) && all(>(0),diff(cutoffs))
force_target=Float64(ref["force_cutoff_tolerance"])
energy_target=Float64(ref["energy_cutoff_tolerance"])
fd_target=Float64(ref["finite_difference_tolerance"])
@assert all(isfinite,[force_target,energy_target,fd_target]) && min(force_target,energy_target,fd_target)>0
@assert ref["kmeshes"]==[1,2]
versions=Dict(dep.name=>string(dep.version) for dep in values(Pkg.dependencies()) if dep.name in ["DFTK","JSON3","Libxc","Libxc_jll","DftFunctionals"])
records=Any[]; comparisons=Any[];last_changes=Any[];fd_records=Any[]
fd_summary=Dict{String,Any}()
function record_scf(pos,n,cutoff;id="base")
 ks=[Float64.(v) for v in spec["kpoint_meshes"][string(n)]]
 expected=[[x/n,y/n,z/n] for x=0:n-1 for y=0:n-1 for z=0:n-1]
 @assert ks==expected
 weights=fill(1/length(ks),length(ks))
 model=model_DFT(lattice,[ElementPsp(:He,psp) for _ in pos],[lattice\p for p in pos];functionals,n_electrons=4,spin_polarization=:none,temperature=0.,symmetries=false)
 basis=PlaneWaveBasis(model;Ecut=cutoff,kgrid=ExplicitKpoints(ks,weights),use_symmetries_for_kpoint_reduction=false)
 started=time()
 r=self_consistent_field(basis;tol=1e-10,maxiter=100,nbandsalg=FixedBands(n_bands_converge=3,n_bands_compute=6),mixing=SimpleMixing(),damping=.6,seed=1234)
 forces=[collect(f) for f in compute_forces_cart(r)]
 vals=[r.energies.total;reduce(vcat,forces);last(r.history_Δρ)]
 @assert all(isfinite,vals)
 r.converged||error("Independent SCF failed at n=$n cutoff=$cutoff")
 Dict("id"=>id,"positions_bohr"=>pos,"k_n"=>n,"n_kpoints"=>length(ks),"kpoints_fractional"=>ks,"kpoint_weights"=>weights,"ecut_hartree"=>cutoff,"energy_per_cell"=>r.energies.total,"forces_cartesian"=>forces,"net_force_max"=>maximum(abs,reduce(+,forces)),"energy_components"=>Dict(pairs(r.energies)),"converged"=>r.converged,"scf_iterations"=>r.n_iter,"density_residual"=>last(r.history_Δρ),"scf_last_energy_change"=>abs(r.history_Etot[end]-r.history_Etot[end-1]),"electron_count"=>sum(r.ρ)*basis.dvol,"max_orthogonality_error"=>maximum(norm(ψ'ψ-I,Inf) for ψ in r.ψ),"sampled_ks_gap_hartree"=>minimum(e[3] for e in r.eigenvalues)-maximum(e[2] for e in r.eigenvalues),"fft_size"=>collect(basis.fft_size),"plane_wave_counts"=>[length(k.G_vectors) for k in basis.kpoints],"elapsed_seconds"=>time()-started)
end
function save_result()
 envpath=dirname(Base.active_project())
 result=Dict("schema_version"=>1,"engine"=>"DFTK","engine_version"=>string(pkgversion(DFTK)),"julia_version"=>string(VERSION),"package_versions"=>versions,"generated_utc"=>string(now(UTC)),"input_sha256"=>bytes2hex(sha256(input_text)),"script_sha256"=>bytes2hex(sha256(read(@__FILE__))),"pseudopotential_sha256"=>bytes2hex(sha256(read(pseudo_path))),"project_sha256"=>bytes2hex(sha256(read(joinpath(envpath,"Project.toml")))),"manifest_sha256"=>bytes2hex(sha256(read(joinpath(envpath,"Manifest.toml")))),"cell"=>cell,"xc"=>spec["xc"]["libxc"],"energy_unit"=>"hartree/cell","force_unit"=>"hartree/bohr","energy_offset_applied"=>0.,"force_offset_applied"=>0.,"independence"=>"Independent DFTK plane-wave Hamiltonian, SCF, analytic local-pseudopotential and Ewald forces. Libxc XC formulas shared with PySCF; no Gaussian basis or PySCF derivative used.","electrostatics"=>"Native neutral-cell Ewald plus native GTH G=0 correction; no fitted energy or force shifts.","scf"=>Dict("density_tolerance"=>1e-10,"maximum_iterations"=>100,"mixing"=>"SimpleMixing with Anderson fixed-point solver","damping"=>.6,"converged_bands"=>3,"computed_bands"=>6,"random_seed"=>1234),"comparisons"=>comparisons,"cutoff_convergence"=>Dict("force_target_hartree_per_bohr"=>force_target,"energy_target_hartree_per_cell"=>energy_target,"target_reached"=>length(last_changes)==length(ref["kmeshes"])&&all(r["target_reached"] for r in last_changes),"last_changes"=>last_changes,"records"=>records),"finite_difference"=>Dict("method"=>"Fully re-converged central total-energy differences at fixed lattice, cutoff and kmesh; atom indices zero based, Cartesian component indices zero based.","target_hartree_per_bohr"=>fd_target,"records"=>fd_records,"summary"=>fd_summary))
 open(output_path,"w") do io;JSON3.pretty(io,result);println(io);end
end
for n in ref["kmeshes"]
 mesh_records=Any[]
 for cutoff in cutoffs
  record=record_scf(positions,n,cutoff;id="k$n-cutoff$cutoff")
  push!(records,record);push!(mesh_records,record);save_result()
  println("REFERENCE_RECORD ",JSON3.write(record));flush(stdout)
 end
 final=last(mesh_records);previous=mesh_records[end-1]
 fdelta=maximum(abs,reduce(vcat,final["forces_cartesian"])-reduce(vcat,previous["forces_cartesian"]))
 edelta=abs(final["energy_per_cell"]-previous["energy_per_cell"])
 push!(last_changes,Dict("k_n"=>n,"from_ecut_hartree"=>previous["ecut_hartree"],"to_ecut_hartree"=>final["ecut_hartree"],"force_max_change"=>fdelta,"energy_change"=>edelta,"target_reached"=>fdelta<force_target&&edelta<energy_target))
 push!(comparisons,final);save_result()
end
# All six Cartesian components are checked at the smallest registered h.
# One nonzero component also gets an h scan, so agreement at a single h is not enough.
base=only(filter(r->r["k_n"]==1,comparisons))
steps=Float64.(ref["finite_difference_steps_bohr"])
@assert length(steps)>=3 && all(isfinite,steps) && all(>(0),steps) && all(<(0),diff(steps))
for h in steps, iatom in 1:2, component in 1:3
 (h==last(steps)||(iatom==1&&component==1))||continue
 displaced=Any[]
 for sign in [-1,1]
  pos=deepcopy(positions);pos[iatom][component]+=sign*h
  record=record_scf(pos,1,last(cutoffs);id="fd-a$(iatom-1)-c$(component-1)-h$h-sign$sign")
  push!(displaced,record)
 end
 ffd=-(displaced[2]["energy_per_cell"]-displaced[1]["energy_per_cell"])/(2h)
 exact=base["forces_cartesian"][iatom][component]
 push!(fd_records,Dict("atom_index"=>iatom-1,"component"=>component-1,"step_bohr"=>h,"energy_minus"=>displaced[1]["energy_per_cell"],"energy_plus"=>displaced[2]["energy_per_cell"],"analytic_force"=>exact,"central_difference_force"=>ffd,"absolute_error"=>abs(ffd-exact),"scf_converged"=>all(r["converged"] for r in displaced),"max_density_residual"=>maximum(r["density_residual"] for r in displaced),"displaced_records"=>displaced))
 save_result();println("REFERENCE_FD atom=",iatom-1," component=",component-1," h=",h," error=",abs(ffd-exact));flush(stdout)
end
fd_summary["maximum_error"]=maximum(r["absolute_error"] for r in fd_records)
fd_summary["smallest_step_maximum_error"]=maximum(r["absolute_error"] for r in fd_records if r["step_bohr"]==last(steps))
fd_summary["target_reached"]=fd_summary["maximum_error"]<fd_target
save_result()
@assert all(r["target_reached"] for r in last_changes)
@assert fd_summary["target_reached"]
println("REFERENCE_COMPLETE ",output_path)
