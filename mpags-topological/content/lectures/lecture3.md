# Lecture 3 - Topological Insulators II

In the previous lecture we looked at a couple of key models in the theory of topological insulators. These were the SSH model which is a 1d topological insulator and the Haldane model which is a Chern insulator. So what's the difference between a Chern insulator and a topological insulator? Both are insulating phases with topological properties and sometimes (depending on who you ask) Chern insulators are considered a subset of topological insulators. An alternative definition for topological insulators is related to symmetry protected topological (SPT) phases. In this definition, the topological modes are also protected by an additional symmetry, however this excludes Chern insulators from being a topological insulator.

In this lecture we will look to understand the importance of symmetries further. To begin, we introduce a classic model for a symmetry-protected topological insulator - the Kane-Mele model

## Kane-Mele

The foundation of the Kane-Mele model is the Haldane model we saw in the last lecture, though we now add two additional components; spin and spin-orbit coupling. 
In order to add spin, we simply take two copies of the Haldane model with opposite spin. We additionally let $\varphi \rightarrow -\varphi$ for $\uparrow\rightarrow\downarrow$. Therefore, we have

$$
H_{\rm site}=M\sum_{i\in A}\sum_{\sigma=\uparrow, \downarrow}a^\dagger_{i,\sigma}a_{i, \sigma} - M\sum_{i \in B}\sum_{\sigma=\uparrow, \downarrow} b_{i,\sigma}^\dagger b_{i,\sigma}
$$

$$
H_{\rm n.n.} = t_1\sum_{\langle i, j \rangle} \sum_{\sigma}\left( b_{i+j, \sigma}^\dagger a_{i, \sigma} + a_{i,\sigma}^\dagger b_{i+j, \sigma}\right)
$$

$$
H_{\rm n.n.n.} = t_2\sum_{\langle i, j \rangle} \left( {\rm e}^{-i\varphi}a_{i+j_1, \uparrow}^\dagger a_{i,\uparrow} + {\rm e}^{i\varphi}a_{i,\uparrow}^\dagger a_{i+j_1, \uparrow}\right) + t_2\sum_{\langle i, j \rangle} \left( {\rm e}^{i\varphi}b_{i+j_2, \uparrow}^\dagger b_{i, \uparrow} + {\rm e}^{-i\varphi}b_{i, \uparrow}^\dagger a_{i+j_2, \uparrow}\right) \\ + t_2\sum_{\langle i, j \rangle} \left( {\rm e}^{i\varphi}a_{i+j_1, \downarrow}^\dagger a_{i,\downarrow} + {\rm e}^{-i\varphi}a_{i,\downarrow}^\dagger a_{i+j_1, \downarrow}\right) + t_2\sum_{\langle i, j \rangle} \left( {\rm e}^{-i\varphi}b_{i+j_2, \downarrow}^\dagger b_{i, \downarrow} + {\rm e}^{i\varphi}b_{i, \downarrow}^\dagger a_{i+j_2, \downarrow}\right)
$$

We then incorporate spin-orbit coupling using a nearest neighbour Rashba term, which has the form

$$
H_{\rm SOC} =  -\frac{i\alpha}{2} \sum_{\langle i,j \rangle} \left(b^\dagger_{i+j}({\boldsymbol \sigma} \times {\boldsymbol R_j})_z a_i - a^\dagger_i({\boldsymbol \sigma} \times {\boldsymbol R_j})_z b_{i+j}\right)
$$

where $\alpha$ is the coupling strength and the operators here are actually spinors, $a_i = (a_{i, \uparrow}, a_{i, \downarrow})^{\rm T}$ with the Pauli matrices acting in the acting in this spin subspace.

As we saw in the previous lecture, it is possible to analyse the spectrum in order to identify the topological phases, however in this case the invariant is not the Chern number. Later on we will address what the invariant is for this model, but for now let's explore why this model is different to the Haldane model.