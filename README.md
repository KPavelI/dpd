# Dissipative particle dynamics

This is 2D domain decomposition implementation.

You should compile fortran file and modify dpdconf.dat as you wish.

In this implementation periodic boundary conditions works only for the solvent particles (type 4 - N), grid particles are not moving at all (type 3 - P), chain particles can not move outside the box (type 1 - O and 2 - S).

This program has been used in the following works [1-7]. The detailed description of DPD can be found in [8].

# Refs.

(1)     Gavrilov, A. A.; Chertovich, A. V. Copolymerization of Partly Incompatible Monomers: An Insight from Computer Simulations. Macromolecules 2017, 50 (12), 4677–4685.

(2)     Tamm, M. V.; Nazarov, L. I.; Gavrilov, A. A.; Chertovich, A. V. Anomalous Diffusion in Fractal Globules. Phys. Rev. Lett. 2015, 114 (17), 178102.

(3)     Govorun, E. N.; Gavrilov, A. A.; Chertovich, A. V. Multiblock Copolymers Prepared by Patterned Modification: Analytical Theory and Computer Simulations. J. Chem. Phys. 2015, 142 (20), 204903.

(4)     Gavrilov, A. A.; Chertovich, A. V.; Khalatur, P. G.; Khokhlov, A. R. Study of the Mechanisms of Filler Reinforcement in Elastomer Nanocomposites. Macromolecules 2014, 47 (15), 5400–5408.

(5)     Gavrilov, A. A.; Kudryavtsev, Y. V.; Chertovich, A. V. Phase Diagrams of Block Copolymer Melts by Dissipative Particle Dynamics Simulations. J. Chem. Phys. 2013, 139 (22), 224901.

(6)     Gavrilov, A. A.; Chertovich, A. V.; Khalatur, P. G.; Khokhlov, A. R. Effect of Nanotube Size on the Mechanical Properties of Elastomeric Composites. Soft Matter 2013, 9 (15), 4067–4072.

(7)     Ulianov, S., Khrameeva, E., Gavrilov, A., Flyamer, I., Kos, P., Mikhaleva, E., Penin, A., Logacheva, M., Imakaev, M., Chertovich, A., Gelfand, M., Shevelyov, Y., and Razin, S. Active chromatin and transcription play a key role in chromosome partitioning into topologically associating domains." Genome research 2016, 26 (1), 70-84.

(8) Groot, Robert D., and Patrick B. Warren. "Dissipative particle dynamics: Bridging the gap between atomistic and mesoscopic simulation." The Journal of chemical physics 1997, 107 (11), 4423-4435.
