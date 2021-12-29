# Nearest-neighbor subsampling efficiency improvement

Advisor: Nicole Hu

## _Background:_

Our group has developed an atomic environment fingerprinting scheme under AMPTorch called Gaussian Multi-Poles (GMPs). AMPTorch is an atomistic neural network potential training package based on PyTorch jointly developed by our collaborators. The specific branch we work on with the latest implementations of GMPs is `MCSH_paper1_lmdb`, available via [Github](https://github.com/ulissigroup/amptorch/tree/MCSH_paper1_lmdb). The trained neural network potential takes atomic positions as input, and outputs the predicted potential energy and forces if force training is turned on. This will be the default toolkit for this project. 

A paper that elaborates the theories and strategies to construct a neural network potential to simulate atomistic environment and to predict the potential energy is given in ref [[1]](https://onlinelibrary.wiley.com/doi/full/10.1002/qua.24890). For the specific fingerprint scheme, please refer to ref [[2]](https://arxiv.org/abs/2102.02390v2) An example dataset to train the neural network potential with AMPTorch package is listed under directory `/data`. It contains `ase` Trajectory files of randomly selected 3,000 points for training from a published dataset, [OC20](https://opencatalystproject.org/).  

This project will focus on improving the efficiency of a current implementation of a subsampling algorithm that selects images based on nearest-neighbor algorithm. The subsampling algorithm works in the feature space, and uses the nearest-neighbor algorithm to calculate the Euclidean distances. It deletes points that are within user-defined cutoff. Currently, the speed of the algorithm is dependent on the number of data points and the feature dimensions. This project will use the [branch under testing on Github](https://github.com/nicoleyghu/amptorch/tree/MCSH_paper1) with latest improvement on nearest-neighbor subsampling. The subsampling algorithm was significantly improved through the VIP course in Fall 2021, and this project will work on applying these developments to test the limits of the improved algorithm. In addition, the project will evaluate the feasibility of using the NNS algorithm for clustering.

    * Testing Dataset: `data/amptorch_data/*`

## _Midterm Goal:_

- Apply the NNS algorithm to the [OC20](https://opencatalystproject.org/) IS2RE dataset (~100K points) to establish the limits of scalability

- Evaluate the possibility of using the NNS algorithm for clustering by treating each of the selected data points as the "center" of a cluster.

* **Midterm deliverables:** 

- Down-sampled versions of OC20 IS2RE containing 1000, 5000, 10,000 and 50,000 data points selected with NNS (LMDB files on PACE ICE).

- Demonstrate proof-of-concept for a clustering variant of the NNS algorithm (txt file describing implementation and testing).


## _Final Goal:_

- Apply the NNS algorithm to the full S2EF dataset from OC20 (~100M points) if possible.

- Modify NNS implementation to enable clustering within AMPTorch.


* **Final deliverables:** 

- Down-sampled versions of OC20 S2EF containing 100K, 500K, 1M and 5M data points selected with NNS (LMDB files on PACE ICE).

- Application of clustering algorithm to OC20 S2EF or IS2RE dataset and analysis of resulting clusters (text file or pdf with figures)

## _Reference_

[1] Behler, J. (2015). Constructing high-dimensional neural network potentials: A tutorial review. International Journal of Quantum Chemistry, 115(16), 1032–1050. https://doi.org/10.1002/qua.24890

[2] Lei, X., & Medford, A. J. (2021). A Universal Framework for Featurization of Atomistic Systems. http://arxiv.org/abs/2102.02390

