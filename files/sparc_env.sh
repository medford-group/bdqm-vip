module purge
module load intel/15.0
module load mkl/11.2
module load mvapich2/2.1
module load git
module load anaconda3/4.2.0

export PATH=/nv/pace-ice/bcomer3/SPARC/SPARC/lib:$PATH
export PYTHONPATH=/nv/pace-ice/bcomer3/ase/ase-ase-3.18.1:$PYTHONPATH
export PATH=/nv/pace-ice/bcomer3/ase/ase-ase-3.18.1/bin:$PATH
export PYTHONPATH=/nv/pace-ice/bcomer3/sparc-ase/pysparcx/:$PYTHONPATH
export SPARC_PSP_PATH=/nv/pace-ice/bcomer3/sparc_psps/PBE_psp_cut


if [[ -z "${PBS_NP}" ]]; then
  export ASE_SPARC_COMMAND="/nv/pace-ice/bcomer3/SPARC/SPARC/lib/sparc -name PREFIX > log"
else
  export ASE_SPARC_COMMAND="mpirun -np $PBS_NP /nv/pace-ice/bcomer3/SPARC/SPARC/lib/sparc -name PREFIX > log"
fi
