# Lecture 10 - Experiments

In the final lecture of this course we aim to address some experimental developments as well as limitations. In particular we will focus on setups that utilise semiconducting heterostructures, though other setups are also possible.

Recall that at the start of this course, we looked at the intger quantum Hall effect where there are integer plateaus measured in the differential conductance.

The typical system in which this effect is measured is a semiconducting heterostructure that allows the formation of a two-dimensional electron gas (commonly referred to as a 2DEG).
Simple models of semiconductors consist of a filled valence band and an empty conduction band. The two bands are separated by a band gap, with the Fermi energy (below which electronic states are filled at zero temperature) typically sitting within the band gap.

<span style="color:red">Insert Figure</span>

In order to form a 2DEG experimentally, two semiconductors with different band gaps and Fermi energies are brought together. At the interface electrons flow from the semiconductor with the larger Fermi energy to the one with the lower Fermi energy. This flow of electrons leaves behind positively charged ions and therefore an electric field is created. This field bends the bands creating a narrow `well' at the interface in which the electron gas sits - this is a 2DEG.



<span style="color:red">Insert Figure</span>

Semiconducting heterostructures are common experimental setups for a variety of reasons, some more practical such as being eadily available, affordable and therefore can be used in applications. From a more scientifc point of view they are well understood, their properties can be tuned (for example using gate voltages and doping), and they can also be used in the creation of very clean samples, which can be extremely useful in solid state physics even if it is not desired for the integer quantum Hall effect. A common class of experiments performed using 2DEGs are transport experiments where leads are attached to the sample and quantities such as currents and voltages are measured.


## Topological Insulators

Similar setups involving semiconductors can be used to realise topological insulators, using a mechanism known as band inversion.

Many of the models we saw in previous lectures, such as the Haldane and Kane-Mele models were constructed on a honeycomb lattice. Therefore a candidate for their realisation is graphene, however it turns out that due to weak spin-oribit coupling, the bulk gap is very small and the topologically insulating phase can't be observed. Instead, semiconducting heterostrucutres with strong spin-orbit coupling are used.

### Mercury Telluride

The first example of a topological insulator was in mercury telluride heterostructures. These consisted of mercury telluride in conjunction with cadmium telluride.

Cadmium telluride is a standard semiconductor in that it has an "s-wave" band (called the E1 band), with angular momentum states $(-\tfrac{1}{2}, \tfrac{1}{2})$ at a higher energy than a "p-wave" band (the H1 band) which has angular momentum states $(-\tfrac{3}{2}, -\tfrac{1}{2}, \tfrac{1}{2}, \tfrac{3}{2})$. Mercury telluride has an inverted structure

<span style="color:red">Insert Figure</span>

When the two are brought together to form a quantum well, the ordering of the levels depends on the thickness of the well formed. Below a critical thickness, $d_c\sim 6-7 {\rm nm}$, the ordering is that of a conventional semiconductor and we have a topologically trivial regime. However, as the thickness of the well is increased beyond the critical value, the energy ordering of the bands switches or inverts and we are left with a topological regime. 

<span style="color:red">Insert Figure</span>

### Band Inversion

In order to understand why the inverted regime is topological we need to understand what is happening in the band inversion process. 

To start with, recall that the Dirac equation is given by 

$$
H = k_x\sigma_x + k_y\sigma_y + M\sigma_z
$$

where $M$ is the mass parameter whose sign determines the Hall conductance $\sigma_{xy} = \tfrac{e^2}{h}\tfrac{{\rm sgn}(M)}{2}$. Note that it is not an integer here as this is not a lattice model. Despite this we can accurately predict changes in differential conductance between regimes and as we go from negative to positive $M$ as 

$$
\Delta\sigma_{xy}=\frac{e^2}{h}
$$

Therefore if one of the regimes has no Hall conductance and a Chern number of 0 and we change the mass parameter across the transition, the Hall conductance will change to a regime with a Chern number of 1. The inversion of the mass parameter leads to a topological phase trnasition.

This is key in understanding the band inversion process in the quantum well. In this instance the Hamiltonian can be expressed near the $\Gamma$ point $\big[(k_x, k_y)=(0,0)\big]$ in the form

$$
H = \left(\begin{matrix}H_{\bm k} & 0 \\ 0 & H^*_{-{\bm k}}\end{matrix}\right)
$$

where the upper block can be viewed as acting on spin-up and the lower block on spin-down. The two blocks are then related by time-reversal symmetry. The blocks have the standard two band form $H_{\bm k}=d_0\sigma_0+{\bm d}\cdot {\bm \sigma}$ with

$$
\begin{align}d_0 &= \alpha_1-\alpha_2(k_x^2+k_y^2)\\d_x+id_y&=\alpha_3(k_x+ik_y)\\ d_z &= M-\alpha_4(k_x^2+k_y^2)\end{align}
$$

where $\{\alpha_i\}$ are material specific parameters. Let's consider the $\Gamma$ point for simplicity