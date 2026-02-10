# Lecture 7 - Topological Quantum Field Theory: Fusion and Braiding

Previously, we introduced anyons and discussed at a high-level some of their properties. For instance, we saw that anyons can have non-trivial exchange and mutual statistics, and we introduced the idea of fusion of anyons. In the next two lectures, we will explore these ideas in more detail, and formulate them in the language of topological quantum field theory (TQFT).

The mathematical formulation of anyon models is (2+1)-dimensional topological quantum field theory (TQFT). More preciely, an anyon model is described by a unitary modular tensor category (UMTC), which encodes the fusion and braiding properties of the anyons. While we are not going to define things in full mathematical rigour, we will introduce the key concepts and structures that are used to describe anyon models.

## Anyons

```{figure} ../images/AnyonTypes.svg
---
align: center
width: 65%
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
It is possible for $N_{ab}^c > 1$, meaning that there are multiple distinct ways in which anyons a and b can fuse to give anyon c. These extra multiplicities will complicate the following and introduce extra indicies and bookkeeping.For simplicity, we will focus on the case where $N_{ab}^c$ is either 0 or 1.

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
width: 30%
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
width: 50%
name: fig:fusion_diagram
---
A fusion diagram showing anyons a and b fusing to form anyon c. A splitting diagram is also shown, where anyon c splits into anyons a and b.
```

We can also use an alternative representation where we take a top-down view of the fusion process, as shown in Figure {numref}`fig:fusion_diagram_topdown`.

```{figure} ../images/FusionDiagramTopDown.svg
---
align: center
width: 65%
name: fig:fusion_diagram_topdown
---
A top-down view of a fusion diagram showing anyons a and b fusing to form anyon c. 
```

For a given set of anyons, we can define a vector space of states associated with that configuration. For example, for two Fibonacci anyons $\tau$, we have two possible fusion channels, corresponding to two states

```{figure} ../images/FibonacciTwoAnyonStates.svg
---
align: center
width: 40%
name: fig:fibonacci_two_anyon_states
---
```

For three Fibonacci anyons, we have three possible fusion diagrams,

```{figure} ../images/FibonacciThreeAnyonStates.svg
---
align: center
width: 75%
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

## F-moves

An important point when defining the states in the previous section was that we had to fix the order in which we fused the anyons. However, we can change the order in which we fuse the anyons and also get a valid state. For example, as shown in {numref}`fig:different_fusion_orders` for three anyons $a$, $b$ and $c$, we can either fuse $a$ and $b$ first, and then fuse the result with $c$, or we can fuse $b$ and $c$ first, and then fuse the result with $a$. 

```{figure} ../images/DifferentFusionOrders.svg
---
align: center
width: 70%
name: fig:different_fusion_orders
---
Two different fusion orders for three anyons a, b and c.
```

The question is: how are these two different fusion orders related? To relate the two we need to add a new ingredient into our TQFT, known as the **F-symbols** or **F-moves**. The F-symbols are complex numbers that relate different fusion orders. For three anyons $a$, $b$ and $c$ fusing to form anyon $d$, the F-move is written as

```{figure} ../images/FMove.svg
---
align: center
width: 80%
name: fig:f_move
---
An F-move relating two different fusion orders for three anyons a, b and c fusing to form anyon d.
```

For us, we consider the case where the F-moves are unitary transformations, i.e. $[F^{abc}_d]^{-1}_{fe} = [F^{abc}_d]^{*}_{ef}$. We also have that $F^{abc}_d$ is *trivial* if any of $a$, $b$, $c$ or $d$ is the vacuum anyon. What trivial means will depend on which anyon is the vacuum, in these cases the diagram boils down to a slightly deformed version of two-anyon fusion.  

### The Pentagon Equation

While the F-moves are an ingredient we add into our definition of the TQFT, they cannot be chosen arbitrarily. The F-moves must satisfy a consistency condition known as the **pentagon equation**. The pentagon equation arises when we consider four anyons $a$, $b$, $c$ and $d$ fusing to form anyon $e$. Given any two fusion orders, there are two distinct sequences of F-moves that relate them, as shown in {numref}`fig:pentagon_equation`. For the TQFT to be consistent, these two sequences of F-moves must give the same result. This requirement leads to the pentagon equation, which can be written as

```{figure} ../images/PentagonEquation.svg
---
align: center
width: 95%
name: fig:pentagon_equation
---
The pentagon equation relating two different sequences of F-moves for four anyons a, b, c and d fusing to form anyon e.
```

Mathematically, the pentagon equation is written as

$$
\left[ F^{fcd}_e \right]_{gl} \left[ F^{abl}_e \right]_{fk} = \sum_{h} \left[ F^{abc}_g \right]_{fh}  \left[ F^{ahd}_e \right]_{gk} \left[ F^{bcd}_k \right]_{hl}. 
$$

So when we have four anyons, we must have F-moves that satisfy this equation. You might ask, "what about more than four anyons?" It turns out that if the F-moves satisfy the pentagon equation for four anyons, then they will automatically satisfy all higher consistency conditions for more than four anyons. Thus, the pentagon equation is the key consistency condition for the F-moves. 

```{admonition} Exercise
For the Fibonacci anyon model, show that only $F^{\tau \tau \tau}_1$ and $F^{\tau \tau \tau}_\tau$ are non-trivial. Using an (unexplained) gauge freedom in the choice of F-moves, we can set $F^{\tau \tau \tau}_1 = 1$. Therefore, solve the pentagon equation to find the solution

$$
F^{\tau \tau \tau}_\tau = \begin{pmatrix}
\phi^{-1} & \phi^{-1/2} \\
\phi^{-1/2} & -\phi^{-1}
\end{pmatrix},
$$
where $\phi = (1 + \sqrt{5})/2$ is the golden ratio.

```


## R-moves

So far, we have only considered fusion of anyons, but we also need to be able to exchange or braid anyons. To describe the braiding of anyons, we introduce another ingredient into our TQFT, known as the **R-symbols** or **R-moves**. The R-moves are complex numbers that relate a diagram with a crossing (i.e. an exchange of two anyons) to a diagram without a crossing. For two anyons $a$ and $b$ fusing to form anyon $c$, the R-move is written as

```{figure} ../images/RMove.svg
---
align: center
width: 50%
name: fig:r_move
---
An R-move relating a diagram with a crossing of anyons a and b to a diagram without a crossing, where a and b fuse to form anyon c.
```

We have introduced crossing in our diagrams. We should think of having another spatial dimension sticking out of the page, so that we can have one anyon going "over" another anyon.

```{figure} ../images/RMoveTopDown.svg
---
align: center
width: 60%
name: fig:r_move_topdown
---
A top-down view of an R-move relating a diagram with a crossing of anyons a and b to a diagram without a crossing, where a and b fuse to form anyon c.
```

The R-moves, $R^{ab}_c$, are complex phases with $[R^{ab}_c]^{-1} = [R^{ab}_c]^*$. Similar to the F-moves, the R-moves are trivial (meaning equal to 1) if $a$ or $b$ is the vacuum anyon. If $c$ is the vacuum anyon, then the R-move corresponds to exchanging an anyon with its anti-particle, which can give a non-trivial phase.

### The Hexagon Equations

Just as for the F-moves, not all choices of R-moves are allowed. Here the choice of $R$ has to be consistent with the F-moves and satisfy the **hexagon equation**. 

```{figure} ../images/HexagonEquation.svg
---
align: center
width: 95%
name: fig:hexagon_equation
---
```

Here we start with three anyons with a very particular braid and see that there are two inequaivalent ways of untangling the braid using a combination of F- and R-moves. The hexagon equation states that these two different sequences of moves must give the same result. Mathematically, the hexagon equation is written as

$$
R^{ab}_e \left[ F^{bac}_d \right]_{eg} R^{ac}_g = \sum_{f} \left[ F^{abc}_d \right]_{ef} R^{af}_d \left[ F^{bca}_d \right]_{fg},
$$

An instance of the Maclance coherence theorem states that if the F- and R-moves satisfy the pentagon and hexagon equations, then all higher consistency conditions for more anyons are automatically satisfied.

The pentagon and hexagon equations are generally a complicated set of coupled equations and there is no general closed-form solution for arbitrary anyon models. However, for specific anyon models, solutions can be found. 

```{admonition} Exercise
1. Using that $R^{a1}_{a} = R^{1a}_{a} = 1$, and that $R^{ab}_c = 0$ if $N_{ab}^c = 0$, show that for the Fibonacci anyon model, only $R^{\tau \tau}_1$ and $R^{\tau \tau}_\tau$ are non-trivial.

2. Solve the hexagon equation with $a = b = c = d = \tau$ to find the remaining R-moves. Note there are two solutions related by complex conjugation. One solution is

$$
R^{\tau \tau}_1 = e^{-4 \pi i / 5}, \quad R^{\tau \tau}_\tau = e^{3 \pi i / 5}.
$$  

```

We have now defined our TQFT in terms of anyon types, fusion rules, F-moves and R-moves. In the next lecture, we will see how to use these ingredients to define modular S and T matrices, which encode the braiding properties of the anyons.

## Summary



<!--
---

## References

```{bibliography}
:filter: docname in docnames
```

-->