# Nearest-neighbor subsampling efficiency improvement

Contact: Nicole Hu

Date: 08/23/2021

## _Background:_

Our group has developed an atomic environment fingerprinting scheme under AMPTorch called Gaussian Multi-Poles (GMPs). AMPTorch is an atomistic neural network potential training package based on PyTorch jointly developed by our collaborators. The specific branch we work on with the latest implementations of GMPs is `MCSH_paper1_lmdb`, available via [Github](https://github.com/ulissigroup/amptorch/tree/MCSH_paper1_lmdb). The trained neural network potential takes atomic positions as input, and output the predicted potential energy and forces if force training is turned on. This will be the default toolkit for this project. 

A paper that elaborates the theories and strategies to construct a neural network potential to simulate atomistic environment and to predict the potential energy is given in ref [[1]](https://onlinelibrary.wiley.com/doi/full/10.1002/qua.24890). For the specific fingerprint scheme, please refer to ref [[2]](https://arxiv.org/abs/2102.02390v2)

The dataset to train the neural network potential with AMPTorch package is listed under directory `/data`. It contains `ase` Trajectory files of randomly selected 3,000 points for training from a published dataset, [OC20](https://opencatalystproject.org/).  

This project will focus on improving the efficiency of a current implementation of a subsampling algorithm that selects images based on nearest-neighbor algorithm. The subsampling algorithm works in the feature space, and uses the nearest-neighbor algorithm to calculate the Euclidean distances. It deletes ponits that are within user-defined cutoff. Currently, the speed of the algorithm is dependent on the number of data points and the feature dimensions. This project will use the [branch under testing on Github](https://github.com/nicoleyghu/amptorch/tree/MCSH_paper1) with latest improvement on nearest-neighbor subsampling. 

    * Dataset: `data/amptorch_data/*`

## _Midterm Goal:_
By the midterm you should be able to generate a baseline neural network model with the test run training data and develop a hyperparameter optimization workflow.

* **Midterm deliverables:** A zip file with the results including a log file with the RMSE values and input files.


## _Final Goal:_

By the final you should have a report of the profiling of the nearest-neighbor subsampling and identify an aspect to improve the efficiency. 

* **Final deliverables:** A zip file with the profiling data collected and codes for subsampling where the efficiency is improved. 


## _Reference_

[1] Behler, J. (2015). Constructing high-dimensional neural network potentials: A tutorial review. International Journal of Quantum Chemistry, 115(16), 1032–1050. https://doi.org/10.1002/qua.24890

[2] Lei, X., & Medford, A. J. (2021). A Universal Framework for Featurization of Atomistic Systems. http://arxiv.org/abs/2102.02390

