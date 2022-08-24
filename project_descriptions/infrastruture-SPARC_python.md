# DFT Infrastructure- SPARC python interface development
Advisors: Jagriti Sahoo and Phanish Suryanarayana 

## Introduction 

Simulations Package for Ab-inito Real Space Calculations or SPARC is an open source computational framework that can be utilized to perform Density Functional Theory (DFT) for chemical systems such as molecules, periodic bulk crystals, extended slabs, nanoparticles etc. It is a finite-difference code written in C where the walltime decreases linearly with the number of cores used, enabling very fast calculations. It can be used for applications in the field of heterogeneous catalysis such as elucidation of reaction mechanism on catalytic processes. The sparc-dft-api is an Atomic Simulations Environment (ASE) based python wrapper for SPARC and is compatible with Python3. 

## Project Description

Rather than having to run a C executable for every DFT calculation, it is easier to write a python script that communicates with the C code to tell it what calculations to perform. There are a few ways in which communication could be carried out - either python bindings to specific C functions or through a server-client architecture where the client is a python script that can dynamically make requests of a server which is running the DFT calcualtions. This second style allows for a more dynamic workflow. 

For this semester, we want to improve upon the existing infrastructure that was developed by students in the VIP team in previous semesters. We want to connect the server-client architecture to SPARC backend. The goal of this project is to understand the utilities offered by the python interface and the server-client architecture set up by the students in previous semesters. Link for the code can be found here: https://github.com/adinhobl/sparc-dft-api/tree/socket

## Midterm Goals

By midterm, you are expected to understand the utilities offered by the SPARC python interface and the how the current architecture works. You are expected to run the current implementation and work on the extension such that the python interface can use i-Pi protocol to connect to SPARC backend.
 

## Final Deliverables

Push the changes to the sparc-dft-api GitHub repository and submit a report with details of your strategy on improving the functionality of the Python interface. 

## References

To learn more about SPARC, please refer to the following paper:

* Xu, Q., Sharma, A., Comer, B., Huang, H., Chow, E., Medford, A. J., ... & Suryanarayana, P. (2021). SPARC: Simulation package for ab-initio real-space calculations. SoftwareX, 15, 100709. (https://www.sciencedirect.com/science/article/pii/S2352711021000546)
