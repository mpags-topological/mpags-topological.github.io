# Lecture 6 - The Toric Code

The toric code is a beautifually simple model for topological order introduced by Alexei Kitaev. It is simple, soluble, and contains many of the key features of more general topologically ordered systems. In particular, it has anyonic excitations and ground state degeneracy that depends on the topology of the underlying manifold. We introduce it here as a key example of topological order, and to motivate the more formal theory of anyons that will follow.

## The Model

The toric code is a system of spin-1/2 degrees of freedom living on the bonds of a square lattice, and is defined by the Hamiltonian

$$
H = -J_e \sum_s A_s - J_m \sum_p B_p,
$$

where the sums are over the stars $s$ (vertices) and plaquettes $p$ (faces) of the lattice, as shown in {numref}`fig:toric_code`. The operators $A_s$ and $B_p$ are defined as

$$
A_s = \prod_{i \in s} \sigma_i^z, \quad B_p = \prod_{i \in p} \sigma_i^x,
$$  

with the products running over the four spins adjacent to the star $s$ or around the plaquette $p$. Here, $\sigma_i^x$ and $\sigma_i^z$ are the Pauli matrices acting on the spin at bond $i$. We define the model with periodic boundary conditions, i.e., we put it on a torus (hence the name). The parameters $J_e$ and $J_m$ are positive coupling constants. The subscripts $e$ and $m$ stand for "electric" and "magnetic", corresponding to the types of excitations in the model (which we will revisit later), and the naming comes from the context of lattice gauge theory.

```{figure} ../images/ToricCode.pdf
---
name: fig:toric_code
width: 85%
align: center
---

Caption for toric code...
``` 

The simplicity of the toric code arises from the fact that all the $A_s$ and $B_p$ operators in the Hamiltonian commute with each other, allowing for an exact solution of the model. That is,

$$
[A_s, A_{s'}] = 0, \quad [B_p, B_{p'}] = 0, \quad [A_s, B_p] = 0, 
$$

for all stars $s, s'$ and plaquettes $p, p'$. The first two commutators are trivial and boil down to $[\sigma_i^z, \sigma_j^z] = 0$ and $[\sigma_i^x, \sigma_j^x] = 0$. The third commutator is less trivial. First, note that if the star $s$ and plaquette $p$ do not share any spins, then the corresponding operators obviously commute. Otherwise, they share exactly two spins. On those shared spins, we have anti-commutations between $\sigma^z$ and $\sigma^x$ on the same site, i.e. $\sigma^z \sigma^x = - \sigma^x \sigma^z$. Since there are two such shared spins, we get two minus signs when commuting $A_s$ and $B_p$, resulting in an overall commutation. Thus, $[A_s, B_p] = 0$

Since all the terms in the Hamiltonian commute, we can simultaneously diagonalise them. The eigenvalues of each $A_s$ and $B_p$ operator are $\pm 1$, since they are products of four Pauli matrices. Therefore, the ground state of the toric code is the state that satisfies

$$
A_s \ket{\psi_0} = \ket{\psi_0}, \quad B_p \ket{\psi_0} = \ket{\psi_0},
$$ (eq:tc_gs_conditions)

for all stars $s$ and plaquettes $p$. This means that in the ground state, all star and plaquette operators have eigenvalue +1. These equations will allow us to construct the ground state explicitly. Furthermore, we know exactly the full spectrum of the Hamiltonian. Each time a star or plaquette operator has eigenvalue -1, it contributes an energy of $2J_e$ or $2J_m$ respectively to the total energy. 

## Ground State Degeneracy

So far so good, but where does topology come in? Let us consider the Hamiltonian a bit more carefully and count the number of independent constraints imposed by the ground state conditions in Eq.{eq}`eq:tc_gs_conditions`. Say our system consists of $N_x \times N_y$ vertices (stars). Since the spins live on the bonds, there are $2N_x N_y$ spins in total. This means our Hilbert space has dimension $2^{2N_x N_y}$. We also have $N_x N_y$ star operators and $N_x N_y$ plaquette operators, giving a total of $2N_x N_y$ constraints. However, due to the periodic boundary conditions, not all of these contraints are independent. Specifically, we have the relations

$$
\prod_{\text{all } s} A_s = \mathbb{I}, \quad \prod_{\text{all } p} B_p = \mathbb{I},
$$

We therefore only have $2N_x N_y - 2$ independent constraints. Each independent constraint halves the dimension of the ground state subspace, so the ground state degeneracy is

$$
\text{Degeneracy} = 2^{2N_x N_y - (2N_x N_y - 2)} = 4.
$$

We have a four-fold degenerate ground state! 

This ground state degeneracy is directly related to the boundary conditions and is a hallmark of topological order. The order of the degeneracy depends on the topology of the underlying manifold. For a torus, we have found a four-fold degeneracy. If we were to put the system on a surface of genus $g$ (i.e., with $g$ "holes"), the ground state degeneracy would be $4^g$. This dependence on topology is a key feature of topologically ordered systems.

## Explicit form of the Ground States

Since we can solve the toric code exactly, we can write down explicit forms for the ground states. To do so, let us work in a particular basis. We choose the $\sigma^z$ basis, where each spin is either up ($\sigma^z\ket{\uparrow} = \ket{\uparrow}$) or down ($\sigma^z\ket{\downarrow} = -\ket{\downarrow}$) along the $z$-axis. We denote this graphically by using thin black lines for spins in the $\ket{\uparrow}$ state and thick black lines for spins in the $\ket{\downarrow}$ state, that is

```{figure} ../images/GSBasis.pdf
---
name: fig:toric_code
width: 85%
align: center
---
```

### Star operators

Let us first consider the action of the star operators $A_s$. Recall that $A_s$ is the product of $\sigma^z$ operators on the four spins adjacent to the star $s$. Therefore, $A_s$ measures the parity of the number of down spins around the star. If there is an even number of down spins, $A_s$ has eigenvalue +1; if there is an odd number, it has eigenvalue -1. Thus, the ground state condition $A_s \ket{\psi_0} = \ket{\psi_0}$ requires that there be an even number of down spins around each star. That is, in the ground state, we can only have 
```{figure} ../images/StarAllowed.pdf
---
name: fig:StarAllowed
width: 60%
align: center
---
```
and not
```{figure} ../images/StarNotAllowed.pdf
---
name: fig:StarNotAllowed
width: 60%
align: center
---
```
Therefore, any configuration in the ground state must consist of closed loops of down spins on the lattice. For example, the following configuration is allowed in the ground state:
```{figure} ../images/StarGSExample.pdf
---
name: fig:StarGSExample
width: 60%
align: center
---
```

### Plaquette operators

In the Z-basis, the plaquette operators flip all spins aroudn the plaquette, e.g.,
```{figure} ../images/PlaquetteExample.pdf
---
name: fig:plaquette_example
width: 60%
align: center
---
```
To have $B_p|\psi_0\rangle = |\psi_0\rangle$, this means if a particular configuation appears in $|\psi_0\rangle$, then the configuration with a plaquette flipped is also in $|\psi_0\rangle$ with the same amplitude. Therefore, the ground state is an equal superposition of all closed loop configurations that can be reached from one another by flipping plaquettes. E.g., 
```{figure} ../images/PlaquetteGSExample.pdf
---
name: fig:PlaquetteGSExample
width: 60%
align: center
---
```

It looks like we've found the ground state, but what about the four-fold degeneracy? To understand this consider the following four spin configurations, labelled $|\Phi_i\rangle$, $i = 0, 1, 2, 3$:
```{figure} ../images/GSReferenceConfigs.pdf
---
name: fig:GSDegeneracy
width: 80%
align: center
---
```
It is not possible to go from one of these configurations to another by flipping plaquettes. Therefore, the ground state must be a superposition of all closed loop configurations that can be reached from each of these four "reference" configurations by flipping plaquettes. These states are characterised by even or odd winding around the two directions of the torus. The four ground states $|\psi_i\rangle$, with $i=0,1,2,3$, can therefore be written as

$$
|\psi_i\rangle = \prod_p \frac{1 + B_p}{\sqrt{2}} |\Phi_i\rangle, \quad i = 0, 1, 2, 3.
$$

## Wilson Loop Operators

```{figure} ../images/WilsonStrings.pdf
---
name: fig:wilson_strings
width: 85%
align: center
---
Caption...
```

Given that we have a four-fold degenerate ground state, it is natural to ask how we can distinguish between these states. One way to do this is to introduce Wilson loop operators, which are non-local operators that measure the winding of spins around the torus. Let us introduce the operators

$$
W^v_z = \prod_{i \in \gamma_v} \sigma_i^z, \quad W^h_z = \prod_{i \in \gamma_h} \sigma_i^z,
$$

where $\gamma_v$ and $\gamma_h$ are any non-contractible paths on the *dual lattice* that wind an odd number of times around the vertical and horizontal directions of the torus, respectively. See Fig.{numref}`fig:wilson_strings` for examples of such paths. These operators commute with the star and plaquette operators, and therefore with the Hamiltonian. They also commute with each other. Their eigenvalues $\pm 1$ completely resolve the four-fold degeneracy of the ground state. Specifically, we have

$$
\begin{aligned}
W^v_z |\psi_0\rangle &= |\psi_0\rangle, & W^h_z |\psi_0\rangle &= |\psi_0\rangle, \\
W^v_z |\psi_1\rangle &= |\psi_1\rangle, & W^h_z |\psi_1\rangle &= -|\psi_1\rangle, \\
W^v_z |\psi_2\rangle &= -|\psi_2\rangle, & W^h_z |\psi_2\rangle &= |\psi_2\rangle, \\
W^v_z |\psi_3\rangle &= -|\psi_3\rangle, &\quad W^h_z |\psi_3\rangle &= -|\psi_3\rangle.
\end{aligned}
$$

The plus and minus signs correspond to the even and odd winding of the reference configurations $|\Phi_i\rangle$ around the torus, perpendicular to the direction of the Wilson loop operator.

We could have equally chosen two other Wilson loop operators defined in terms of $\sigma^x$ operators:

$$
W^v_x = \prod_{i \in C_v} \sigma_i^x, \quad W^h_x = \prod_{i \in C_h} \sigma_i^x,
$$

where $C_v$ and $C_h$ are any non-contractible paths on the lattice that wind an odd number of times around the vertical and horizontal directions of the torus, respectively. See Fig.{numref}`fig:wilson_strings` for examples of such paths. These operators also commute with the Hamiltonian and with each other, but they do not commute with the previous Wilson loop operators. We can distinguish the ground states using any commuting pair of $\{W^v_z, W^h_z, W^v_x, W^h_x\}$.

```{note}
There are no **local** operators that can distinguish between the four ground states. We need **non-local** operators like the Wilson loop operators to do so. This is another hallmark of topological order. There is said to be a topological ground state degeneracy. An important consequence of this is that local perturbations to the Hamiltonian cannot lift the ground state degeneracy, making it robust against local noise. More precisely, any local operator can at most cause energy splittings that are exponentially small in the system size.
```

## Anyons

Let us now turn to the excitations of the toric code. Here we will encounter one of the most remarkable aspects of topologically ordered systems: anyons. In the remaining lectures, we will develop a more formal theory of anyons. 

Let us apply a $\sigma^z$ operator to a single spin in the ground state. This has the effect of flipping the eigenvalue of the two adjacent plaquette operators from +1 to -1. These plaquettes with $B_p = -1$ correspond to local excitations, each costing energy $2J_m$. We call these excitations "magnetic" excitations by convention, and denote them by $m$. 

```{figure} ../images/AnyonCreation.pdf
---
name: fig:anyons_creation
width: 85%
align: center
---
This can be a combined figure with star and plaquette excitations, including the Wilson string operators. 
```

We can then move these excitations around by applying further $\sigma^z$ operators to adjacent spins. If the operators acts on a spin adjacent to one of the excitations, it will move the excitation to the other plaquette adjacent to that spin without costing any additional energy. By applying a string of $\sigma^z$ operators along a path on the lattice, we can create a pair of $m$ excitations at the endpoints of the path and move them around. See Fig.{numref}`fig:anyons_creation` for an illustration.

We can define open **Wilson string operators** that create and move these excitations. For a path $\gamma$ on the dual lattice, we define

$$
W^z(\gamma) = \prod_{i \in \gamma} \sigma_i^z.
$$

The operator created a pair of magnetic (plaquette) excitations at the endpoints of the path $\gamma$, or moves existing excitations if they are already present at the endpoints. Note that the Wilson loop operators we defined earlier are special cases of these string operators, where the path winds around the torus and has no endpoints, thus creating no excitations.

Similarly, we can define the electric Wilson string operators

$$
W^x(C) = \prod_{i \in C} \sigma_i^x,
$$

where $C$ is a path on the lattice. These operators create and move "electric" (star) excitations, which we denote by $e$. 

```{note}
The Wilson string operators are explicitly defined in terms of a given path $\gamma$ or $C$. However, the excitations they create at the endpoints do not depend on the specific path taken, only on the endpoints themselves. More precisely, two Wilson string operators defined on different paths with the same endpoints may be related by multiplication with plaquette or star operators, and if there are no excitations in the region between the two paths, these operators act identically on the state.
```


