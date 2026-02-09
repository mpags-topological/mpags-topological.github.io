# Lecture 9 - Topological Quantum Computation

In previous sessions, we saw how the braiding of non-abelian anyons results in non-commuting matrices acting on the space of fusion channels. Furthermore, these matrices are unitary. In this session we will show how these braiding operations can be used for quantum computation. Due to the non-local properties of anyons, such operations are expected to be *intrinsically robust* against noise, and this approach to quantum computation is known as **topological quantum computation**.

## Incredibly Brief Overview of Quantum Computation

Since this is not a course on quantum computation, let us very briefly introduce the main ideas at an abstract level. Quantum computation works with quantum states, typically finite-dimensional. In practice, quantum computers are nearly always built out of qubits (two-level systems) and so the total Hilbert space is a $2^N$-dimensional space for $N$ qubits. In the simplest models of quantum computation we then have two types of operations that we can perform: unitary gates and measurements. Unitary gates are unitary operators that act on the Hilbert space, and they are used to manipulate the quantum state. Measurements are typically projective measurements that collapse the quantum state onto a particular basis state, and they are used to extract information from the quantum computer. The goal of quantum computation is to perform a sequence of unitary gates and measurements that allows us to solve a particular problem more efficiently than classical algorithms.

In this section we will show how we can build our state space out of anyons, and how we can perform unitary gates by braiding them. We will briefly discuss how to perform measurements, but will not go into detail of how this might be done in practice. We will also discuss the concept of universality, which is the idea that a particular set of gates is sufficient to perform any quantum computation. More precisely, a set of gates is universal if any unitary operation can be approximated to arbitrary accuracy by a finite sequence of gates from the set.

## Ising Anyons

In this sections we will focus on the Ising anyon model, which is a simple example of a non-abelian anyon model that can be used for topological quantum computation. We choose to focus on this model because it ties together various aspects of this course. It is a particularly important model both in the context of topologically ordered systems but also in the context of topological insulators and superconductors. It is currently one of the most experimentally relevant models in the context of fault-tolerant quantum computation. Unfortunately, it turns out that it is not universal for quantum computation using noise-resiliant operations along, but we will discuss how to achieve universality in this model later on.

```{note}
Another important non-abelian anyon model that we have encountered earlier is the Fibonacci anyon model. This model is universal for quantum computation using braiding alone. It is possible that these anyons may be realised in fractional quantum Hall systems, however, they have not yet been observed or braided in experiments to date.
```

Ising anyons are a set of three anyon types, $\{1, \sigma, \psi\}$, with fusion rules

$$
\begin{aligned}
\sigma \times \sigma &= 1 + \psi \\
\sigma \times \psi &= \sigma \\
\psi \times \psi &= 1
\end{aligned}
$$

Importantly, this model is non-abelian because the fusion of two $\sigma$ anyons can result in two different outcomes, $1$ or $\psi$. The quantum dimension of the $\sigma$ anyon is $d_\sigma = \sqrt{2}$, which means that the Hilbert space of $N$ $\sigma$ anyons grows as $2^{N/2}$. This exponential growth of the Hilbert space is what allows us to encode quantum information in the fusion channels of the anyons. 

The non-trivial F- and R-moves for the Ising anyon model are given by

$$
\begin{aligned}
F^{\sigma\sigma\sigma}_\sigma &= \frac{1}{\sqrt{2}}\left(\begin{matrix}1 & 1 \\ 1 & -1\end{matrix}\right) \\
\left[F^{\psi\sigma\psi}_\sigma\right]_{\sigma\sigma} &= -1 \\
\left[F^{\sigma\psi\sigma}_\psi\right]_{\sigma\sigma} &= -1 \\
R^{\sigma\sigma}_1 &= e^{-i\pi/8} \\
R^{\sigma\sigma}_\psi &= e^{3i\pi/8} \\
R^{\sigma\psi}_\sigma &= -i \\
R^{\psi\psi}_1 &= -1    
\end{aligned}
$$

In the following it will be useful to introduce the following matrices

$$
F = F^{\sigma\sigma\sigma}_\sigma = \frac{1}{\sqrt{2}}\left(\begin{matrix}1 & 1 \\ 1 & -1\end{matrix}\right), \qquad R = \left(\begin{matrix}e^{-i\pi/8} & 0 \\ 0 & e^{3i\pi/8}\end{matrix}\right)
$$

The braids that we will compute can be written in terms of these matrices.


## A Single Qubit

Let us start by considering how to represent a single qubit using Ising anyons, and understanding the gates that we can perform on this qubit by braiding. On its own, a single qubit is not particularly useful, but looking at this simple case first will simplify the discussion when we move on to multiple qubits later on.

### States

To represent a single qubit, we can use four $\sigma$ anyons. The total fusion outcome of these four anyons is the identity anyon $1$. We will then work in a basis where we fuse the first two anyons together, and the last two anyons together, as shown in {numref}`fig:single_qubit_states`. Because of the fusion rules, these two fusion channels must be the same and can be either $1$ or $\psi$, giving us our two states. We can then identify the state where both fusion channels are $1$ as the logical $|0\rangle$ state, and the state where both fusion channels are $\psi$ as the logical $|1\rangle$ state. In this way we have encoded a single qubit in the fusion channels of four $\sigma$ anyons. In {numref}`fig:single_qubit_states` we show both the top-down and the diagrammatic representation of these states.

```{figure} ../images/SingleQubitStates.svg
---
name: fig:single_qubit_states
width: 70%
align: center
---
States ...
``` 


### Braids

Now that we have defined our states, we can look at the braids that we can perform on these anyons. Since we have four anyons, any braid can be generated by the three elementary braids that exchange anyons $1$ and $2$, anyons $2$ and $3$, and anyons $3$ and $4$. 

```{figure} ../images/SingleQubitBraids.svg
---
name: fig:single_qubit_braids
width: 70%
align: center
---
Top down view of the braids...
``` 


**Braid 1 $\leftrightarrow$ 2:** When we exchange anyons $1$ and $2$, we can directly apply the R-move to get the braid operator. The phase accumulated on the $|0\rangle$ state is $e^{-i\pi/8}$, and the phase accumulated on the $|1\rangle$ state is $e^{3i\pi/8}$. Therefore the braid operator for this exchange is given by the $R$ matrix defined above. Up to an overall phase of $e^{-i\pi/8}$, this is the $S$ gate in quantum computation, i.e.,

$$
B_{12} = e^{-i\pi/8}\left(\begin{matrix}1 & 0 \\ 0 & i\end{matrix}\right) = e^{-i\pi/8} S.
$$  

The $S$ gate is the square root of the $Z$ Pauli gate.

**Braid 3 $\leftrightarrow$ 4:** By symmetry, the braid operator for exchanging anyons $3$ and $4$ is the same as the braid operator for exchanging anyons $1$ and $2$, so we have

$$
B_{34} = e^{-i\pi/8} S.
$$

**Braid 2 $\leftrightarrow$ 3:** This braid is a bit more complicated because anyons $2$ and $3$ are not fused together in our chosen basis. To compute this braid operator, we first need to change basis using the F-move so that anyons $2$ and $3$ are fused together. We can then apply the R-move to exchange them, and finally use the F-move again to return to our original basis. More explicitly, we have

```{figure} ../images/SingleQubitH.svg
---
name: fig:single_qubit_H
width: 70%
align: center
---
``` 

In terms of the $F$ and $R$ matrices defined above, this braid operator is given by

$$
B_{23} = F^{-1} R F = \frac{e^{-i\pi/8}}{2}\left(\begin{matrix}1+i & 1-i \\ 1-i & 1+i\end{matrix}\right) = e^{i\pi/8} \sqrt{X}
$$

where $\sqrt{X}$ is the square root of the $X$ Pauli gate. This gate is related to an important gate in quantum computation known as the Hadamard gate, which is related via the relation $H = S \sqrt{X} S$. 

In total then, we can realise the $S$ and $\sqrt{X}$ gates, and any combinations and inverses thereof, by braiding our anyons. Unfortunately, these gates are not universal. There exist single qubit gates that we cannote approximate to arbitrary accuracy by braiding, and therefore we cannot perform arbitrary single qubit operations by braiding alone. The set of gates that we can perform by braiding is known as the Clifford group. We will return to the question of how to achieve universality in this model later on, but for now let us move on to multiple qubits and see what gates we can perform there.

```{note}
The Clifford group is the group of gates that transform Pauli operators to Pauli operators. On a single qubit, the Clifford group is generated by the Hadamard gate and the S gate, and it also includes the Pauli gates. The Clifford group is not universal for quantum computation, but it is an important subgroup of the unitary group that has many applications in quantum error correction and other areas of quantum information. Importantly, the Clifford group can be efficiently simulated on a classical computer.
```

## Multiple Qubits

Let us now consider the case of multiple qubits. For concretenes, we will focus on the case of two qubits and leave the generalisation to more qubits as an exercise.

### States

There are different ways to encode multiple qubits using anyons, and the choice of encoding can affect the gates that we can perform by braiding. One common encoding is the **sparse encoding**, where we use four $\sigma$ anyons for each qubit. However, we cannot generate entangling gates between these qubits using braiding along in this encoding, but they can instead be generated by measurements. Another common encoding, and the one we will consider, is the **dense encoding**. This uses 2 $\sigma$ anyons per qubit, and an additional pair of $\sigma$ anyons to ensure that the total fusion outcome is the identity anyon $1$. For the case of two qubits, this requires a total of six $\sigma$ anyons. In this encoding, we can generate entangling gates by braiding alone, and therefore we can achieve universality by braiding alone in this encoding. 

```{figure} ../images/TwoQubitStates.svg
---
name: fig:two_qubit_states
width: 70%
align: center
---
Two qubits...
```

The general fusion diagram for these six $\sigma$ anyons is shown in {numref}`fig:two_qubit_states`. The total fusion outcome of all six anyons is fixed to the identity anyon $1$. We are then left with four fusion channels that can be either $1$ or $\psi$. However, not all of these fusion channels are independent. The total fusion channel being $1$ means that $d$ and $c$ must be the same. Furthermore, we have that $d = a \times b$. This leave use with two independent fusion channels, resulting in a four-dimensional Hilbert space that can encode two qubits. We can then identify the logical states as follows:

```{figure} ../images/TwoQubitLogicalStates.svg
---
name: fig:two_qubit_logical_states
width: 70%
align: center
---
```

We can think of $a$ labelling the state of the first qubit, $c$ labelling the state of the second qubit, and $b$ is the parity bit that ensures that the total fusion outcome is $1$.


### Braids

