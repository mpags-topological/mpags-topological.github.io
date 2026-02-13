# Introduction to Topology in Condensed Matter Physics

In this course, we aim to give an overview of many different aspects of topology in condensed matter physics. We hope to show the its importance in this area of physics and why it is an active research field. We will begin in this lecture by demonstrating the usefulness of a topological description and how it can be used to explain robust phenomena. To do this we will explore the integer quantum Hall effect. However, first we wish to introduce why we may wish to study topological phases.

## Topological Phases of Matter - An Overview

The role of topology in condensed matter physics has been a key area of research in recent years with a key motivator being the desire to further our classification of phases of matter. 'Traditional' phases of matter are characterised by a local order parameter which we can use to identify the phase. Transitions to more ordered states then involve the breaking of a symmetry. This is the Ginzburg-Landau theory of spontaneous symmetry breaking and underpins many of the phase transitions we are familiar with {cite}`Tinkham_SC, Coleman_ManyBody` - for example, magnetisation, superconductors and the water phase diagram.

```{figure} ../../_static/figs/SSB.svg
:width: 100%
:height: 400

Spontaneous symmetry breaking in a superconductor leads to a non-zero superconducting density below the transition temperature.
```

However not all phases of matter are characterised by a local parameter, examples of which are the topological phases that will be discussed in this course (as well as those that go beyond the scope of these introductory lectures). In particular we will consider three classes
 
- Free fermions
- Symmetry protected topological (SPT) phases
- Topologically ordered states

A simplistic view of a topological state is that it remains the same under continuous deformations - the classic example is that a coffee cup is the same as a doughnut, with the characterisation being that they have the same number of holes.




```{figure} ../../_static/figs/CoffeeCup_Doghnut.gif
:width: 100%
:height: 400

A coffee cup is topologically equivalent to a doughnut. {cite}`TopologyGif` 
```

In quantum mechanics the topology is often viewed as continuous deformations of the Hamiltonian and providing a gap in the spectrum is not closed then a phase transition does not occur. In this way we have topologically protected states.

## The Quantum Hall Effect

One of the early examples of using topology to explain physical phenomena came in the form of the integer quantum Hall effect. We will introduce it here and focus on the links to topology, but for a more complete overview, see {cite}`DavidTong`.

The integer quantum Hall effect was first measured in 1980 {cite}`IQHE_FirstMeasurement`, with typical experimental results being shown below. 

```{figure} ../../_static/figs/IQHE.svg
:width: 100%
:height: 400

Experimental results for the Integer quantum Hall effect. Figure from {cite}`IQHE_Measurement`
```

The experiments are performed on a two-dimensional semiconducting structure (often referred to as a 2d electron gas, or 2DEG). A voltage is applied in the $x$-direction and then in the presence of a magnetic field, a current is observed in the $y$-direction too. In the integer quantum Hall effect, we find that in a disordered system there are plateaus in the Hall resistance (the resistance in the $y$-direction). These have a height (if we consider resistivity rather than resistance) of 

$$
\rho_{\rm H} = \frac{h}{e^2}\frac{1}{\nu}
$$

where $\nu \in \mathbb{Z}$. The height and positions of these plateaus are robust to disorder (and in fact they even require disorder), as well as the size and geometry of the sample. 

```{note}
Other results in these experiments include
- Initially the Hall resistance is linear in the magnetic field. This region can be explained using the classical Hall effect as we will see shortly.
- The resistance in the $x$-diection peaks when there are jumps in the Hall resistance. For a discussion of this - see {cite}`DavidTong`
```

The robustness of the results to disorder and geometry suggests that topology may be useful in explaining these results, but first let's explore one of the other explanations.

## Classical Hall Effect

Let's begin with a discussion of the classical Hall effect. The setup is similar. We consider a 2d metal with an in-plane electric field and a magnetic field perpendicular, ${\boldsymbol B} = B_z \hat{\boldsymbol z}$ to the sample.

```{figure} ../../_static/figs/HallEffect.svg
:width: 100%
:height: 200

Setup for the classical Hall effect.
```

The equation of motion for the electrons is given by 

$$
m\dot{\boldsymbol v} = -e{\boldsymbol E} - e{\boldsymbol v}\times {\boldsymbol B} - \frac{m {\boldsymbol v}}{\tau}
$$

where the last term is a scattering term, with the scattering rate given by $\tau^{-1}$. In equilibrium, $ \dot{\boldsymbol v} =0$ and we can use that for an electron density of $n$, the current density is given by ${\boldsymbol J}=-ne{\boldsymbol v}=\sigma{\boldsymbol E}$. The conductivity is then a matrix given by

$$
\sigma = \frac{\sigma_0}{1+(\omega_{\rm c}\tau)^2}\left(\begin{matrix} 1 &-\omega_{\rm c}\tau \\ \omega_{\rm c}\tau & 1 \end{matrix}\right)
$$

where $\sigma_0 = ne^2\tau/m$ is the standard Drude conductivity and $\omega_{\rm c} = eB_z/m$ is the cyclotron frequency. We can take the inverse of this matrix to obtain the resistivity, with the Hall resistivity then being given by

$$
\rho_{\rm H}\equiv \rho_{12}=\frac{B}{ne}
$$

This result along with the relationship between the components of $\rho$ and $\sigma$ allow us to explain the first two points reagrding the quantum Hall results we highlighted above. We now need to understand the plateaus and this is done using Landau levels.

## Landau Levels

In this course we won't provide the details of Landau levels but rather summarise some results that allow us to see how we may explain the plateuas observed in quantum Hall.

In the presence of a magnetic field, electrons will perform cyclotron orbits, with a frequency $\omega_{\rm c}$ and will have discrete energy levels given by

$$
E_n = \hbar \omega_{\rm c}(n+\tfrac{1}{2})
$$

This looks like the harmonic oscialltor, however the levels here are highly degenerate, with the number of degenerate levels being given by $N=eB_z L^2/h$. We can break this degeneracy using an electric field

```{figure} ../../_static/figs/LandauLevels.svg
:width: 100%
:height: 200

The degeneracy of the Landau levels is lifted by the presence of an electric field.
```

The velocity associated with these modes is then propotional to the gradient which is given by $-(E_x/B_z)$. Therefore we have

$$
J_y = -nev_y = - \frac{N\nu}{L^2}e\left(-\frac{E_x}{B_z}\right) = \frac{e^2}{h}\nu E_x 
$$

We then find that $\rho_{\rm H} = \rho_{12} =  {h}/(e^2\nu)$, exactly as is observed in the experiments. 

The Landau level picture can be expanded upon in order to explain the importance of disorder too and the robustness of the results. However, for this course we will now turn our focus to topological arguments which can explain this too.

## Topology

In order to understand the quantum Hall effect in terms of topology, it is necessary to introduce a couple of concepts that frequenctly appear in condensed matter, namely the Berry phase and the Chern number. Here, we follow a similar approach to that presented in {cite}`BernevigHughes` and for further details, this book should be consulted.

### Berry Phase 

Let's consider a Hamiltonian that depends on various parameters ${\boldsymbol \lambda} = {\boldsymbol \lambda}(t)$ that vary with time. At a given instant of time the eigenstates are given by

$$
H_{\boldsymbol \lambda} \ket{n_{\boldsymbol \lambda}(t)} = E_{n_{\boldsymbol \lambda}}(t) \ket{n_{\boldsymbol \lambda}(t)}.
$$

If we assume the Hamiltonian is changing adiabatically, that is the parameters are varying sufficiently slowly, then if we start in an eigenstate, we will remain in an eigenstate up to a phase. Therefore, the state to consider is 

$$
\ket{\psi_{n_{\boldsymbol \lambda}}(t)} = \mathrm{e}^{-i\theta(t)}\ket{n_{\boldsymbol \lambda}(t)}.
$$

Substituting this state into the Schrödinger equation and taking the inner product with $\bra{n_{\boldsymbol \lambda}(t)}$ gives a differential equation for the phase $\theta (t)$,

$$
\hbar \partial_t \theta(t) = E_{n_{\boldsymbol \lambda}}(t) - i\hbar \bra{n_{\boldsymbol \lambda}(t)}\partial_t\ket{n_{\boldsymbol \lambda}(t)}.
$$

Integrating with respect to time we find two contributions to the phase $\theta (t) = \varphi (t) - \gamma_n$.The first of these is the standard dynamical phase encountered in untiary evolution

$$
\varphi (t) = \frac{1}{\hbar}\int_0^t E_{n_{\boldsymbol \lambda}}(t') \hspace{5pt} {\rm d}t',
$$

and the second contribution (which is also real so that $\theta$ is just a phase - there is no decay involved) is known as the Berry phase

$$
\begin{aligned}
\gamma_n &= i\int_0^t \bra{n_{\boldsymbol \lambda}(t')}\partial_{t'}\ket{n_{\boldsymbol \lambda}(t')} {\rm d}t' \\ &= i \oint \bra{n_{\boldsymbol \lambda}}\nabla_{\boldsymbol \lambda}\ket{n_{\boldsymbol \lambda}} \cdot {\rm d}{\boldsymbol \lambda}
\end{aligned}
$$

where in the second line we have used that the time dependence of the states originates from the time dependence of ${\boldsymbol \lambda}$ in order to write it in a form where it depends on the path through parameter space but is independent of time. For this reason, the Berry phase is sometimes known as a geometric phase. 

We note here that in the last line the integral is over a closed path in parameter space.  We won't delve into details of the gauge invariance here, but the key point is that the Berry phase can not be removed by a simple gauge transformation for closed paths. 

There are a couple of additional quantities related to the Berry phase that we now introduce. The first is the the Berry Connection (sometimes called the Berry vector potential),

$$
{\boldsymbol A_n}({\boldsymbol \lambda})=i\bra{n_{\boldsymbol \lambda}}\nabla_{\boldsymbol \lambda}\ket{n_{\boldsymbol \lambda}}. 
$$

This is not a gauge invariant quantity but it can be useful to define one, which leads to the Berry connection. In 3-dimensions, this takes the form

$$
{\boldsymbol \Omega_n}({\boldsymbol \lambda}) = \nabla_{\boldsymbol \lambda} \times {\boldsymbol A_n}({\boldsymbol \lambda})
$$

### Chern Number

Using Stokes' theorem we can rewrite the Berry phase as 

$$
\gamma_n = \int_S d{\boldsymbol S}\cdot {\boldsymbol \Omega_n}({\boldsymbol \lambda})
$$

If the surface is a closed two-dimenstional surface, then the integral above is given by $2\pi n$, with $n \in \mathbb{Z}$ due to the Chern/Gauss-Bonnet theorem. 

In condensed matter, a common surface of interest is the 2d Brillouin zone (which is peridioc due to points only being defined up to a lattice vector). Using the above ideas, we can therefore define an integer quantity 

$$
C = \frac{1}{2\pi}\int_{BZ}\Omega({\boldsymbol k}) \hspace{2pt} {\rm d}{\bf k}
$$

where $\Omega({\boldsymbol k}) = \partial_{k_x}A_y({\boldsymbol k}) -  \partial_{k_y}A_x({\boldsymbol k})$. 

This an integer known as the Chern number and only changes when we have a energy gap closing (i.e. a topological phase transition). 

## Topology in integer quantum Hall

The link between the Chern number and the integer quantum Hall effect is often referred to as a TKNN invariant after the authors who discovered it - Thouless, Kohmoto, Nightingale, and den Nijs {cite}`TKNN`. The relation turns out to be remarkably simple, with the Hall conducitivty being given by

$$
\sigma_{12} = \frac{e^2}{h}\sum_n C_n
$$

where the sum is over all filled bands. The Landau levels then have a Chern number of 1 and so we recover the previous results.Since the Chern number is an integer that is robust to perturbations, this explains the robusteness of the quantum Hall results that are observed. 

### Edge Modes
There is also an additional remark we wish to make about this result. This is that a non-zero Chern number corresponds to the presence of gapless edge modes ($C$ of them to be precise) due a result known as the bulk-boundary correspondence. It is easy to see why the quantum Hall system might host these and how they might contribute to the conductivity even in the semiclassical picture. In the bulk of the system we know that we have cyclotron orbits. Now, near the edge of the system, these orbit must give rise to so-called `skipping orbits', which can carry current across the system. Such a result can also be explained in the Landau level picture, but this topological approach makes clear their presence, importance and robustness. We will encounter edge modes further in the coming lectures.


```{figure} ../../_static/figs/SkippingOrbits.svg
:width: 100%
:height: 200

A semiclassical view of the edge modes. Cyclotron modes near the edge of the sample result in modes that propagate along the edge.
```



## Summary

To summarise, we have introduced topological physics in condensed matter and motivated its importance using the integer quantum Hall effect. By defining the Berry phase and Chern number, which are key topics in this field of physics, we were able to explain the robustness of the results that are seen in experiments.

---

## References

```{bibliography}
:filter: docname in docnames
```