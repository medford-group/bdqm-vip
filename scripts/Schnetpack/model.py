import os
import torch.nn.functional as F

import logging
from torch.optim import Adam
import schnetpack as spk
from schnetpack.train import Trainer, CSVHook, ReduceLROnPlateauHook, TensorboardHook
from schnetpack.train.metrics import MeanAbsoluteError, RootMeanSquaredError
#from schnetpack.metrics import build_mse_loss
from schnetpack.train.metrics import MeanSquaredError
from schnetpack.data import AtomsData
import schnetpack.atomistic as atm
import schnetpack.representation as rep

#mse_loss = MeanSquaredError()
mse_loss = spk.train.loss.build_mse_loss

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


# basic settings
model_dir = "psi4_model"  # directory that will be created for storing model
#os.makedirs(model_dir)
properties = ["energy", "forces"]  # properties used for training

# data preparation
logging.info("get dataset")
dataset = AtomsData("psi4.db", 
                    available_properties=properties,
                    #required_properties=properties,
                    collect_triples=True)

train, val, test = spk.train_test_split(
    data=dataset,
    num_train=200,
    num_val=20,
    split_file=os.path.join(model_dir, "split.npz"),
)
train_loader = spk.AtomsLoader(train, batch_size=50)
val_loader = spk.AtomsLoader(val, batch_size=5)

# get statistics
#atomrefs = dataset.get_atomrefs(properties)
per_atom = dict(energy=True, forces=False)
means, stddevs = train_loader.get_statistics(
    properties, 
    #atomrefs=atomrefs, 
    #per_atom=per_atom
)

# model build
logging.info("build model")
#representation = spk.SchNet(n_interactions=6)
#representation = spk.representation.SymmetryFunctions(elements={6})
"""
output_modules = [
    spk.Atomwise(
        property="energy",
        derivative="forces",
        mean=means["energy"],
        stddev=stddevs["energy"],
        negative_dr=True,
    )
]
"""
reps = rep.BehlerSFBlock(elements={13},
                         n_radial = 22,
                         n_angular = 8,
                         cutoff_radius = 8,
                         crossterms = True,
                         zetas = {1,4},
                         
                         )
output = spk.atomistic.output_modules.ElementalAtomwise(reps.n_symfuncs,
                                              n_layers=2,
                                              n_hidden=24,
                                              property = 'energy',
                                              derivative = 'forces',
                                              mean=means["energy"],
                                              stddev=stddevs["energy"],
                                              )


#output = spk.output_modules.Atomwise(reps.n_symfuncs)
model = atm.AtomisticModel(reps, output)
#model = spk.AtomisticModel(representation, output_modules)

# build optimizer
optimizer = Adam(params=model.parameters(), lr=1e-4)

# hooks
logging.info("build trainer")
metrics = [MeanAbsoluteError(p, p) for p in properties] + \
          [RootMeanSquaredError(p, p) for p in properties]
hooks = [CSVHook(log_path=model_dir, metrics=metrics), 
        ReduceLROnPlateauHook(optimizer), 
        TensorboardHook(log_path=model_dir,
        metrics=metrics)]

# trainer
#loss = lambda b, p: F.mse_loss(p["y"], b['energy','force'])
loss = mse_loss(properties)


trainer = Trainer(
    model_dir,
    model=model,
    hooks=hooks,
    loss_fn=loss,
    optimizer=optimizer,
    train_loader=train_loader,
    validation_loader=val_loader,
    #device = 'cuda'
)

# run training

logging.info("training")
trainer.train(device="cpu", n_epochs=10000)
