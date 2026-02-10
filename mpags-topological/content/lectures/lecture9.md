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
width: 75%
align: center
---
Definition of the two states of a single qubit encoded in four $\sigma$ anyons with trivial total topological charge. The top-down view is shown on the left, and the diagrammatic representation is shown on the right.
``` 


### Braids

Now that we have defined our states, we can look at the braids that we can perform on these anyons. Since we have four anyons, any braid can be generated by the three elementary braids that exchange anyons $1$ and $2$, anyons $2$ and $3$, and anyons $3$ and $4$. 

```{figure} ../images/SingleQubitBraids.svg
---
name: fig:single_qubit_braids
width: 95%
align: center
---
The three elementary braids that we can perform on our single qubit. All other braids can be generated by combinations of these three and their inverses.
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
width: 85%
align: center
---
The general state of our six $\sigma$ anyons encoding two qubits. Left shows the top-down view, and right shows the diagrammatic representation. The four fusion channels $a, b, c, d$ can be either $1$ or $\psi$, but they are not all independent (see main text).
```

The general fusion diagram for these six $\sigma$ anyons is shown in {numref}`fig:two_qubit_states`. The total fusion outcome of all six anyons is fixed to the identity anyon $1$. We are then left with four fusion channels that can be either $1$ or $\psi$. However, not all of these fusion channels are independent. The total fusion channel being $1$ means that $d$ and $c$ must be the same. Furthermore, we have that $d = a \times b$. This leave use with two independent fusion channels, resulting in a four-dimensional Hilbert space that can encode two qubits. We can then identify the logical states as follows:

```{figure} ../images/TwoQubitLogicalStates.svg
---
name: fig:two_qubit_logical_states
width: 45%
align: center
---
```

We can think of $a$ labelling the state of the first qubit, $c$ labelling the state of the second qubit, and $b$ is the parity bit that ensures that the total fusion outcome is $1$.


### Braids

Let us now look at the five elementary braids that we can perform on these six anyons. 

**Braid 1 $\leftrightarrow$ 2:** This simply applies the R-move to the first two anyons, giving $R^{\sigma\sigma}_a$, which is the same as the braid operator for exchanging anyons $1$ and $2$ in the single qubit case. Therefore this braid applies the $S$ gate (up to a phase) to the first qubit and leaves the second qubit unchanged.

**Braid 5 $\leftrightarrow$ 6:** For the same reasons this braid applies the $S$ gate to the second qubit and leaves the first qubit unchanged.

**Braid 2 $\leftrightarrow$ 3:** To figure out this braid, we first need to change basis using an F-move, that is

```{figure} ../images/TwoQubitBraid23.svg
---
name: fig:two_qubit_braid_23
width: 75%
align: center
---
```

This F-move is trivial, that is $\left[F^{\sigma\sigma b}_c\right]_{a\sigma} = 1$. The remaining diagram on the right (highlighted in blue) is the same one we encountered in the single qubit case. The braid on $2$ and $3$ is then independent of $c$ and gives us the same $\sqrt{X}$ gate on the first qubit as in the single qubit case, while leaving the second qubit unchanged.

**Braid 4 $\leftrightarrow$ 5:** For this braid, we first need to change basis using an F-move. However, this F-move is trivial and is essentially a redrawing of the diagram, that is

```{figure} ../images/TwoQubitBraid45.svg
---
name: fig:two_qubit_braid_45
width: 65%
align: center
---
```

Then by symmetry the braid on $4$ and $5$ is the similar to the braid on $2$ and $3$, giving us the $\sqrt{X}$ gate on the second qubit while leaving the first qubit unchanged.

**Braid 3 $\leftrightarrow$ 4:** So far, the braids we have considered have reproduced the single qubit gates on each qubit independently. This final braid is more interesting because it can generate an entangling gate between the two qubits. It is simply given by the R-move 

$$
B_{34} = R^{\sigma\sigma}_b = R^{\sigma\sigma}_{a\times c} = \left(\begin{matrix} e^{-i\pi/8} & 0 & 0 & 0 \\ 0 & e^{3i\pi/8} & 0 & 0 \\ 0 & 0 & e^{3i\pi/8} & 0 \\ 0 & 0 & 0 & e^{-i\pi/8}\end{matrix}\right)
$$

This is an entangling gate because the phase accumulated depends on the state of both qubits. This matrix cannot be written as a Kronecker product of two single qubit gates, i.e. it is not a product of single qubit gates. This gate can be written as $B_{34} = e^{i\pi/8} \exp\left(-i\frac{\pi}{4} Z\otimes Z\right)$. By combining this gates with single qubit gates, we can generate a CZ (controlled-Z) gate,

$$
B_{34} B^{-1}_{12} B^{-1}_{56} \propto CZ.
$$

Furthermore, using the Hadamard gate we can generate a CNOT (controlled-NOT) gate. Any of these threee entangling gates is as good as any other since they are related by single qubit gates. A standard chosen set of generating gates that we can implement by braiding is $\{S, H, CNOT\}$. 


## Measurement

The final ingredient we need for quantum computation is measurement. The simplest type of projective measurement is to bring a pair of $\sigma$ anyons close together and measure the total fusion outcome. That is, measure whether there is a fermion in that regions ($\psi$) or not ($1$). This is a projective measurement because it collapses the state of the system onto a particular fusion channel. How the measurement is performed in practice depends on the physical system that we are working with, and we will not go into details of this here. However, it is important to note that this measurement is topologically protected because the fusion outcome is a global property of the system that cannot be changed by local perturbations. Therefore, this measurement is robust against noise and errors, which is one of the key advantages of topological quantum computation.


## Universality

While we will not consider the general case of $N$ qubits here, we can show that all gates that we can perform by braiding in the dense encoding of $N$ qubits are generated by the set $\{S, H, CNOT\}$. This is not a universal set of gates. This generates the Clifford group on $N$ qubits, which is a finite subgroup of the unitary group. Therefore we cannot perform arbitrary unitary operations by braiding alone in this model. 

To achieve universality, we only need to add one additional gate that is outside of the Clifford group. A common choice is the $T$ gate, which is given by

$$
T = \left(\begin{matrix}1 & 0 \\ 0 & e^{i\pi/4}\end{matrix}\right)
$$

This gate can be implemented by bringing a pair of $\sigma$ anyons close together, making them interact (resulting in an energy splitting between the $1$ and $\psi$ fusion channels), and then separating them again after a certain amount of time. By tuning the amount of time that the anyons are close together, we can implement the $T$ gate. However, this operation is analogue, and is not topologically protected. By bringing the anyons close together, local noise can cause errors in the implementation of the $T$ gate. Therefore, while we can achieve universality by adding this gate, we lose the topological protection for this gate, and therefore we lose the intrinsic robustness against noise for this gate.

One approach to circumvent this issue is to use a technique known as **magic state distillation**. The idea is to prepare a special state, known as a magic state by applying unprotected operations to a state that we can prepare using topologically protected operations. This will result in a noisy magic state. If we then make many versions of this noisy magic state, we can use the topologically protected operations, combined with measurements, to create a single higher quality magic state. This process can be repeated to create magic states of arbitrarily high quality. Given this high quality magic state, we can then use it to implement the $T$ gate in a fault-tolerant way through a combination of topologically protected operations and measurements. This allows us to achieve universality while maintaining the intrinsic robustness.


## Summary

Bringing together all the aspects of TQFT that we have learnt in this course, we have seen how the braiding of non-abelian anyons can be used to perform quantum computation. We have focussed on the Ising anyon model, which is one of the simplest and most experimentally relevant cases. We have seen how to encode qubits in the fusion channels of the anyons, and how to perform gates by braiding them. We have also discussed how to perform measurements, and how to achieve universality by adding an additional gate that is not topologically protected. 


<!--
---

## References

```{bibliography}
:filter: docname in docnames
```

-->