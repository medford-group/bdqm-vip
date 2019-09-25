module purge
module load intel/15.0
module load mkl/11.2
module load mvapich2/2.1
module load git
module load anaconda3/4.2.0

export PATH=/gpfs/pace1/project/chbe-medford/medford-share/builds/sparc/dev_new_inputs/SPARC/lib/:$PATH
export PYTHONPATH=/gpfs/pace1/project/chbe-medford/medford-share/gits/frozen/ase_3.18.0b1/ase:$PATH
export PATH=/gpfs/pace1/project/chbe-medford/medford-share/gits/frozen/ase_3.18.0b1/ase/bin:$PATH
export PYTHONPATH=/gpfs/pace1/project/chbe-medford/medford-share/gits/dev/ase-sparc/rewrite/pysparcx/:$PYTHONPATH
export SPARC_PSP_PATH=/gpfs/pace1/project/chbe-medford/medford-share/data/pseudos/oncv_2015/PBE_psp_cut


if [[ -z "${PBS_NP}" ]]; then
  export ASE_SPARC_COMMAND="/gpfs/pace1/project/chbe-medford/medford-share/builds/sparc/dev_new_inputs/SPARC/lib/sparc -name PREFIX > log"
else
  export ASE_SPARC_COMMAND="mpirun -np $PBS_NP /gpfs/pace1/project/chbe-medford/medford-share/builds/sparc/dev_new_inputs/SPARC/lib/sparc -name PREFIX > log"
fi
