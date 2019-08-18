#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=1:00:00
#PBS -q iw-shared-6
#PBS -N environ_test
#PBS -o stdout
#PBS -e stderr
cd $PBS_O_WORKDIR

source /gpfs/pace1/project/chbe-medford/medford-share/envs/VASP_envs/VASP_ase3.18
python vasp_demo.py
