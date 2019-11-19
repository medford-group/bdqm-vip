# Big Data and Quantum Mechanics Traning Project

This project covers basic training for 1) generating data using quantum-mechanical simulations based on density functional theory (DFT) and 2) using machine learning to create models that predict the outcome of these simulations based on large datasets.


## Midterm Goal:
Compute the adsorption energy of carbon monoxide (CO) on a Pt(111) surface using DFT on the PACE computing cluster. You will use grid sizes (`h`) of 0.2, 0.15, and 0.12 A and a k-point mesh of (4,4,1) to compute the adsorption energy.

Be sure to perform the calculations on a 2x2 slab of Pt(111) with 4 layers. Also be sure to constrain the bottom 2 layers. Be aware that using different adsorbtion sites will give different answers, please use the `hcp` site in the `add_adsorbate` command. There are links below to the relevant documentation pages you will likely need.
https://wiki.fysik.dtu.dk/ase/ase/build/surface.html

https://wiki.fysik.dtu.dk/ase/ase/constraints.html#module-ase.constraints

https://wiki.fysik.dtu.dk/ase/ase/build/build.html?


### Midterm Deliverables:
* A text file containing the computed adsorption energies and the path to the directory of the DFT calculation on the PACE cluster (be sure to change permissions) and/or a .zip file containing all relevant inputs and outputs for the calculatoin.

## Final Goal:
Train a neural-network model to predict the energies and forces of 0.05 eV/A

### Final Deliverables:
* A zip/tar archive containing your trained force field and the DFT calculations used to generate it.
