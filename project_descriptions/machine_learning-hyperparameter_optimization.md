# Hyperparameter Optimization for AMPTorch

Contact: Nicole Hu

Date: 01/26/2020

## _Background:_

Our group is working to develop a new PyTorch-based version of AMP software[[1]](https://www.sciencedirect.com/science/article/pii/S0010465516301266) named AMPTorch. An Alpha version of AMPTorch is available via [Github](https://github.com/ulissigroup/amptorch). The trained neural network potential takes atomic positions as input, and output the predicted potential energy. This will be the default toolkit for this project. 

A paper that elaborates the theories and strategies to construct a neural network potential to simulate atomistic environment and to predict the potential energy is given in ref [[2]](https://onlinelibrary.wiley.com/doi/full/10.1002/qua.24890). 

The dataset to train the neural network potential with AMPTorch package is listed under directory `/data`. It contains `ase` Trajectory files of water molecules interacting with a TiO2 surface from molecular dynamics simulations.  



## _Project Description:_

This project will focus on improving training accuracy by developing a pipeline to tune the hyperparameters of descriptor generation and neural network architecture (e.g. number of nodes, layers, activation functions, etc.). The test run dataset consists of 270 images of training data, and 30 images of testing dataset that'd be kept outside of training and be used to analyze the accuracy of the NN model. The test run dataset will be used for familiarizing with the tool-kits and develop optimization pipelines. 
    * Dataset: `data/amptorch_data/test_run/*`

There would also be three datasets of various sizes added later in this term to apply the hyperparameter optimization routines and check if the optimal settings are similar. These datasets will be published later. 

## _Midterm Goal:_
By the midterm you should be able to generate a baseline neural network model with the test run training data and develop a hyperparameter optimization workflow.

* **Midterm deliverables:** A zip file with the results including a log file with the RMSE values and input files.


## _Final Goal:_
By the final you should have a report of the optimal hyperparameters for the three datasets of different sizes. 

* **Final deliverables:** A zip file with all model details as described in the midterm deliverable, along with a report explaining your strategy and the reasoning behind the improved performance.

## _Reference_

[1] Alireza Khorshidi, Andrew A.Peterson. [Amp: A modular approach to machine learning in atomistic simulations.](https://www.sciencedirect.com/science/article/pii/S0010465516301266)

[2] Jörg Behler. [Constructing high‐dimensional neural network potentials: A tutorial review](https://onlinelibrary.wiley.com/doi/full/10.1002/qua.24890)

