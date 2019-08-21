from ase.build import molecule
from ase.calculators.vasp.vasp2 import Vasp2

atoms = molecule('H2O')
atoms.set_cell([10,10,10])
atoms.center()

calc = Vasp2(
             atoms = atoms,
             encut = 350, # the planewave cutoff, (the basis set size)
             xc = 'PBE', # the exchange correlation functional
             ibrion = 1, # flag to relax the atoms
             kpts = (1,1,1) # k-point grid
             )

atoms.set_calculator(calc)

energy = atoms.get_potential_energy()
print(energy)
