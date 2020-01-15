# Big Data and Quantum Mechanics Traning Project

This project covers basic training for 1) generating data using quantum-mechanical simulations based on density functional theory (DFT) and 2) using machine learning to create models that predict the outcome of these simulations based on large datasets.


## Midterm Goal:
Compute the reaction energy of 2H2O -> 2H2 + O2 using DFT on the PACE computing cluster. You will use the SPARC code with grid spacings (`h`) of 0.2, 0.16, 0.14, and 0.12 A and a k-point mesh of (1,1,1) to compute the adsorption energy. Be sure that you remember to "relax" the structures to find the optimal geometry of each molecule.


### Midterm Deliverables:
* A text file or spreadsheet containing the computed total energies and reaction energies at each grid spacing, and the path to the directory of the DFT calculation on the PACE cluster (be sure to change permissions).
* A .zip file containing all relevant inputs and outputs for the calculatoin.

## Final Goal:
Train a neural-network model to predict the energies and forces of 0.05 eV/Angstrom on the water data provided in `data/training_data.traj`. You can use the [AMP package](https://amp.readthedocs.io/en/latest/) to complete this task.

### Final Deliverables:
* A zip/tar archive containing your trained force field and the training data used to generate it.
* A script showing that you have tested the trained force field on a "test" set not used for training.
