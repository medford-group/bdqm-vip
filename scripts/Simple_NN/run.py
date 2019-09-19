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


    
model = Simple_nn('input.yaml', 
                   descriptor=Symmetry_function(inputs = dict(refdata_format='traj')), 
                   model=Neural_network())
model.run()
