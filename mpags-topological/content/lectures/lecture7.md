# Lecture 7 - Intoduction to Anyons

## Fermi and Bose Statistics Revisited

All fundamental particles in Nature of one of two types: fermions or bosons. The difference between the two can be neatly summarised by what happends when we exchange a pair of indistinguishable particles.

**For bosons**, the wavefunction is symmetric under exchange:

```{figure} ../images/boson_exchange.svg
---
name: boson_exchange
width: 60%
align: center
---
```

that is, we get exactly the same state when we swap two indistinguishable bosons. 

**For fermions**, on the other hand, the wavefunction is antisymmetric under exchange:

```{figure} ../images/fermion_exchange.svg
---
name: fermion_exchange
width: 60%
align: center
---
```
that is, we pick up a minus sign when we swap two indistinguishable fermions.

This small difference has huge ramifications: Bosons can occupy the same quantum state, leading to phenomena such as Bose-Einstein condensation, superfluidity, and the coherent light of lasers. Fermions, on the other hand, are subject to the Pauli exclusion principle, which follows directly from the antisymmetric nature of their wavefunction. This means that no two fermions can occupy the same quantum state simultaneously. This principle is fundamental to the structure of matter, as it explains the arrangement of electrons in atoms, the behaviour of chemical reactions, and the stability of matter itself.

But why only fermions or bosons? Is there anything else? Let us consider a simple argument for why these are the only two possibilities in three-dimensional space. Let us add a ficticious label to each particle and consider what happens when we exchange two particles twice:

```{figure} ../images/double_exchange.svg
---
name: double_exchange
width: 60%
align: center
---
```

Swapping the particles gives the same state, possibly up to a phase $e^{i\phi}$. Swapping them again must return us to the original state, resulting in a total phase of $e^{i2\phi}$. However, let us change the centre of mass frame to one where particle $a$ is stationary.

```{figure} ../images/double_exchange_cmf.svg
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

```{figure} ../images/mutual_statistics.svg
---
name: mutual_statistics
width: 60%
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



````
