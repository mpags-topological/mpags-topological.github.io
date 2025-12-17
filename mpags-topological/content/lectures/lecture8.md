# Lecture 8 - Topological Quantum Field Theory: Fusion and Braiding

Previously, we introduced anyons and discussed at a high-level some of their properties. For instance, we saw that anyons can have non-trivial exchange and mutual statistics, and we introduced the idea of fusion of anyons. In the next two lectures, we will explore these ideas in more detail, and formulate them in the language of topological quantum field theory (TQFT).

The mathematical formulation of anyon models is (2+1)-dimensional topological quantum field theory (TQFT). More preciely, an anyon model is described by a unitary modular tensor category (UMTC), which encodes the fusion and braiding properties of the anyons. While we are not going to define things in full mathematical rigour, we will introduce the key concepts and structures that are used to describe anyon models.

## Anyons

```{figure} ../images/AnyonTypes.svg
---
align: center
width: 60%
name: fig:anyon_types
---
Different anyon types represented as labelled lines. The arrows indicate the direction of time.
```

The first ingredient in our TQFT is the anyon types (otherwise known as topological charges or topological sectors). This is a finite set of labels, which we will denote by $\mathbb{A} = \{1, a, b, c, \ldots\}$. We will draw anyons in diagrams as lines labelled by their anyon type. The label $1$ is reserved for the vacuum anyon, and must always be present in the anyon model. The vacuum anyon has the property that fusing (which we come to shortly) it with any other anyon leaves that anyon unchanged, and that it is its own anti-particle. Each anyon type $a$ has a unique anti-particle $\bar{a}$, such that fusing $a$ and $\bar{a}$ can yield the vacuum anyon. In our diagrams, we will represent the anti-particle of an anyon by reversing the arrow on the line representing that anyon. If an anyon is its own anti-particle, i.e. $\bar{a} = a$ we will simply draw it without an arrow.

## Fusion

Given our anyon labels we can define **fusion rules**, which describe how anyons can combine together. The fusion rules are written as

$$
a \times b = \sum_{c \in \mathbb{A}} N_{ab}^c \, c,
$$

where $N_{ab}^c$ are non-negative integers known as the **fusion coefficients**.

````{admonition} Examples (from previous lecture)

### Toric Code Anyons
The toric code anyons have the following fusion rules:

$$\begin{aligned}
1 \times 1 & = 1  & 1 \times e & = e  & 1 \times m & = m  & 1 \times \epsilon & = \epsilon \\
e \times e & = 1  & e \times m & = \epsilon  & e \times \epsilon & = m \\
m \times m & = 1  & m \times \epsilon & = e \\
\epsilon \times \epsilon & = 1
\end{aligned}$$

### Fibonacci Anyons
Fibonacci anyons have the following fusion rules:

$$ \begin{aligned}
1 \times 1 & = 1 & 1 \times \tau & = \tau \\
\tau \times \tau & = 1 + \tau
\end{aligned} $$


### Ising Anyons
Ising anyons have the following fusion rules:

$$
\begin{aligned}
1 \times 1 & = 1 & 1 \times \sigma & = \sigma & 1 \times \psi & = \psi \\
\sigma \times \sigma & = 1 + \psi & \sigma \times \psi & = \sigma & \psi \times \psi & = 1
\end{aligned}
$$
````

```{note}
It is possible for N_{ab}^c > 1, meaning that there are multiple distinct ways in which anyons a and b can fuse to give anyon c. These extra multiplicities will complicate the following and introduce extra indicies and bookkeeping.For simplicity, we will focus on the case where N_{ab}^c is either 0 or 1.

**Group Analogy:** Fusion multiplicities are similar to what happens for more complicated groups. For instance, in SU(3), the tensor product of two 8-dimensional representations decomposes as 
$$
8 \otimes 8 = 1 \oplus 8 \oplus 8 \oplus 10 \oplus \overline{10} \oplus 27,
$$
where the 8-dimensional representation appears twice on the right-hand side.

```

### Properties of Fusion

To define a tensor category (the core structure underlying TQFTs), the fusion rules must satisfy a number of properties:
- **Commutativity:** Fusion is commutative, i.e.

  $$
  a \times b = b \times a  \quad \Rightarrow \quad N_{ab}^c = N_{ba}^c.
  $$

- **Associativity:** Fusion is associative, i.e.
    $$
    (a \times b) \times c = a \times (b \times c) \quad \Rightarrow \quad \sum_{e \in \mathbb{A}} N_{ab}^e N_{ec}^d = \sum_{f \in \mathbb{A}} N_{af}^d N_{bc}^f.
    $$

- **Vacuum:** The vacuum anyon acts as the identity for fusion, i.e.
    $$
    a \times 1 = a \quad \Rightarrow \quad N_{a1}^b = \delta_{ab}.
    $$

- **Anti-anyons:** Each anyon has a unique anti-particle, such that fusing an anyon with its anti-particle can yield the vacuum anyon, i.e.
    $$
    a \times \bar{a} = 1 + \sum_{c \neq 1} N_{a\bar{a}}^c \, c \quad \Rightarrow \quad N_{a\bar{a}}^1 = 1.
    $$

### Quantum Dimensions

```{figure} ../images/QuantumDimension.svg
---
align: center
width: 60%
name: fig:quantum_dimension
---
```

Each anyon type $a$ has an associated **quantum dimension** $d_a$, which is a positive real number. The quantum dimensions satisfy the relation

$$
d_a d_b = \sum_{c \in \mathbb{A}} N_{ab}^c \, d_c.
$$

For abelian anyons, the quantum dimension is $d_a = 1$, while for non-abelian anyons, $d_a > 1$. The quantum dimension is related to the asymptotic growth of the Hilbert space dimension as more anyons of type $a$ are added. 

## Fusion Diagrams

We can think of fusion rules as specifying the allowed ways that two anyons can fuse or combine. They also allow us to define a state space associated with a set of anyons. We will represent fusion processes using **fusion diagrams**.

```{figure} ../images/FusionDiagram.svg
---
align: center
width: 60%
name: fig:fusion_diagram
---
A fusion diagram showing anyons a and b fusing to form anyon c. A splitting diagram is also shown, where anyon c splits into anyons a and b.
```

We can also use an alternative representation where we take a top-down view of the fusion process, as shown in Figure {numref}`fig:fusion_diagram_topdown`.

```{figure} ../images/FusionDiagramTopDown.svg
---
align: center
width: 60%
name: fig:fusion_diagram_topdown
---
```

For a given set of anyons, we can define a vector space of states associated with that configuration. For example, for two Fibonacci anyons $\tau$, we have two possible fusion channels, corresponding to two states

```{figure} ../images/FibonacciTwoAnyonStates.svg
---
align: center
width: 60%
name: fig:fibonacci_two_anyon_states
---
```

For three Fibonacci anyons, we have three possible fusion diagrams,

```{figure} ../images/FibonacciThreeAnyonStates.svg
---
align: center
width: 60%
name: fig:fibonacci_three_anyon_states
---
```

Importantly here, we have been consistent with the order in which we fuse the anyons.

```{admonition} Exercise:

Given that F(N) = number of diagrams for $N$ anyons, show that F(N) satisfies the Fibonacci recurrence relation
$$
F(N+1) = F(N) + F(N-1),
$$
with initial conditions F(1) = 1 and F(2) = 1.

Therefore, $F(N) \sim \phi^{N} = d_\tau^N$, for large $N$, where $\phi = (1 + \sqrt{5})/2$ is the golden ratio.

Q. What fusion diagrams do we get for $N$ $\sigma$-type Ising anyons?

```
