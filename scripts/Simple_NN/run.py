"""
Run the code below:
    python run.py

run.py:
"""

from simple_nn import Simple_nn
from simple_nn.features.symmetry_function import Symmetry_function
from simple_nn.models.neural_network import Neural_network
import numpy as np
from ase.io import read
import os
import time
from lammps_interface.tools import make_params_file


files = ['H','O']
dist_dict = {'H':0.5,'Pt':1.5,'O':1.0}


etas = np.append(np.linspace(0.0001, 4, 10), np.logspace(-4,1,10))
rs_s = [0] * 20

#make_params_file(files, etas, rs_s, dist_dict, n_g4_eta = 10)

atoms = read('8.traj', index = '-1')
    
model = Simple_nn('input.yaml', 
                   descriptor=Symmetry_function(inputs = dict(refdata_format='traj')), 
                   model=Neural_network())
model.run()
