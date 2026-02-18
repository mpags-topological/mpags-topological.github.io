# Introduction to Anyons

In this lecture, we'll introduce more carefully what we mean when we talk about anyons and in future lectures we will look at the underlying theory used to describe them, known as topological quantum field theory. For more details on this topic, the book by Steve Simon is highly recommended {cite}`TopologicalQuantum`.


## Fermi and Bose Statistics Revisited

All fundamental particles in Nature of one of two types: fermions or bosons. The difference between the two can be neatly summarised by what happends when we exchange a pair of indistinguishable particles.

**For bosons**, the wavefunction is symmetric under exchange:

```{figure} ../images/BosonExchange.svg
---
name: boson_exchange
width: 60%
align: center
---
```

that is, we get exactly the same state when we swap two indistinguishable bosons. 

**For fermions**, on the other hand, the wavefunction is antisymmetric under exchange:

```{figure} ../images/FermionExchange.svg
---
name: fermion_exchange
width: 60%
align: center
---
```
that is, we pick up a minus sign when we swap two indistinguishable fermions.

This small difference has huge ramifications: Bosons can occupy the same quantum state, leading to phenomena such as Bose-Einstein condensation, superfluidity, and the coherent light of lasers. Fermions, on the other hand, are subject to the Pauli exclusion principle, which follows directly from the antisymmetric nature of their wavefunction. This means that no two fermions can occupy the same quantum state simultaneously. This principle is fundamental to the structure of matter, as it explains the arrangement of electrons in atoms, the behaviour of chemical reactions, and the stability of matter itself.

But why only fermions or bosons? Is there anything else? Let us consider a simple argument for why these are the only two possibilities in three-dimensional space. Let us add a ficticious label to each particle and consider what happens when we exchange two particles twice:

```{figure} ../images/DoubleExchange.svg
---
name: double_exchange
width: 90%
align: center
---
```

Swapping the particles gives the same state, possibly up to a phase $e^{i\phi}$. Swapping them again must return us to the original state, resulting in a total phase of $e^{i2\phi}$. However, let us change the centre of mass frame to one where particle $a$ is stationary.

```{figure} ../images/DoubleExchangeCMF.svg
---
name: double_exchange_cmf
width: 60%
align: center
---
```

Then, swapping the particles twice is equivalent to moving particle $b$ around a closed loop encircling particle $a$. In three dimensions, we can continuously deform this loop to a point without crossing particle $a$, meaning that the wavefunction must return to its original value (up to some non-universal path dependent phase that we can ignore). That is, this process is *topologically equivalent* to doing nothing. Therefore, we must have $e^{i2\phi} = 1$, which implies that $\phi$ can only be $0$ or $\pi$. This leads us to the conclusion that in three-dimensional space, particles can only be fermions or bosons.

The important part of this argument is the ability to continuously deform the loop in three dimensions. If we instead lived in a two-dimensional world, we could not continuously deform the loop without crossing particle $a$. This opens up the possibility of particles with exchange statistics that are neither fermionic nor bosonic. Such particles are known as **anyons**. 

```{note}
The name "anyon" was coined by Frank Wilczek, who proposed that in two-dimensional systems, particles could exhibit a continuous range of statistical behaviours, interpolating between fermions and bosons. The term reflects the idea that these particles can have "any" phase upon exchange, not limited to the discrete values associated with fermions and bosons. However, in actual fact, not all values are allowed for the exchange phase. 
```

## Exchange and Mutual Statistics

As well as the exchange statistics, in two-dimensions we can also have non-trivial **mutual statistics** between distinguishable particles. Roughly speaking, we have the two following processes

```{figure} ../images/MutualStatistics.svg
---
name: mutual_statistics
width: 95%
align: center
---
```

Where: 
- $\theta_a = e^{ih_a}$ is the topological twist of particle $a$, corresponding to exchanging two identical particles of type $a$.
- $M_{ab} = e^{i\phi_{ab}}$ is the mutual statistics between particles of type $a$ and $b$, corresponding to moving particle $a$ around particle $b$ in a closed loop.

Often this information is summarised in the form of two matrices, the $T$-matrix and the $S$-matrix, where the $T$-matrix contains the topological twists on the diagonal, i.e. $T_{ab} = \theta_a \delta_{ab}$, and the $S$-matrix contains the mutual statistics, $S_{ab} \propto M_{ab}$.

```{note}
$M_{ab}$ is sometimes also called the monodromy between particles $a$ and $b$. There is a simple but non-tivial relationship between $S_{ab}$ and $M_{ab}$. Ultimately, they contain the same information, but are normalised differently.
```

<!--
````{admonition} Examples

### Toric Code

The toric code has four types of anyons $\{1, e, m, \epsilon\}$, with the following $T$ and $S$ matrices:

$$
T = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & -1 \\
\end{pmatrix},
\qquad
S = \frac{1}{2} \begin{pmatrix}
1 & 1 & 1 & 1 \\
1 & 1 & -1 & -1 \\
1 & -1 & 1 & -1 \\
1 & -1 & -1 & 1 \\
\end{pmatrix}
$$

That is, the $e$ and $m$ anyons are bosons with respect to themselves, but have mutual statistics of $-1$ with each other. The $\epsilon$ anyon is a fermion with respect to itself, and has mutual statistics of $-1$ with both $e$ and $m$. You may see it said that the $e$ and $m$ anyons are "mutual semions" (not a term I particularly like).

### Fibonacci Anyons

Fibonacci anyons are an important example of **non-Abelian anyons** (an idea we will return to). There are two types of anyons, the trivial $1$ and the non-trivial $\tau$. Their $T$ and $S$ matrices are given by:

$$
T = \begin{pmatrix}
1 & 0 \\
0 & e^{4\pi i / 5} \\
\end{pmatrix},
\qquad
S = \frac{1}{\sqrt{1 + \phi^2}} \begin{pmatrix}
1 & \phi \\
\phi & 1-\phi \\
\end{pmatrix}
$$

where $\phi = \frac{1 + \sqrt{5}}{2}$ is the golden ratio. Here, the $\tau$ anyon has non-trivial exchange statistics, and the mutual statistics between two $\tau$ anyons is also non-trivial. 

### Ising Anyons

Ising anyons are another important example of non-Abelian anyons, relevant to topological superconductors. There are three types of anyons $\{1, \sigma, \psi\}$, with the following $T$ and $S$ matrices:

$$
T = e^{-i\frac{\pi}{24}}\begin{pmatrix}
1 & 0 & 0 \\
0 & e^{\pi i / 8} & 0 \\
0 & 0 & -1 \\
\end{pmatrix},
\qquad
S = \frac{1}{2} \begin{pmatrix}
1 & \sqrt{2} & 1 \\
\sqrt{2} & 0 & -\sqrt{2} \\
1 & -\sqrt{2} & 1 \\
\end{pmatrix}
$$

The $\sigma$ anyon corresponds to a Majorana fermion and can describe the non-Abelian statistics of Majorana zero modes in $p$-wave topological superconductors.

````
-->


## Fusion

In addition to exchange and mutual statistics, anyons also have a set of rules for how they can combine, or "fuse", together. This is described by the **fusion rules**. For example, in the toric code, we saw that the $e$ and $m$ anyons could combine to form the $\epsilon$ anyon. 

There are two ways to think of fusion:
1. **Particle Perspective**: Two anyons of types $a$ and $b$ can come together to form a new anyon of type $c$. This very similar to the idea of particle - antiparticle annihilation in high-energy physics, except that the resulting particle type is not necessarily the vacuum (trivial) particle.
```{figure} ../images/FusionParticle.svg
---
name: fusion_particle
width: 60%
align: center
---
```


2. **Collective Perspective**: Two anyons of types $a$ and $b$ are brought close together, and we consider the combined system as a whole. The total topological charge of the combined system can be measured, yielding a result of type $c$. They collectively behave as a single anyon of type $c$. This is similar to how a hydrogen atom, consisting of a proton and an electron (fermions), can be treated as a single entity with bosonic properties.
```{figure} ../images/FusionCollective.svg
---
name: fusion_collective
width: 75%
align: center
---
```

We write the fusion rules in the form (for abelian anyons) as 

$$
a \times b = c
$$

meaning that anyons of type $a$ and $b$ fuse to form an anyon of type $c$.

### Multiple Fusion Outcomes: Non-Abelian Anyons

While we have seen the abelian fusion above in the context of the toric code, this can be generalised to allow for multiple possible fusion outcomes. That is, we can have

$$
a \times b = \sum_c N_{ab}^c \, c
$$

where $N_{ab}^c$ is an integer indicating how many ways anyons of type $a$ and $b$ can fuse to form an anyon of type $c$. For instance we could have $a \times b = c + d$, meaning that $a$ and $b$ can fuse to form either $c$ or $d$. 

But what does having multiple fusion channels mean? A good analogy is the combination of two spin-1/2 particles. When we combine two spin-1/2 particles, the possible states can be split into two types: a singlet state with total spin 0, and a triplet state with total spin 1. i.e.

$$
\frac{1}{2} \otimes \frac{1}{2} = 0 \oplus 1
$$

```{note}
When we say there are two channels, the actual state of a pair of anyons can be in a superposition of both channels. This is similar to how two spin-1/2 particles can be in a superposition of the singlet and triplet states. The amplitudes in this superposition will depend on all other anyons in the system!
```

<!--
````{admonition} Examples: Non-abelian fusion

### Fibonacci Anyons
Fibonacci anyons have the following fusion rules:

$$
1 \times 1 = 1 \\
1 \times \tau = \tau \\
\tau \times \tau = 1 + \tau
$$

That is, two $\tau$ anyons can fuse to form either the trivial anyon $1$ or another $\tau$ anyon.

### Ising Anyons

Ising anyons have the following fusion rules:

$$
1 \times 1 = 1 \\
1 \times \sigma = \sigma \\
1 \times \psi = \psi \\
\sigma \times \sigma = 1 + \psi \\
\sigma \times \psi = \sigma \\
\psi \times \psi = 1
$$

That is, two $\sigma$ anyons can fuse to form either the trivial anyon $1$ or the fermionic anyon $\psi$.

````
-->


## Braiding

So far we have looked at the properties of a pair of anyons. When we have more than two, things get more complicated and interesting. With more than two anyons we can introduce "braiding" operations, where we move anyons around each other in specific ways. We will use Fibonacci anyons as an example.

```{note}
Exchange (T) and mutual statistics (S) are special cases of braiding.
```

For Fibonacci anyons we have the following fusion rule

$$
\tau \times \tau = 1 + \tau
$$

meaning there are three possible states for a system of three $\tau$ anyons, depending on how they fuse together. These are 

```{figure} ../images/FibonacciThreeAnyons.svg
---
name: fibonacci_three_anyons
width: 45%
align: center
---
```

Here, we have drawn circles around groups of anyons and indicated the total fusion outcome for that group. We have also labelled these $|0\rangle$, $|1\rangle$, and $|N\rangle$ in relations to quantum computation (more on this later). Let us then consider the following two braids

```{figure} ../images/FibonacciBraids.svg
---
name: fibonacci_braids
width: 70%
align: center
---
```

These braids can be represented as matrices acting on the three-dimensional Hilbert space spanned by the states $|0\rangle$, $|1\rangle$, and $|N\rangle$. If use a matrix-vector notation where

$$
|0\rangle = \begin{pmatrix}1 \\ 0 \\ 0\end{pmatrix}, \quad
|1\rangle = \begin{pmatrix}0 \\ 1 \\ 0\end{pmatrix}, \quad
|N\rangle = \begin{pmatrix}0 \\ 0 \\ 1\end{pmatrix}
$$  

then braid $A$ is represented by the matrix

$$
\begin{pmatrix}
e^{-i4\pi/5} & 0 & 0 \\
0 & e^{i3\pi/5} & 0 \\
0 & 0 & e^{i3\pi/5} \\
\end{pmatrix}
$$

This matrix is diagonal, and its elements correspond to the exchange statistics of the anyons depending on their fusion channel. Braid $B$, on the other hand, is represented by the matrix

$$
\begin{pmatrix}
\phi^{-1} e^{4\pi i / 5} & \phi^{-1/2} e^{-3\pi i / 5} & 0 \\
\phi^{-1/2} e^{-3\pi i / 5} & -\phi^{-1} & 0 \\
0 & 0 & e^{3\pi i / 5} \\
\end{pmatrix}
$$

Importantly, we see that braiding corresponds to unitary matrices and does not simply result in a phase factor. This is a hallmark of non-Abelian anyons, where braiding operations can change the state of the system in a non-trivial way. The name non-abelian is related to the fact that these braiding matrices do not commute with each other, i.e. $AB \neq BA$.

An interesting property of these particular matrices is that they split into a $2\times2$ block acting on the subspace spanned by $|0\rangle$ and $|1\rangle$, and a $1\times1$ block acting on $|N\rangle$. This means that if we restrict ourselves to the subspace spanned by $|0\rangle$ and $|1\rangle$, these braids keep us within that subspace. Furthermore, the matrices on this subspace

$$
\sigma_1 = \begin{pmatrix}
e^{-i4\pi/5} & 0 \\
0 & e^{i3\pi/5} \\
\end{pmatrix},
\qquad
\sigma_2 = \begin{pmatrix}
\phi^{-1} e^{4\pi i / 5} & \phi^{-1/2} e^{-3\pi i / 5} \\
\phi^{-1/2} e^{-3\pi i / 5} & -\phi^{-1} \\
\end{pmatrix}
$$

are sufficient to approximate any $2\times2$ unitary matrix to arbitrary accuracy, in other words they can approximate an arbitrary single qubit gate. By finding the correct sequence of these two braids, we can implement any single qubit gate using Fibonacci anyons! This is the basis of topological quantum computation, which we will return to later in the course.

## Summary

In this session we revisted the statistics of fermions and bosons and showed that other options - anyons - are possible in two dimensions. These anyons can have non-trivial exchange and mutual statistics. We also introduced the concepts of fusion and braiding. We saw that for non-Abelian anyons, braiding can be represented by matrices instead of simple phase factors. In the next two sessions we formalise the ideas that we have introduced here. 

<!--
---

## References

```{bibliography}
:filter: docname in docnames
```

-->