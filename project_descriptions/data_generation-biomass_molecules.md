# Data Generation - Adsorption Energies of Biomass Molecules on Metal Surfaces

Advisor: Chaoyi Chang

Sugars and sugar alcohols are industrially important as precursors to a variety of fine chemicals, and sorbitol (a type of sugar alcohol) is identified as one of the top 10 biorefinery products by the DOE. In this project, you will to calculate the adsorption energy of some important sugars and sugar derivatives like glucose, ethyrose, glycerol, and sorbitol on different transition-metal slabs to understand the binding energy and geometry of these compounds on each surface. This will help in the development of biomass catalysts.

In this project you will compute the adsorption energies of the following molecules/substructures on Pt (111) surfaces. You should try at least 2 different initial guesses for the binding geometry of each molecule and 1 initial structure for substructures on Pt surface. You will use the ASE package in python to build the structures and Quantum Espresso is used for the DFT calculation. You can also practice coding by scripting Python to build structures, re-submit jobs, and organize/analyze data.

Molecules to compute: erythrose

Substructures to compute: erythrose with 1 chemical bond breaking (C-H, C-O, C=O, O-H and C-C, 14 reactions in total)

You should use the following parameters for the DFT calculation:

* xc = 'BEEF-vdW'
* kpts = (6,6,1)
* pw = 400
* dw=4000

## Midterm Goal:

Get optimized structures for both erythrose and its substructures, and make sure no other bonds break during the optimization process.


### Midterm Deliverables:
A spreadsheet containing the current optimization configurations/energies/convergence for at least 7 molecules/substructures, along with the paths where the calculations were performed on PACE. A template will be provided.

## Final Goal:

Complete the DFT calculations for all molecules/substructures.

### Final Deliverables:
Updated spreadsheet including energies for all molecules/substructures on the Pt (111) surface in all configurations.
