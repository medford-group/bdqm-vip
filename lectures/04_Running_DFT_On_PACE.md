# Running DFT on PACE

Today we're going to go over how to run DFT calculations on the PACE supercomputing cluster. To review, a supercomputing cluster is a network of connected computers. You enter in the login node and request computing time on the computing nodes.

![alt text](https://ucdavis-bioinformatics-training.github.io/2017-June-RNA-Seq-Workshop/monday/cluster_diagram.png "Cluster Supercomputer Structure")

Let's start by logging into the pace-ice cluster.

```
ssh -X [username]@pace-ice.pace.gatech.edu
```

enter your password

## Interacting With The Compute Nodes

This section will discuss how to ask for computing resources from PACE. PACE usings a batch queue system called [Portable Batch System (PBS)](https://en.wikipedia.org/wiki/Portable_Batch_System), here is a quick [cheat sheet](https://albertsk.files.wordpress.com/2011/12/pbs.pdf) on how to use it.

The PBS Queue system is a program that monitors user requests for computing time and allocates computing time based on resources available, the size of the request, how much the user has asked for in the past, ect... There is a semi-sophisticated alogrithim that controls how the resources are allocated.

### Inspecting The Queue
In a supercomputing cluster, there are subsets of compute nodes known as "queues." These are a set ofnodes that all accept jobs from the same line or "queue" of jobs. We have access to the `pace-ice` queue. To view what is in that queue we will run:

```
qstat pace-ice
```

This shows all the jobs in that queue at the moment. We can check the overall status of this queue with:

```
pace-check-queue pace-ice
```

Each line is a compute node (a rack computer sitting somewhere on campus.) The hostname is the internal address of this node, the tasks/np is how many of it's cores are being used, ect...

We can see what jobs we are running with:

```
qstat -u [username]
```

### Submitting Jobs

We need a script file to submit a job, this needs to have a particular form based on the PBS Queue system requirements, here is an example:

```
#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=0:02:00
#PBS -q pace-ice
#PBS -N hello_world_job
#PBS -o stdout
#PBS -e stderr
cd $PBS_O_WORKDIR

echo "hello world"
```

This particular script doesn't do much other than print "hello world" There are a few sections We need to break down.

The first is the `#!/bin/bash` this just tells th system that it is a bash script and to use the bash shell to run it.

The next block is a set of comments all starting with `#PBS` These are a signal to the queue system to read inputs. The first two have a `-l` flag, this is a resource request. Here we are asking for 1 node with 1 core per node. Basically, a single processor. The second line is asking for 2 minutes of "walltime" which is just how long we want that one processor for. The next line with the `-q` flag is what queue we're asking for. Here we want to use the `pace-ice` queue. The `-N` line gives the job a name. Then the final two are telling the system where to direct the output and error messages to.

Let's run this one. first we want to make a new directory (_never run jobs in your home directory, it confuses the queuing system_.) 

```
mkdir pace_run
cd pace_run
```

Next letsput this into a file:

```
nano run.sh
```

Finally to submit a job we need to use the `qsub` command. We just run `qsub [the name of the file]`. So that's:

```
qsub run.sh
```

now lets look at it in the queue:

```
qstat -u [username]
```

Keep in mind that it may have already run. If it did run, we'll see the files `stdout` and `stderr` which contain the output.

## Doing DFT

We'll be using `SPARC-X` as our DFT calculator. This is an experimental calculator we're helping to develop.

### Getting Set Up

Let's start by making a new directory:

```
cd ../
mkdir sparc_run
cd sparc_run
```

We'll also need to load in SPARC and the accompanying software. To do that we're going to source an environmnet I made just for this.

```
source /nv/pace-ice/bcomer3/sparc_env.sh
```

What is this doing? It is adding things to your `$PATH` and `$PYTHONPATH`. Linux looks for commands and programs to run by checking through the variable `$PATH` to find the program/command you've asked for. This is not critical to understand, but I mention it so this doesn't seem like magic.

### Running A DFT Calculation in ASE

Using ASE to run DFT is just like running EMT like we did in the second week. Let's copy the example script below into a new file:


```
# import stuff
from sparc.sparc_core import SPARC
from ase.build import molecule

# make the atoms
atoms = molecule('H2O')
atoms.cell = [[6,0,0],[0,6,0],[0,0,6]]
atoms.center()

# set up the calculator
calc = SPARC(
             KPOINT_GRID=[1,1,1],
             h = 0.2,
             EXCHANGE_CORRELATION = 'GGA',
             TOL_SCF=1e-5,
             RELAX_FLAG=1,
             PRINT_FORCES=1,
             PRINT_RELAXOUT=1)

# set the calculator on the atoms and run
atoms.set_calculator(calc)
print(atoms.get_potential_energy())

```

There are now keyword arguments in the calculator. Kpoints are the density at which we sample the inverse space (maybe AJ can explain better.) `h` is the grid spacing of our mesh basis set. `tol_scf` is the convergence criteria. `Relax\_Flag` is just telling it we want to perform a structural relaxtion. The reset are controlling the output.

Let's run it (don't do this normally.) Note that it has made lots of output files. `sprc-calc.out` is the main one.

At the top are the settings. Many of these are defaults we did not enter. Next we See `Self Consistent Field` blocks. These are converging the electron density of the structure. Once converged it gets the energy and forces, then moves the atoms down the potential energy surface.

### Submitting DFT Calculations

Let's make a fresh folder:

```
cd ../
mkdir PBS_sparc_run
cd PBS_sparc_run
```

Let's copy in our sparc python script and PBS batch file. We need to modify the PBS file to source our environment and run the script. So remove `echo "hello world"` and put in:

```
source /nv/pace-ice/bcomer3/sparc_env.sh
python calc_sparc.py
```

now let's submit it. With luck it will run and we can view the result

## Doing The Training Project

You will need to calculate the reaction energy of oxygen and hydrogen converting to water at different values of `h`. The details are in the project description. Please let us know if you have questions.


## But What is SPARC-X Actually Doing?

In a broad sense, SPARC-X is solving the schrodinger equation very approximately. It is doing this through an iterative calculation. You begin with some initial guess of the electron density, then refine that by minimizing the energy. Once you've hit some convergence criteria, you terminate this, then you can calculate the energy and forces.

