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

So far so good, but where does topology come in? Let us consider the Hamiltonian a bit more carefully and count the number of independent constraints imposed by the ground state conditions in Eq.{eq}`eq:tc_gs_conditions`. 