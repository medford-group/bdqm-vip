# DFT Infrastructure- SPARC python interface development
Advisors: Phanish Suryanarayana and Jagriti Sahoo

## Introduction 

Simulations Package for Ab-inito Real Space Calculations or SPARC is an open source computational framework that can be utilized to perform Density Functional Theory (DFT) for chemical systems such as molecules, periodic bulk crystals, extended slabs, nanoparticles etc. It is a finite-difference code where the walltime decreases linearly with the number of cores used, enabling very fast calculations. It can be used for applications in the field of heterogeneous catalysis such as elucidation of reaction mechanism on catalytic processes. The sparc-dft-api is an Atomic Simulations Environment (ASE) based python wrapper for SPARC and is compatible with Python3. 

## Project Description

The team will focus on transitioning to SPARC infrastructure. This will involve improving the sparc-dft-api to make it more efficient for DFT calculations. The sparc-dft-api can be accessed using the following link:
https://github.com/SPARC-X/sparc-dft-api

Running the SPARC code requires two input files, **.inpt** file with the appropriate DFT settings and **.ion** file with atomic positions and constraints on the atoms of a given system. Currently, the SPARC python interface has multiple utilities but it is still in its development phase, hence there is a lot of scope for improvement. The goal of this project is to understand the utilities offered by the python interface and develop it further such that it works efficiently with ASE Atoms objects. By the end of this semester, we plan to develop the interface such that it supports different input file formats (translating constraints from POSCAR or .traj files to .inpt and .ion file formats) and add utilities that will facilitate visualization of relaxed trajectories of systems. 

## Midterm Goals

By midterm, you are expected to understand the utilities offered by the SPARC python interface and benchmark some simple DFT calculations for SPARC and compare them with Quantum Espresso. You should be able to construct an ASE atoms object, attach it to the SPARC calculator and perform a relaxation calculation for adsorption of CO(molecule) on Platinum (111) slab system, understand the SPARC input files: .inpt and .ion, the output files: .geopt and .out files. If this is achieved prior to the midterm, you can start figuring out how to improve some functionalities of the python interface. Some utilities to consider are:

* Appending .ion file to .geopt file and constructing a .traj object (final trajectory file). If you run a relaxation calculation in Quantum Espresso, it generates a .traj file that can be visualized using the ASE GUI. We need a similar functionality in SPARC that supports easier analysis of results from a DFT calculation. 

* A converter from POSCAR to **.ion** format to ensure that the constraints are properly translated. 

### Midterm Deliverables

Submit a zip file with results for DFT calculations from SPARC and Quantum Espresso with input and output files and a report on analysis of different utilities offered by the SPARC python interface. 

## Final Goal

By the final, you are expected to add the utilities mentioned in the midterm goals to the SPARC python interface. 

### Final Deliverables

Push the changes to the sparc-dft-api GitHub repository and submit a report with details of your strategy on improving the functionality of the Python interface. 

## References

To learn more about SPARC, please refer to the following paper:

* Xu, Q., Sharma, A., Comer, B., Huang, H., Chow, E., Medford, A. J., ... & Suryanarayana, P. (2021). SPARC: Simulation package for ab-initio real-space calculations. SoftwareX, 15, 100709. (https://www.sciencedirect.com/science/article/pii/S2352711021000546)
