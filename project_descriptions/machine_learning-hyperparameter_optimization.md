# Hyperparameter Optimization for AMPTorch

Contact: Nicole Hu

Date: 08/28/2020

## _Background:_

Our group is working to develop a new PyTorch-based version of AMP software[[1]](https://www.sciencedirect.com/science/article/pii/S0010465516301266). An Alpha version of AMPTorch is available via [Github](https://github.com/ulissigroup/amptorch). The trained neural network potential takes atomic positions as input, and output the predicted potential energy. This will be the default toolkit for this project. 

A paper that elaborates the theories and strategies to construct a neural network potential to simulate atomistic environment and to predict the potential energy is given in ref [[2]](https://onlinelibrary.wiley.com/doi/full/10.1002/qua.24890). 

The dataset to train the neural network potential with AMPTorch package is listed under directory `/data`. It contains `ase` Trajectory files of water molecules interacting with an iron surface from molecular dynamics simulations.  



## _Project Description:_

1. _Project 1_ will focus on improving training accuracy by developing a pipeline to tune the hyperparameters of descriptor generation (e.g. parameters in G's that defines the symmetry function) and neural network architecture (e.g. number of nodes, layers, activation functions, etc.). Dataset for this project will involve 360 images of training data, and 41 images of testing dataset that'd be kept outside of training and be used to analyze the accuracy of the NN model. Previous training of a NN potential on this dataset gives an error of ~35 meV per atom energy. 
    * Dataset: `data/amptorch_data/Project_1/*`

2. _Project 2_ will focus on profiling AMPTorch, identifying and improving its bottlenecks to ensure the scalability and speed when challenged with a large dataset. The investigator will be provided with a dataset of ~16,000 frames each containing 35-164 atoms. 
    * Dataset: `data/amptorch_data/Project_2/*`

## _Midterm Goal:_
1. _Project 1:_ By the midterm you should be able to generate a neural network model with accuracy comparable to the accuracy already achieved in the group (see above).
    * **Midterm deliverables:** A zip file with the results including a log file with the RMSE values and input files.
2. _Project 2:_ The progess of this project will be assessed more openly with discussion of Prof. Medford and Nicole. Performance analysis with different implementations of a specific feature of AMPTorch that allows for better performance/stability would be acceptable. 

## _Final Goal:_
1. _Project 1:_ By the final you should have a neural network model and/or training strategy that has an improved accuracy for energies. 
    * **Final deliverables:** A zip file with all model details as described in the midterm deliverable, along with a report explaining your strategy and the reasoning behind the improved performance.

2. _Project 2:_ By the final you should have a feature of AMPTorch that outperforms the orignal package in speed, scalability on the given dataset. 
    * **Final deliverables:** An implemented feature or improvement integrated into AMPTorch.  

## _Reference_

[1] Alireza Khorshidi, Andrew A.Peterson. [Amp: A modular approach to machine learning in atomistic simulations.](https://www.sciencedirect.com/science/article/pii/S0010465516301266)

[2] Jörg Behler. [Constructing high‐dimensional neural network potentials: A tutorial review](https://onlinelibrary.wiley.com/doi/full/10.1002/qua.24890)

