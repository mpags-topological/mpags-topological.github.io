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

To represent a single qubit, we can use four $\sigma$ anyons. The total fusion outcome of these four anyons is the identity anyon $1$. We will then work in a basis where we fuse the first two anyons together, and the last two anyons together, as shown in Fig.XXX. Because of the fusion rules, these two fusion channels must be the same and can be either $1$ or $\psi$, giving us our two states. We can then identify the state where both fusion channels are $1$ as the logical $|0\rangle$ state, and the state where both fusion channels are $\psi$ as the logical $|1\rangle$ state. In this way we have encoded a single qubit in the fusion channels of four $\sigma$ anyons.


### Braids

Now that we have defined our states, we can look at the braids that we can perform on these anyons. Since we have four anyons, any braid can be generated by the three elementary braids that exchange anyons $1$ and $2$, anyons $2$ and $3$, and anyons $3$ and $4$. 