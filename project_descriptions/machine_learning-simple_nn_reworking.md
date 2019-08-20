# Machine Learning -  Simple\_NN Improvement
Advisor: Ray Lei

Simple\_NN is a python package out of South Korea for generating machine learned potential energy surfaces (known as neural network forcefields.) These are models that can be trained reproduce the results of DFT but at much lower cost. Currently we use Simple\_NN as a standard in our group. However, this package has some issues producing consistent results. We have a fork of the pakage and are looking to modify it and improve it for our own purposes.

Your first goal will be to learn to use the package and train a force field with data provided. Next, you must understand the code and modify it to train more consistently. Finally, you must explore the different hyper-parameters that can be changed in Simple\_NN and produce recommendations on how it should be run.

https://github.com/medford-group/SIMPLE-NN

## Midterm Goal:

* Train a neural network forcefield from the psi4 data provided to have a force RMSE of 0.07 eV/A
* Establish a scheme to ensure training is generally consistent across runs


### Midterm Deliverables:
A zip file containing your successful run and commits to the `medford-group` fork that make substative changes improving the code.


## Final Goal:
* Modify Simple\_NN to produce constitent results
* produce a set of recommened defaults to run the program at and commit them to the simple\_NN repo


### Final Deliverables:
Commits on the `medford-group` fork of Simple\_NN.

### Relevant Literature:
https://onlinelibrary.wiley.com/doi/full/10.1002/qua.24890
https://www.sciencedirect.com/science/article/pii/S0010465519301298
