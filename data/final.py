import matplotlib.pyplot as plt
import numpy as np
import sys
import torch
from ase import Atoms
import ase.io
from ase.calculators.emt import EMT
from ase.build import molecule


from amptorch.ase_utils import AMPtorch
from amptorch.trainer import AtomsTrainer

# get training images by reading trajectory files

# read all images from the trajectory
training = ase.io.read("./training_data.traj", index=":")

# read every 10th image from the trajectory
# training = ase.io.read("./data/water_2d.traj", index="::10")

# define sigmas
nsigmas = 10
sigmas = np.linspace(0, 2.0,nsigmas+1,endpoint=True)[1:]

# define MCSH orders
MCSHs_index = 2
MCSHs_dict = {
0: { "orders": [0], "sigmas": sigmas,},
1: { "orders": [0,1], "sigmas": sigmas,},
2: { "orders": [0,1,2], "sigmas": sigmas,},
3: { "orders": [0,1,2,3], "sigmas": sigmas,},
4: { "orders": [0,1,2,3,4], "sigmas": sigmas,},
5: { "orders": [0,1,2,3,4,5], "sigmas": sigmas,},
6: { "orders": [0,1,2,3,4,5,6], "sigmas": sigmas,},
7: { "orders": [0,1,2,3,4,5,6,7], "sigmas": sigmas,},
8: { "orders": [0,1,2,3,4,5,6,7,8], "sigmas": sigmas,},
9: { "orders": [0,1,2,3,4,5,6,7,8,9], "sigmas": sigmas,},
}
MCSHs = MCSHs_dict[MCSHs_index] # MCSHs is now just the order of MCSHs. 


GMP = {
    "MCSHs": MCSHs,
    "atom_gaussians": {
        "H": "/home/lucas/local_data/pseudo/H_pseudodensity_2.g",
        "O": "/home/lucas/local_data/pseudo/O_pseudodensity_4.g",
    },
    "cutoff": 12.0,
    "solid_harmonics": True,
}

elements = ["H", "O"]

config = {
    "model": {
        "name":"singlenn",
        "get_forces": True,
        "num_layers": 3,
        "num_nodes": 10,
        "batchnorm": True,
        "activation":torch.nn.Tanh,
    },
    "optim": {
        "force_coefficient": 0.01,
        "lr": 1e-3,
        "batch_size": 16,
        "epochs": 500,
        "loss": "mse",
        "metric": "mae",
    },
    "dataset": {
        "raw_data": training,
        "fp_scheme": "gmpordernorm",
        "fp_params": GMP,
        "elements": elements,
        "save_fps": True,
        "scaling": {"type": "normalize", "range": (0, 1)},
        "val_split": 0.1,
    },
    "cmd": {
        "debug": False,
        "run_dir": "./",
        "seed": 1,
        "identifier": "test",
        "verbose": True,
        # Weights and Biases used for logging - an account(free) is required
        "logger": False,
    },
}

torch.set_num_threads(1)
trainer = AtomsTrainer(config)

with open("trained_nn.txt", "w") as f:
    sys.stdout = f
    trainer.train()

# testing NN on other dataset

#predictions = trainer.predict(training)

testing = ase.io.read("./validation_data.traj", index=":")
predictions = trainer.predict(testing)

true_energies = np.array([image.get_potential_energy() for image in testing])
pred_energies = np.array(predictions["energy"])

with open("testing.txt", "w") as f:
    f.write(f"Energy MSE: {np.mean((true_energies - pred_energies) ** 2)}\n")
    f.write(f"Energy MAE: {np.mean(np.abs(true_energies - pred_energies))}\n")
    training[0].set_calculator(AMPtorch(trainer))
    f.write(f"Potential energy: {training[0].get_potential_energy()}")
