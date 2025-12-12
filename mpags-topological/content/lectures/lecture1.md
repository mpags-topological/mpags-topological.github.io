# Lecture 1 - Introduction to Topology in Condensed Matter Physics

In this course, we aim to give an overview of many different aspects of topology in condensed matter physics. We hope to show the its importance in this area of physics and why it is an active research field. We will begin in this lecture by demonstrating the usefulness of a topological description and how it can be used to explain robust phenomena. To do this we will explore the integer quantum Hall effect. However, first we wish to introduce why we may wish to study topological phases.

## Topological Phases of Matter - An Overview

The role of topology in condensed matter physics has been a key area of research in recent years with a key motivator being the desire to further our classification of phases of matter. 'Traditional' phases of matter are characterised by a local order parameter which we can use to identify the phase. Transitions to more ordered states then involve the breaking of a symmetry. This is the Ginzburg-Landau theory of spontaneous symmetry breaking and underpins many of the phase transitions we are familiar with - for example, magnetisation, superconductors and the water phase diagram.

<img src="../../_static/figs/SSB.svg" width="100%" height="400"></img>

However not all phases of matter are characterised by a local parameter, examples of which are the topological phases that will be discussed in this course (as well as those that go beyond the scope of these introductory lectures). In particular we will consider three classes
 
- Free fermions
- SPT
- Topologically ordered states

A simplistic view of a topological state is that it remains the same under continuous deformations - the classic example is that a coffee cup is the same as a doughnut, with the characterisation being that they have the same number of holes.

<img src="../../_static/figs/CoffeeCup_Doghnut.gif" width="100%" height="400"></img>

In quantum mechanics the topology is often viewed as continuous deformations of the Hamiltonian and providing a gap in the spectrum is not closed then a phase transition does not occur. In this way we have topologically protected states.

## The Quantum Hall Effect

One of the classic examples when introducing topology in condensed matter physics is the quantum Hall effect, so it would be wrong to leave it out here.


<img src="../../_static/figs/IQHE.svg" width="100%" height="400"></img>

Let's begin with a discussion of the classical Hall effect

$$
\sigma = 
$$



An alternative way of understanding the integer quantum Hall effect is through topology.

## Berry Phase and Topological Invariants
As we emphasised in the introduction, this course will not focus on the mathematical field of topology, however there are number of related concepts that appear in condensed matter and here we aim to introduce a couple of them.

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

An additional comment is that the integral is over a closed path. We won't delve into details of the gauge invariance here, but the essential point is that the Berry phase can not be removed by a simple gauge transformation for closed paths, but rather it is modified by an integer$\times 2\pi$. 


In addition to the Berry phase, there are a couple of other quantities that are useful to be aware of. The first is the the Berry Connection (sometimes called the Berry vector potential),
$$
{\boldsymbol A_n}({\boldsymbol \lambda})=i\bra{n_{\boldsymbol \lambda}}\nabla_{\boldsymbol \lambda}\ket{n_{\boldsymbol \lambda}}. 
$$

This is not a gauge invariant quantity but it can be useful to define one, which leads to the Berry connection. In 3-dimensions, this takes the form

$$
\Omega_n({\boldsymbol \lambda}) = \nabla_{\boldsymbol \lambda} \times {\boldsymbol A_n}({\boldsymbol \lambda})
$$

## Returning to Quantum Hall

In condensed matter, a common surface of interest is the 2d Brillouin zone (which is peridioc due to points only being defined up to a lattice vector). Using the above ideas, we define a topological invariant

$$
C = \frac{1}{2\pi}\int_{BZ}\Omega({\boldsymbol k}) \hspace{2pt} {\rm d}{\bf k}
$$

where $\Omega({\boldsymbol k}) = \partial_{k_x}A_y({\boldsymbol k}) -  \partial_{k_y}A_x({\boldsymbol k})$. 

This an integer known as the Chern number and only changes when we have a energy gap closing (i.e. a topological phase transition). TALK ABOUT THE CHERN NUMBER BEING OVER FULL BANDS AS THE SUM OVER ALL BANDS IS ZERO.

Now, it can be shown that the conductance in the QHE can be expressed in terms of the Chern number

$$
\sigma = 
$$

A natural question to ask is why a current that is characterisitc of the edge modes in the system can be characterised by the Chern number which is a bulk property of the system (remember that the Brillouin zone is periodic in the calculation of the Chern number). Well, the solution to this is a principle known as the bulk-boundary correspondence. This states that


