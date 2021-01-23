# Data Generation/Infrastructure - Nitrogen Reactivity of p-Block Dopants on Oxides and SPARC interface development
Advisor: Jagriti Sahoo

Photocatalytic nitrogen fixation is an interesting new reaction that has the potential to create fertilizers from air. Research in the Medford group has explored many aspects of this reaction, and it was recently discovered that carbon impurities on titania (TiO<sub>2</sub>) may be the key to enabling the reaction. However, the role of other p-block elements has not been explored. One important factor in enabling this reaction is the relative reactivity between molecular nitrogen (N<sub>2</sub>) and molecular oxygen (O<sub>2</sub>), both of which are present in air. Surfaces that are preferentially reactive toward N2 are particularly promising for photocatalytic nitrogen fixation.

## Project Description:

This project will have two sub-teams:

The first sub-team will focus on computing the adsorption energies of N<sub>2</sub> and O<sub>2</sub> molecules on TiO<sub>2</sub> surfaces that have p-block elements substituted for surface oxygen. You will compute the adsorption energies of these two molecules with the following elements substituted for the surface oxygen: B, C, N, F, Si, P, S, Cl, Se, Br. For each surface you will compare the ratio of the adsorption energies to identify promising materials. The team will use the existing infrastructure (Quantum Espresso) for these calculations. 

The second sub-team will focus on transitioning to SPARC instructure. SPARC (Simulation Package for Ab-initio Real-space Calculations) is an open-source software package for DFT calculations using finite-difference code. This project will involve benchmarking SPARC versus Quantum Espresso for accuracy and testing/developing the SPARC Python interface for making it more efficient. 

## Midterm Goal:

1. For project 1, the sub-team should complete DFT calculations for N<sub>2</sub> and O<sub>2</sub> adsorbed with the following elements substituted for the surface oxygen:

* B, C, N, F

2. For project 2, the sub-team should start with running DFT calculations using SPARC for the above systems and benchmark for accuracy. 



### Midterm Deliverables:
A spreadsheet containing adsorption energies for N<sub>2</sub> and O<sub>2</sub> on each surface, along with a zip/tar archive containing the actual calculations. A template for the spreadsheet will be provided.

## Final Goal:

Complete the DFT calculations for N<sub>2</sub> and O<sub>2</sub> on with all p-block substitutions.

### Final Deliverables:
Updated spreadsheet including energies for N<sub>2</sub> and O<sub>2</sub> on all surfaces and a zip/tar archive containing the actual calculations.

### Relevant Literature:
https://pubs.acs.org/doi/pdf/10.1021/acssuschemeng.7b03652
https://pubs.acs.org/doi/10.1021/jacs.8b08464
https://link.springer.com/content/pdf/10.1007/s10562-020-03348-z.pdf
