# Machine Learning - Hyperparameter optimization

In this project you will work with a dataset of water molecules interacting with an iron surface in a constant temperature molecular dynamics simulation.  You will be provided with a dataset of 842 images that can be used for training the model, and an additional 200 images for validating the performance.

Prior work in the group has achieved neural network force fields with an accuracy of 4 meV/atom (energy) and 0.23 eV/A (forces) for the dataset provided. Your goal in this project is to improve this result by modifying the neural network architecture (number of layers/nodes, activiation function, etc.) and/or initialization and training procedure. It is recommended that you utilize the Simple-NN package, but you may also use any other software package, or implement/modify algorithms as needed.

the data is located in the `data` folder in the top level of this github repository named `iron_data.traj` and `iron_validation.traj`

There are many options for software to train these neural networks. Some commonly-used options are [Simple\_NN](https://github.com/medford-group/SIMPLE-NN.git) and [Schnetpack](https://github.com/atomistic-machine-learning/schnetpack). These are both academic software packages, and as such are hard to use. However, an example directory for running each can be found in the `scripts` folder in this repository. Our group is also working to develop a new PyTorch-based version of the AMP software package. An alpha version is available [via Github](https://github.com/ulissigroup/amptorch). You may wish to try this as well.

A paper by Behler explaining how this style of neural network force field works is below in the "Relevant Literature" section

## Midterm goal:

By the midterm you should be able to generate a neural network model with accuracy comparable to the accuracy already achieved in the group (see above).

### Midterm deliverables:

A zip file with the results including a log file with the RMSE values and input files.

## Final goal:

By the final you should have a neural network model and/or training strategy that has an improved accuracy for both energies and forces.

### Final deliverables:

A zip file with all model details as described in the midterm deliverable, along with a report explaining your strategy and the reasoning behind the improved performance.

## Relevant Literature
https://onlinelibrary.wiley.com/doi/full/10.1002/qua.24890 https://www.sciencedirect.com/science/article/pii/S0010465519301298

https://www.sciencedirect.com/science/article/pii/S0927025617307206
