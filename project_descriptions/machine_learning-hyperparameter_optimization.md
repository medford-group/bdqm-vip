# Hyperparameter Optimization for AMPTorch
Advisor: Nicole Hu


## _Background:_

Our group has developed an atomic environment fingerprinting scheme under AMPTorch called Gaussian Multi-Poles (GMPs). AMPTorch is an atomistic neural network potential training package based on PyTorch jointly developed by our collaborators. The specific branch we work on with the latest implementations of GMPs is `master`, available via [Github](https://github.com/ulissigroup/amptorch). The trained neural network potential takes atomic positions as input, and output the predicted potential energy and forces if force training is turned on. This will be the default toolkit for this project. 

A paper that elaborates the theories and strategies to construct a neural network potential to simulate atomistic environment and to predict the potential energy is given in ref [[1]](https://onlinelibrary.wiley.com/doi/full/10.1002/qua.24890). For the specific fingerprint scheme, please refer to ref [[2]](https://arxiv.org/abs/2102.02390v2)

The dataset to train the neural network potential with AMPTorch package is listed under directory `/data/amptorch_data.zip`. It contains `ase` Trajectory files of randomly selected 3,000 points for training from a published dataset, [OC20](https://opencatalystproject.org/).  

For this semester, we want to build the existing hyperparameter optimization pipeline to study the difference between two different datasets. One named `MD17` which consists of the molecular dynamic simulations of aspirin molecules. Another named `OC20` which consists of metal-adsorbate catalytic systems. With difference in two datasets, we want to see what are the differences with optimal hyperparameters to guide further research. This project will first focus on improving training accuracy by developing a pipeline to tune the hyperparameters of descriptor generation and neural network architecture (e.g. number of nodes, layers, activation functions, etc.), and apply to two datasets for comparison. The training dataset of OC20 consists of 3,000 images, and 300 images of testing dataset to be kept outside of training and used to assess the accuracy of the NN model. 

    * Dataset: `data/amptorch_data.zip`

## _Final Goal:_

By the final you should have a report of the optimal hyperparameters for two datasets. 

* **Final deliverables:** A zip file with all model details and checkpoints to reliably reproduce the results, along with a report explaining your strategy and the reasoning behind the improved performance.

## _Reference_

[1] Behler, J. (2015). Constructing high-dimensional neural network potentials: A tutorial review. International Journal of Quantum Chemistry, 115(16), 1032–1050. https://doi.org/10.1002/qua.24890

[2] Lei, X., & Medford, A. J. (2021). A Universal Framework for Featurization of Atomistic Systems. http://arxiv.org/abs/2102.02390
