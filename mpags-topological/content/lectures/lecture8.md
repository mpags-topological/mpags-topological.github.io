# Lecture 8 - Topological Quantum Field Theory: Braiding and modular S and T

Previously, we defined our topological quantum field theory (TQFT) in terms of anyon types, fusion rules, F-moves and R-moves. If these ingredients satisfy certain consistency conditions (the pentagon and hexagon equations), then we have a well-defined TQFT. In this lecture, we will focus on how to extract physical information about the anyons from these ingredients, specifically through braiding and the modular S and T matrices.

## Braids

Equipped with the F and R-moves, we can now describe more general braiding operations on multiple anyons. The core idea is to fix a basis for the multi-anyon Hilbert space, which corresponds to choosing a particular order for fusing the anyons together. The we can swap (braid) anyons to get a twisted diagram. We then use the F- and R-moves to untwist the diagram back into our original basis. This procedure gives us a unitary operator that describes the braiding operation in our chosen basis. For example, let use consider a braid $B_{i, i+1}$ that exchanges anyons $i$ and $i+1$ in a system of $n$ anyons. Diagramatically, we have

```{figure} ../images/BraidDiagram.svg
---
align: center
width: 95%
name: braid_diagram
---
```

where we have acted on a chosen basis state. To express this braid in our chosen basis, we first use an inverse F-move so that anyons $i$ and $i+1$ are directly fused together. We then apply the R-move to exchange them, and finally use the F-move to return to our original basis. In diagramatic form this is

```{figure} ../images/BraidOperation.svg
---
align: center
width: 70%
name: braid_operation
---
```

This gives use the definition of the braid operator

$$
\left[ B^{abc}_e \right]_{df} = \sum_{g} \left[F^{acb}_e\right]_{dg} R^{cb}_g \left[F^{abc}_e\right]^{-1}_{gf}
$$

```{note}
We have freedom of where we put the indices in the braid operator, and you may see different conventions in the literature. In particular, should the index ordering correspond to the anyon order before or after the braid? The important thing is to be consistent.
```

```{admonition} Exercise
Show using the Fibonacci F- and R-moves that the two braid operators for three $\tau$ anyons are

COMPLETE EXERCISE!!!
```

## Exchange Statistics: The T matrix

One of the most important physics properties of anyons that we have encountered before is their exchange statistics. Previously, we simply wrote down that on exchange of anyons we get a phase $\theta_a$ for anyon type $a$. Now we have the machinery to derive this phase from the R-moves. 

The **topological spin** $\theta_a$ of an anyon type $a$ is defined by the following diagram. 

```{figure} ../images/TopologicalSpin.svg
---
align: center
width: 50%
name: topological_spin
---
```

We can interpret this diagram physically by taking a top-down view, that is

```{figure} ../images/TopologicalSpinTopDown.svg
---
align: center
width: 95%
name: topological_spin_top_down
---
```

which nicely matches with our previous definition of exchange statistics. Let us now *evaluate* this diagram using our F- and R-moves. Note, in the process we will use a couple of identities that we have not introduced, but we will show what we use in each step.

```{figure} ../images/TopologicalSpinEvaluation.svg
---
align: center
width: 90%
name: topological_spin_evaluation
---
```

In total we have

$$
\theta_a = \frac{1}{d_a} \sum_c d_c \, R^{aa}_c
$$

and we can collect this into a diagonal matrix called the **T matrix**, with elements $T_{ab} = \theta_a \delta_{ab}$. The T matrix encodes the exchange statistics of the anyons in our theory.

```{note}
For abelian anyons, formula for the topological spin simplifies since we have only one fusion channel and all quantum dimensions $d_a=1$, so if $a\times a = c$, then $\theta_a = R^{aa}_c$.
```

<!-- ```{admonition} Exercise
1. Compute $\theta_\tau$ for the Fibonacci anyon model using the F- and R-moves we derived previously.
2. Compute $\theta_a$ for your favourite anyon model.
``` 
-->

## Mutual Statistics: The S matrix

The next quantity we want to derive is the mutual statistics between different anyon types. This is encoded in the modular S matrix, which we will now define and evaluate. The modular S matrix is defined by the following diagram.

```{figure} ../images/ModularSMatrix.svg
---
align: center
width: 50%
name: modular_s_matrix
---
```

where $\mathcal{D} = \sqrt{\sum_a d_a^2}$ is the total quantum dimension of the theory. From this diagram, we can already see some symmetries the $S$ matrix should have. Specifically, $S_{ab} = S_{ba}$ since we can rotate the diagram by $180^\circ$ about a horizontal axis. We also have that $S_{1a} = d_a/\mathcal{D}$ since the anyon of type $1$ (the vacuum) can be removed from the diagram without changing its value.

Again, we can interpret this diagram physically by taking a top-down view, that is

```{figure} ../images/ModularSMatrixTopDown.svg
---
align: center
width: 95%
name: modular_s_matrix_top_down
---
```

which matches our previous definition of mutual statistics. Let us now *evaluate* this diagram using our F- and R-moves. Note, in the process we will use a couple of identities that we have not introduced, but we will show what we use in each step. The idea here is not to get bogged down in the details of the evaluation, but to see how we can use the F- and R-moves to evaluate complicated diagrams.

```{figure} ../images/ModularSMatrixEvaluation.svg
---
align: center
width: 90%
name: modular_s_matrix_evaluation
---
```

## Summary

In this section we have seen how to use the F- and R-moves to derive the braiding properties of anyons, which are encoded in the modular S and T matrices. The S and T matrices are fundamental quantities that encode the topological properties of the anyons in our theory, and they play a crucial role in understanding the physics of anyons and their applications in topological quantum computation.



<!--
---

## References

```{bibliography}
:filter: docname in docnames
```

-->