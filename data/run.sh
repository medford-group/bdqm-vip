#!/bin/bash
#PBS -l nodes=1:ppn=2
#PBS -l pmem=1GB
#PBS -l walltime=1:00:00
#PBS -q pace-ice
#PBS -N optimizer
#PBS -o stdout
#PBS -e stderr

cd $PBS_O_WORKDIR

source ~/.bashrc

conda activate amptorch

python final.py
~                     
