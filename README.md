# Dissipative particle dynamics

This is 2D domain decomposition parallel implementation.

## Hardware requirements

DPD requires a standard computer with enough RAM to support the operations defined by a user but the simulating system size depends on RAM. For minimal performance, this will be a computer with about 2 GB of RAM. For optimal performance, we recommend to use Supercomputere facilities:

## Software requirements

This package is supported for Linux operating systems. The package has been tested on the following systems:

Linux: Ubuntu 16.04, CentOS Linux (release 7.1.1503)

## Installation guide

In `example` folder you will find the `makefile`. Put together `makefile` and `dpd.F90` and type 
```
make
```
in terminal. So you compile fortran file dpd.F90 with GNU Fortran (default) or Intel Fortran compiler. To run the application you need configuration file `dpdconf.dat`, input files `*.mol` and executable `dpd`. Then just type:
```
./dpd
```
You will find test sets in `example` folder.

## Overview
In this implementation periodic boundary conditions works only for the solvent particles (type 4 - N), grid particles are not moving at all (type 3 - P), chain particles can not move outside the box (type 1 - O and 2 - S). There are three stages (see dpdconf.dat): the first one is to equilibrate system, the second one is to simulate bonds formation and the third one is to simulate system without bonds formation. To visualize output restart files you may convert it to mol2 via `rst2mol2.py`. You will find it in `example` folder.

## Example
In example folder you will find two subfolders: `demo` and `reproduction`. 
 - In the first folder there is an example of small cell with simple solvent. Сalculation takes about 1 minutes. Finally you will get 4 files: initial system, after first stage, after second and after third.
 - In the second folder there are parameters to reproduce the results. Strongly recommend to use Cluster facilities because the system is large.


## Citation
This program has been used in the following works [1-7], please cite some of this in case of using this code. The detailed description of DPD can be found in [8].

## Refs.

(1)     Gavrilov, A. A.; Chertovich, A. V. Copolymerization of Partly Incompatible Monomers: An Insight from Computer Simulations. Macromolecules 2017, 50 (12), 4677–4685.

(2)     Tamm, M. V.; Nazarov, L. I.; Gavrilov, A. A.; Chertovich, A. V. Anomalous Diffusion in Fractal Globules. Phys. Rev. Lett. 2015, 114 (17), 178102.

(3)     Govorun, E. N.; Gavrilov, A. A.; Chertovich, A. V. Multiblock Copolymers Prepared by Patterned Modification: Analytical Theory and Computer Simulations. J. Chem. Phys. 2015, 142 (20), 204903.

(4)     Gavrilov, A. A.; Chertovich, A. V.; Khalatur, P. G.; Khokhlov, A. R. Study of the Mechanisms of Filler Reinforcement in Elastomer Nanocomposites. Macromolecules 2014, 47 (15), 5400–5408.

(5)     Gavrilov, A. A.; Kudryavtsev, Y. V.; Chertovich, A. V. Phase Diagrams of Block Copolymer Melts by Dissipative Particle Dynamics Simulations. J. Chem. Phys. 2013, 139 (22), 224901.

(6)     Gavrilov, A. A.; Chertovich, A. V.; Khalatur, P. G.; Khokhlov, A. R. Effect of Nanotube Size on the Mechanical Properties of Elastomeric Composites. Soft Matter 2013, 9 (15), 4067–4072.

(7)     Ulianov, S., Khrameeva, E., Gavrilov, A., Flyamer, I., Kos, P., Mikhaleva, E., Penin, A., Logacheva, M., Imakaev, M., Chertovich, A., Gelfand, M., Shevelyov, Y., and Razin, S. Active chromatin and transcription play a key role in chromosome partitioning into topologically associating domains." Genome research 2016, 26 (1), 70-84.

(8) Groot, Robert D., and Patrick B. Warren. "Dissipative particle dynamics: Bridging the gap between atomistic and mesoscopic simulation." The Journal of chemical physics 1997, 107 (11), 4423-4435.
