# Machine Learning - Latent Spaces for Iron/Water Interfaces
Advisor: AJ Medford

In this project you will work with a dataset of water molecules interacting with an iron surface in a constant temperature molecular dynamics simulation.  The dataset contains 1042 images and energies. Your goal is to use machine-learning techniques to create and analyze various latent-space representations of these structures.

Prior work in the group has achieved neural network force fields with an accuracy of 4 meV/atom (energy) and 0.23 eV/A (forces) for the dataset provided. Your goal in this project is to (1) analyze the latent space of existing models to understand the features that the neural network is learning and (2) explore new techniques for establishing better latent-space descriptions. You may wish to use the [ElectroLens](https://github.com/ray38/ElectroLens) tool developed by the group to analyze the data.

the data is located in the `data` folder in the top level of this github repository named `iron_data.traj` and `iron_validation.traj`

There are many options for software to train these neural networks. Some commonly-used options are [Simple\_NN](https://github.com/medford-group/SIMPLE-NN.git) and [Schnetpack](https://github.com/atomistic-machine-learning/schnetpack). These are both academic software packages, and as such are hard to use. However, an example directory for running each can be found in the `scripts` folder in this repository. Our group is also working to develop a new PyTorch-based version of the AMP software package. An alpha version is available [via Github](https://github.com/ulissigroup/amptorch). You may wish to try this as well, particularly if you want to integrate new neural net architectures such as auto-encoders.

A paper by Behler explaining how this style of neural network force field works is below in the "Relevant Literature" section

## Midterm goal:

Utilize existing scripts to train a neural network and extract the latent-space variables. Use dimensional reduction and/or visualization techniques to connect the latent space(s) to the atomic structures.

### Midterm deliverables:

* Script for traning a neural network.
* Script for extracting latent space representations from trained neural network.
* Script and/or plots/screenshots visualizing the latent space representation for a subset of images.

## Final goal:

Explore different neural network architectures and identify the architecture and layer that provides the most intuitive latent-space description fo the data.

### Final deliverables:

* Script for traning a neural network with the proposed best architecture.
* Visualization comparing multiple latent-space representations and justifying the "optimal" choice.

## Relevant Literature
https://onlinelibrary.wiley.com/doi/full/10.1002/qua.24890 https://www.sciencedirect.com/science/article/pii/S0010465519301298

https://www.nature.com/articles/s41467-019-10827-4
