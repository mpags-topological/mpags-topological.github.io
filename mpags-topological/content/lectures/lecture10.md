# Experiments

In the final lecture of this course we aim to address some experimental developments as well as limitations. In particular we will focus on setups that utilise semiconducting heterostructures, though other setups are also possible.

## The two-dimensional electron gas (2DEG)

Recall that at the start of this course, we looked at the intger quantum Hall effect where there are integer plateaus measured in the differential conductance.

The typical system in which this effect is measured is a semiconducting heterostructure that allows the formation of a two-dimensional electron gas (commonly referred to as a 2DEG).
Simple models of semiconductors consist of a filled valence band and an empty conduction band. The two bands are separated by a band gap, with the Fermi energy (below which electronic states are filled at zero temperature) typically sitting within the band gap.

In order to form a 2DEG experimentally, two semiconductors with different band gaps and Fermi energies are brought together. At the interface electrons flow from the semiconductor with the larger Fermi energy to the one with the lower Fermi energy. This flow of electrons leaves behind positively charged ions and therefore an electric field is created {cite}`Datta`. This field bends the bands creating a narrow well at the interface in which the electron gas sits - this is a 2DEG.

```{figure} ../../_static/figs/2DEG.svg
:width: 100%
:height: 200

A semiconducting heterostructure (left) can be used to create a two-dimensional electron gas, which sits at the well created by the bands bending (right) Figure from {cite}`IhnBook`.
```

Semiconducting heterostructures are common experimental setups for a variety of reasons, some more practical such as being readily available, affordable and therefore can be used in applications. From a more scientfic point of view they are well understood, their properties can be tuned (for example using gate voltages and doping), and they can also be used in the creation of very clean samples, which can be extremely useful in solid state physics even if it is not desired for the integer quantum Hall effect. A common class of experiments performed using 2DEGs are transport experiments where leads are attached to the sample and quantities such as currents and voltages are measured.


## Topological Insulators

Similar setups involving semiconductors can be used to realise topological insulators, using a mechanism known as band inversion.

Many of the models we saw in previous lectures, such as the Haldane and Kane-Mele models were constructed on a honeycomb lattice. Therefore a candidate for their realisation is graphene, however it turns out that due to weak spin-oribit coupling, the bulk gap is very small and the topologically insulating phase can't be observed. Instead, semiconducting heterostrucutres with strong spin-orbit coupling are used.

### Mercury Telluride

The first example of a topological insulator was in mercury telluride heterostructures {cite}`BHZ_Science, QSHExpt`. These consisted of mercury telluride in conjunction with cadmium telluride.

Cadmium telluride is a standard semiconductor in that it has an "s-wave" band (called the E1 band), with angular momentum states $(-\tfrac{1}{2}, \tfrac{1}{2})$ at a higher energy than a "p-wave" band (the H1 band) which has angular momentum states $(-\tfrac{3}{2}, -\tfrac{1}{2}, \tfrac{1}{2}, \tfrac{3}{2})$. Mercury telluride has an inverted structure where the energy levels are the other way round.

When the two are brought together to form a quantum well, the ordering of the levels depends on the width of the well formed. Below a critical width, $w_c\sim 6-7 {\rm nm}$, the ordering is that of a conventional semiconductor and we have a topologically trivial regime. However, as the width of the well is increased beyond the critical value, the energy ordering of the bands switches or inverts and we are left with a topological regime. 

```{figure} ../../_static/figs/InvertedWell.svg
:width: 100%
:height: 300

Band inversion occurs for wide quantum wells.
```

### Band Inversion

In order to understand why the inverted regime is topological we need to understand what is happening in the band inversion process {cite}`BHZ_Science`. 

To start with, recall that the Dirac equation is given by 

$$
H = k_x\sigma_x + k_y\sigma_y + M\sigma_z
$$

where $M$ is the mass parameter whose sign determines the Hall conductance $\sigma_{xy} = \tfrac{e^2}{h}\tfrac{{\rm sgn}(M)}{2}$. Note that it is not an integer here as this is not a lattice model. Despite this we can accurately predict changes in differential conductance between regimes and as we go from negative to positive $M$ as 

$$
\Delta\sigma_{xy}=\frac{e^2}{h}
$$

Therefore if one of the regimes has no Hall conductance and a Chern number of 0 and we change the mass parameter across the transition, the Hall conductance will change to a regime with a Chern number of 1. The inversion of the mass parameter leads to a topological phase transition.

This is key in understanding the band inversion process in the quantum well. In this instance the Hamiltonian can be expressed near the $\Gamma$ point $\big[(k_x, k_y)=(0,0)\big]$ in the form

$$
H = \left(\begin{matrix}H_{\boldsymbol{k}} & 0 \\ 0 & H^*_{-\boldsymbol{k}}\end{matrix}\right)
$$

where the upper block can be viewed as acting on spin-up and the lower block on spin-down. The two blocks are then related by time-reversal symmetry. The blocks have the standard two band form $H_{\boldsymbol{k}}=d_0\sigma_0+{\boldsymbol{d}}\cdot { \boldsymbol{\sigma}}$ with

$$
\begin{align*}d_0 &= \alpha_1-\alpha_2(k_x^2+k_y^2)\\d_x+id_y&=\alpha_3(k_x+ik_y)\\ d_z &= M-\alpha_4(k_x^2+k_y^2)\end{align*}
$$

where $\{\alpha_i\}$ are material specific parameters. Let's consider the $\Gamma$ point for simplicity. There, the Hamiltonian is simply

$$
H_{\boldsymbol{k}}=\alpha_1\sigma_0+M\sigma_z
$$

From this it is clear that $\alpha_1$ is simply an energy offset and $M$ acts in the same way as the mass parameter in the Dirac equation. In particular, it gives the energy gap between the two-levels at the $\Gamma$-point. Now when the width of the well is increased beyond $w_c$, the bands invert and therefore the sign of $M$ has flipped. As for the Dirac equation this leads to a change in the conductivity

$$
\Delta\sigma_{xy}^{\uparrow} = \frac{e^2}{h}
$$

However, in our original Hamiltonian, we also have $H^*_{-\boldsymbol{k}}$ for spin down. Due to time-reversal symmetry in this model, the change in conductivity for this block after the band inversion is

$$
\Delta\sigma_{xy}^{\downarrow} = -\frac{e^2}{h}
$$

These conductance changes effectively signify going from a region that is topologically trivial to one with opposite spin counter-propagating edge states. In other words the region we move to has a pair of helical edge modes as we saw in the Kane-Mele model. To confirm this, we identify the presence of the spin Hall effect by defining the electrical (or charge) and spin Hall conductances as

$$
\begin{align*}\Delta \sigma_{xy}^{(e)} &= \Delta \sigma_{xy}^{\uparrow} +  \Delta \sigma_{xy}^{\downarrow}=0\\ \Delta \sigma_{xy}^{(s)} &= \Delta \sigma_{xy}^{\uparrow} -  \Delta \sigma_{xy}^{\downarrow}=\frac{2e^2}{h}\end{align*}
$$

Such an effect can be detected experimentally, as shown below for samples III and IV. 

```{figure} ../../_static/figs/QSH_Expt.svg
:width: 100%
:height: 300

Experimental observation of the quantum spin Hall effect. This is particularly clear in samples III and IV. Figure from {cite}`QSHExpt`
```

```{note}
There are alternatives to the solid state setup described here, although we won't go into much detail. One key alternative is the use of optical lattices in systems of cold atoms, which allow for a large degree of control as well as a clean system. In this case, magnetic fields are not required and lasers can be used to manipulate/drive the lattice. This can lead to complex couplings/hoppings and the Haldane and Kane-Mele models can be realised {cite}`ColdAtomsExpt, OpticalLatticeExpt`. 
```
## Topological Superconductors

Now we wish to look at experimental implementations of topological superconductors. These are of particular interest at the moment due to the prediction of Majorana zero modes which can be used in implementations of quantum computing. 

```{note}
Majorana modes are not unique to topological superconductors {cite}`MZM_TQC`. They are also predicted to occur in the Fractional Quantum Hall Effect (FQHE). In the FQHE, the setup is similar to the integer quantum Hall effect we came across at the beginning of this course, except now electron-electron interactions must additionally be considered. Whilst the particular microscopic mechanisms for this are an active area of research, what is clear is that there are robust plateaus in the conductance at fractional values of $e^2/h$ (which can be viewed as having a fractional filling factor, $\nu$). 

Abelian anyons have been observed in the $\nu=\tfrac{1}{3}$ state through observation of the braiding statistics {cite}`FQHE_Anyons`, no such confirmation has occured for Majorana modes, which are predicted in the $\nu=\tfrac{5}{2}$ state. 
```

### Engineering Topological Superconductors

Naturally occuring unconventional superconductors are still an active area of research and often a more controllable way to realise a $p$-wave topological superconductor is using a semiconducting heterostructure (see {cite}`AliceaReview, LeijnseFlensberg, SatoReview, SatoReview2` for reviews on the setup and signatures). 

In particular a semiconductor with spin-orbit coupling is placed in conjuction with an $s$-wave superconductor. Along with a magnetic field, this allows the $p$-wave pairing to occur. We show this below by considering how the band structure changes. 

```{figure} ../../_static/figs/TSC_Engineered.svg
:width: 100%
:height: 400

Semiconductor heterostructures can be used to engineer topological superconductivity.
```

Once the samples have been created, it is necessary to have ways to detect Majoranas. Measuring braiding statistics directly using interferometry-style experiments is difficult in solid state setups, and so alternative transport experiments are preferred.

### Zero-bias conductance

The first of these is not on its own a conclusive signature of Majoranas, although any system with Majoranas will display it. 

Consider a one-dimensional setup (although the argumets here generalise to two dimensions too), where we have a lead in conjunction with a wire in a topological superconductor phase. For voltages smaller than the superconducting gap, there are two possible processes present. These are normal reflection and Andreev reflection, and it is the latter that can result in current flowing through the system.

```{note}
Normal reflection is a standard reflection process. An electron comes in and doesn't have enough energy to enter the superconductor. It is simply reflected back in the direction it came. Andreev reflection is specific to a superconductor where at the interface, an electron can be reflected as a hole, and a Cooper pair then propagagtes in the superconductor.

```{figure} ../../_static/figs/Andreev.svg
:width: 100%
:height: 100

Normal and Andreev reflection.
```



Since the Andreev reflection results in the propagation of a Copper pair, it is this process that facilitates a current passing through the system, with the current depending on the probability of Andreev reflection to occur, $|S_{he}|^2$,

$$
I = \frac{2e}{h}\int_0^{eV} {\rm d}\varepsilon |S_{he}(\varepsilon)|^2 \implies G = \frac{{\rm d}I}{{\rm d}V} = \frac{2e^2}{h} |S_{he}(\varepsilon=eV)|^2
$$

Since we are interested in a zero bias peak in the conductance (the analysis can be done for finite $V$ but it is beyond this course), we therefore nned to calculate the probability of Andreev reflection at zero energy. To do this we use the S-matrix which links the incoming to outgoing states.  

```{figure} ../../_static/figs/ScatteringStates.svg
:width: 100%
:height: 100

The incoming and outgoing states, as defined in the scattering problem.
```

$$
\Psi_{\rm out} = S \Psi_{\rm in} \implies \left(\begin{matrix} e \\ h \end{matrix}\right)_{\rm out} = \left(\begin{matrix} S_{ee} & S_{eh} \\ S_{he} & S_{hh} \end{matrix}\right)\left(\begin{matrix} e \\ h \end{matrix}\right)_{\rm in}
$$

Using that the S-matrix obeys particle-hole symmetry means that at $\varepsilon=0$, we have

$$
S_{hh}^* = S_{ee}, \hspace{10pt} S_{he}^* = S_{eh}
$$

Additionally, we can use that the S-matrix is unitary to lead to the following two conditions: (1) $|S_{ee}|^2 + |S_{he}|^2$ = 1, and (2) $2S_{ee}S_{he} = 0$.

These conditions lead to two possible forms of the S-matrix

$$
S_N(0) =  \left(\begin{matrix} {\rm e}^{i\alpha} & 0 \\ 0 & {\rm e}^{-i\alpha} \end{matrix}\right), \hspace{10pt} S_A(0) =  \left(\begin{matrix} 0 & {\rm e}^{-i\beta} \\ {\rm e}^{i\beta} & 0 \end{matrix}\right)
$$

where the first corresponds to perfect normal reflection and the second, perfect Andreev reflection. If the superconductor is in the trivial regime, then we have perfect normal reflection, whereas if the superconductor is in the topological regime we have perfect Andreev reflection. The actual mechanism by which this occurs is slightly more involved than the introductory arguments presented here, but the zero-energy edge mode facilitates the conversion of the electron to the hole, therefore enabling the Andreev reflection. This results in a zero bias conductance peak

$$
 G(V=0) = \frac{2e^2}{h}
$$

Some groups have reported measurements of this peak suggesting the observation of Majoranas, however it turns out that similar peaks can be caused by low-energy modes that arise due to disorder in the system. A definitive measurement of Majorana zero modes is still sought after {cite}`DasSarma_Expt_Review`.


### Fractional Josephson Effect

A more conclusive signature would be the observation of the fractional Joesphson effect, however as of yet there haven't been any reproducible measurements of this.

```{note}
The standard Josephson effect considers two superconductors separated by a tunnel barrier. 

The order parameters for these can be expressed in the form $\psi_i = \sqrt{n_i}{\rm e}^{i\phi_i}$, where $n_i$ is the number density of Cooper pairs. The phase difference $\delta\phi=\phi_R-\phi_L$ results in a current flowing between the superconductors

$$
I = I_{\rm c} \sin(\delta\phi) 
$$

Additionally, if we apply a voltage across the Josephson junction, we can write 

$$
\frac{{\rm d}\delta\phi}{{\rm d}t} = \frac{2e}{\hbar}V(t)
$$

which results in the Josephson current becoming time dependent $I(t) = I_{\rm c} \sin(\delta\phi(t)) $
```

Consider two Kitaev chains (labelled by $\alpha=L,R$)

$$
H_{\alpha}= -t\sum_{m=1}^{N-1}\left(c_{m+1, \alpha}^\dagger c_{m, \alpha} + c_{m, \alpha}^\dagger c_{m+1, \alpha}\right) - \mu\sum_{m=1}^Nc_{m, \alpha}^\dagger c_{m, \alpha} + \sum_{m=1}^{N-1}\left(\Delta c_{m, \alpha} c_{m+1, \alpha} + \Delta^*c_{m+1, \alpha}^\dagger c_{m, \alpha}^\dagger\right)
$$

The coupling between the superconductors is then given by 

$$
H_{\rm tun} = -\Gamma(c_{L, N}^\dagger c_{R,1}+{\rm h.c.})
$$

In the topological regime, $\mu=0, t=|\Delta|$, we write the Hamiltonians in terms of the Majorana operators

$$
H_\alpha = it\sum_{m=1}^{N-1} \gamma_{2m, \alpha} \gamma_{2m+1,\alpha} 
$$

Recall that the zero energy edge modes don't appear in this Hamiltonian and therefore if we want to just explore the effect of these zero modes on the Josephson current we need to see how these zero modes appear in the tunnelling term. Writing the tunnelling term in terms of Majorana operators and only keeping the zero-energy edge operators, leads to the effective low-energy Hamiltonian

$$
\begin{align*}
H_{\rm eff} &= -\frac{\Gamma}{2}\left(-\frac{1}{2}{\rm e}^{-i\delta\phi/2}i\gamma_{2N}^{(L)}\gamma_1^{(R)} + {\rm h.c.}\right) \\ &=-\frac{\Gamma}{2}\cos \left(\frac{\delta\phi}{2}\right)i\gamma_{2N}^{(L)}\gamma_1^{(R)} \\ &=-\Gamma  \cos \left(\frac{\delta\phi}{2}\right) (n_f-\tfrac{1}{2})
\end{align*}
$$

where in the last line we have defined a fermion $f=\tfrac{1}{2}(\gamma_{2N}^{(L)} + i\gamma_1^{(R)} )$ and $n_f = f^\dagger f$.

The Josephson current. due to the zero-energy edge modes is then

$$
I = \frac{2e}{\hbar}\frac{{\rm d}E}{{\rm d}(\delta\phi)} = \pm \frac{e\Gamma}{\hbar}\sin \left(\frac{\delta\phi}{2}\right)
$$

where the plus sign is for $n_f=1$ and the minus is for $n_f=0$. Note that $n_f$ is conserved so we can't go between the branches. This is the fractional Josephson effect. The reason for the name is that the current is proportional to $(e/h)$ rather than $(2e/h)$, so we can think of a fraction of a Cooper pair being transmitted. Perhaps more importantly is that the current is proportional to $\sin(\delta\phi/2)$ rather than $\sin(\delta\phi)$, which means we have doubled the period to $4\pi$. This, if observed, would be a clear signature of Majorana modes.


## Summary

The original observation of topological insulators represented a key breakthrough in the study of topological physics and has led to many further studies. The path to observe Majoranas has been more challenging and there are other experiments that we have not had time to cover here, particularly interferometry style experiments which aim to probe the non-Abelian statistics of Majoranas more directly. Despite many different experimental avenues being explored,results claiming to have observed Majoranas are still contested and we still don't have conclusive evidence of their existence. Their detection, however, is still an active area of research, particularly due to their proposed use in topological quantum computation. 


---

## References

```{bibliography}
:filter: docname in docnames
```

