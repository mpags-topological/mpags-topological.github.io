# Topological Insulators I

In this lecture we will begin to introduce some key topological models - namely the Su-Schrieffer-Heeger (SSH) model and the Haldane Model. Through these we will focus on a couple of key features of topological physics - invariants and edge modes. Additionally these models will serve as introductory examples to the class of systems known as topological insulators. As the name suggests these are insulating materials that have topological properties. Should you wish to read more about the models in this lecture then some useful references are {cite}`BernevigHughes, QiZhang_Review, Asboth_TI_Course, HasanKane_Review`.


## The SSH Model

The SSH model is a simple model that demonstrates topological properties. Initially introdiced as a simple model of a polymer {cite}`SSH_Model`, in this model there are unit cells consisting of two different sublattices, $A$ and $B$. The intracell and intercell hopping strengths are given by $t_1$ and $t_2$ respectively.

```{figure} ../../_static/figs/SSH_Model.svg
:width: 100%
:height: 100

The SSH Model
```


The Hamiltonian is given by 

$$
H = t_1\sum_{n=1}^N \left(b_n^\dagger a_n+a_n^\dagger b_n\right)+t_2\sum_{n=1}^{N-1} \left(a_{n+1}^\dagger b_n+b_n^\dagger a_{n+1}\right).
$$

where the sum is over the unit cells, of which there are $N$ in total.

Initially, let's explore the bulk properties of the system. In order to do this we assume periodic boundary conditions, meaning that every unit cell is effectivley in the middle of an infinite system. Assuming these boundary conditions allows us to take the Fourier transform

$$
a_n = \sum_k {\rm e}^{ikn}a_k, 
$$

to give

$$
H = t_1\sum_k (b_k^\dagger a_k+a_k^\dagger b_k) +t_2 \sum_k\left({\rm e}^{-ik}a_k^\dagger b_k+{\rm e}^{ik}b_k^\dagger a_k\right)
$$

We can write this in the form $H = \sum_k \Psi_k^\dagger H_k \Psi_k$ with $\Psi_k = \left(a_k, b_k \right)^{\rm T}$ and 

$$
H_k = \left(\begin{matrix}0 &t_1+t_2{\rm e}^{-ik} \\t_1+t_2{\rm e}^{ik} &0 \end{matrix}\right)
$$

We can then obtain the energy spectrum by solving the eigenvalue equation $H_k \Psi_k = E_k \Psi_k$

$$
E_k^2 = (t_1+t_2{\rm e}^{-ik})(t_1+t_2{\rm e}^{ik}) \implies E_k = \pm\sqrt{t_1^2+t_2^2+2t_1t_2\cos k}
$$

<iframe src="../../_static/plots/ssh_dispersion.html" width="100%" height="600" style="border:none;"></iframe>

From the expression for the energy, as well as the plot we make a couple of remarks. First if $|t_1| \neq |t_2|$, then the spectrum is gapped (no modes that cross zero energy) for all $k$. The system in this phase is an insulator. However when $|t_1| = |t_2|$, it can be possible to close the gap, such that the system becomes a conductor. The gap closes at 

$$
\begin{align}
k&=0 \hspace{4pt}\mathrm{for } \hspace{4pt} t_1=-t_2\\ k&=\pi  \hspace{4pt}\mathrm{for} \hspace{4pt} t_1=t_2
\end{align}
$$

It is precisely at these points that a topological phase transition can occur. We now need to identify when we are in the topological phase and try to understand its properties. Let's begin by calculating the topological invariant. To do this we write $H_k$ in the form


$$
H_k = \left(\begin{matrix}0 &t_1+t_2\cos k-it_2\sin k \\t_1+t_2\cos k +it_2 \sin k &0 \end{matrix}\right) = d_0(k) \sigma_0 + {\boldsymbol d}(k)\cdot {\boldsymbol \sigma}
$$

with

$$
\begin{align}
d_0 &= d_z=0,\\
d_x &= t_1 + t_2 \cos k, \\ d_y &= t_2 \sin k
\end{align}
$$

In the above the notation $\sigma_0$ is the identity and ${\boldsymbol \sigma}$ is a three-dimensional vector of Pauli matrices. Using these definitions, the invariants is defined as 

$$
\nu = \frac{1}{2\pi}\int {\rm d}k \left(\frac{{\boldsymbol d}}{|{\boldsymbol d}|}\times \frac{\partial}{\partial k} \frac{{\boldsymbol d}}{|{\boldsymbol d}|}\right)_z
$$

```{note}
Notice the subscript $z$ in the above equation, so when we expand out the cross-product, it doesn't look too dissimilar from the Chern number. However, it is different and in this case is known as the Winding number. The reason for this name is that as $k$ goes from $0\rightarrow 2\pi$, the vector ${\boldsymbol d}$ traces a circle and this invariant simply counts how many time the vector winds around the origin. 
```

Performing this integral gives $\nu=1$ for $|t_1|<|t_2|$ and $\nu = 0$ otherwise. The non-zero winding signifies a non-trivial topological phase which we will now demonstrate by considering the edge states. 

### Edge States

Let's start by considering the case where $|t_1|>|t_2|$. To do this we will look at $t_1=1, t_2=0$. In this case, it is easy to see that all sites are "paired up".


```{figure} ../../_static/figs/SSH_pairing.svg
:width: 100%
:height: 100

All sites are paired in the trivial regime and there are no edge modes.
```

Therefore there are no edge states in this regime, which is consistent with the trivial value of the invariant.

Now if we consider the opposite limit of $t_1=0, t_2=1$, we can see that the pairing now misses out the two edge modes.

```{figure} ../../_static/figs/SSH_Edge_Modes.svg
:width: 100%
:height: 100

In the topological regime we have edge modes that are unpaired and sit at zero energy
```


If we look at the Hamiltonian in this limit,

$$
H = \sum_{n=1}^{N-1} \left(a_{n+1}^\dagger b_n+b_n^\dagger a_{n+1}\right)
$$

we see that $a_1$ and $b_N$ (the edges of the system) are no longer involved in the Hamiltonian. This means that we can add a mode to these sites at no energy cost - we have zero-energy (gapless) edge modes. This is consistent with $\nu \neq 0$ found earlier.

Even away from the the values of parameters considered here, the topological edge states are found to be robust, as we demonstrate numerically below, where we plot the energy spectrum for 30 sites and the probability distribution for the highlighted mode, which is the mode with the smallest absolute energy. 

```{figure} ../../_static/plots/SSH_RealSpace.svg
:width: 100%
:height: 300

The real space structure of the lowest energy modes (highlighted in the inset) of the SSH model in the trivial (left) and topological (right) regimes.
```


## The Haldane Model

We now turn to the Haldane Model {cite}`Haldane_Model`, which was the first model of type of matter known as a Chern insulator. A Chern insulator shows the physics of the quantum Hall effect without the magnetic field. Here, we will introduce the model and demonstrate that it has a non-trivial Chern number which can be associated to robust edge modes via the bulk-boundary correspondence.

The Haldane model is defined on the honeycomb lattice  and consists on three terms.

```{figure} ../../_static/figs/HaldaneModel.svg
:width: 100%
:height: 400

The Haldane model. The $A$ sublattice is purple and the $B$ sublattice is green. The orange hops have an associated phase of $\varphi$.
```

First, we have the onsite terms where the different sublattices have an energy difference of $2M$

$$
H_{\rm site}=M\sum_{i\in A}a^\dagger_ia_i - M\sum_{i \in B} b_i^\dagger b_i
$$

Here, by $a_i$ we mean the annihilation operator defined on the site located at ${\boldsymbol r}_i$. The nearest neighbours will be located at ${\boldsymbol r}_i + {\boldsymbol R}_j$ and belong to opposite lattice. Denoting the corresponding operators as $b_{i+j}$, the nearest neighbour hopping term becomes

$$
H_{\rm n.n.} = t_1\sum_{\langle i, j \rangle} \left( b_{i+j}^\dagger a_i + a_i^\dagger b_{i+j}\right)
$$

The next nearest neighbours in this model connect sites belonging to the same sublattice and sit at ${\boldsymbol r}_i + \widetilde{\boldsymbol R}_j$. Denoting the operators as $a_{i+j'}$ and $b_{i+j'}$, the Hamiltonian for next nearest neighbour hopping is 

$$
H_{\rm n.n.n.} = t_2\sum_{\langle i, j' \rangle} \left( {\rm e}^{-i\varphi}a_{i+j'}^\dagger a_i + {\rm e}^{i\varphi}a_i^\dagger a_{i+j'}\right) + t_2\sum_{\langle i, j' \rangle} \left( {\rm e}^{i\varphi}b_{i+j'}^\dagger b_i + {\rm e}^{-i\varphi}b_i^\dagger b_{i+j'}\right)
$$

We emphasise that the next nearest neighbour hopping terms have an additional phase associated with them. This phase is precisely what allows for the quantum Hall physics without the magnetic field.

As with the SSH model, the first step is to obtain the energy spectrum in momentum space. Through this we can identify the parameters at which gaps in the spectrum close and therefore obtain the different topological regimes. These regimes can subsequently be characterised through invariants and topological edge states.

Using that for this model we can write $\sum_{i \in A} \rightarrow \tfrac{1}{2}\sum_i$, the Fourier transform can be expressed in the same way as for the SSH model, $H=\sum_{\boldsymbol k} \Psi_{\boldsymbol k}^\dagger H_{\boldsymbol k} \Psi_{\boldsymbol k}$, with 

$$
H_{\boldsymbol k} = \left(\begin{matrix}\frac{M}{2}+t_2\sum_j \cos (\varphi+{\boldsymbol k}\cdot\tilde{\boldsymbol R}_j) &\frac{t_1}{2}\sum_j {\rm e}^{i {\boldsymbol k}\cdot{\boldsymbol R}_j} \\\frac{t_1}{2}\sum_j {\rm e}^{-i {\boldsymbol k}\cdot{\boldsymbol R}_j} & -\frac{M}{2}+t_2\sum_j \cos (\varphi-{\boldsymbol k}\cdot\tilde{\boldsymbol R}_j) \end{matrix}\right)
$$

In order to diagonalise this, it can be convenient to express this in the form $H_{\boldsymbol k}= d_0({\boldsymbol k}) \sigma_0 + {\boldsymbol d}({\boldsymbol k})\cdot {\boldsymbol \sigma}$ as then the energy takes the simple form

$$
E({\boldsymbol k}) = d_0({\boldsymbol k}) \pm \sqrt{d_x^2({\boldsymbol k}) + d_y^2 ({\boldsymbol k}) + d_z^2({\boldsymbol k})}
$$


For the Haldane model, 

$$
d_0({\boldsymbol k})= t_2\sum_j \cos \varphi \cos({\boldsymbol k}\cdot\tilde{\boldsymbol R}_j)\\
d_x({\boldsymbol k})=\frac{t_1}{2}\sum_j \cos({\boldsymbol k}\cdot {\boldsymbol R}_j) \\
d_y({\boldsymbol k})=-\frac{t_1}{2}\sum_j \sin({\boldsymbol k}\cdot {\boldsymbol R}_j) \\
d_z({\boldsymbol k})= \frac{M}{2}-t_2\sum_j \sin \varphi \sin({\boldsymbol k}\cdot\tilde{\boldsymbol R}_j)
$$

We now wish to look at where the spectrum is gapless. In order to identify these points we need $d_x^2({\boldsymbol k}) + d_y^2 ({\boldsymbol k}) + d_z^2({\boldsymbol k})=0$ for a given ${\boldsymbol k}$. As each of the components are real, this condition means that we need $d_x({\boldsymbol k}) = d_y ({\boldsymbol k}) = d_z({\boldsymbol k})=0$ for a given ${\boldsymbol k}$.

To find the parameters at which this occurs, let's start by considering $d_x({\boldsymbol k}) = d_y ({\boldsymbol k})=0$ and finding how to satisfy this. In particular, we will find the ${\boldsymbol k}$ at which this is satisfied. Then, by substituting this into $d_z({\boldsymbol k})=0$, we can find the parameters (and the ${\boldsymbol k}$) at which the spectrum is gapless.

Starting with the $x$ and $y$ components we need to solve

$$
\sum_j \cos({\boldsymbol k}\cdot{\boldsymbol R}_j) = \sum_j \sin({\boldsymbol k}\cdot{\boldsymbol R}_j) = 0
$$

Using that for the honeycomb lattice we have depicted, ${\boldsymbol R}_1 = \hat{\boldsymbol y}$, ${\boldsymbol R}_2=-\tfrac{\sqrt{3}}{2}\hat{\boldsymbol x}-\tfrac{1}{2}\hat{\boldsymbol y}$, ${\boldsymbol R}_3=\tfrac{\sqrt{3}}{2}\hat{\boldsymbol x}-\tfrac{1}{2}\hat{\boldsymbol y}$, we find that the above conditions lead to the following equations

$$
\cos k_y= -2\cos\left( \frac{\sqrt{3}}{2} k_x \right)\cos\left( \frac{1}{2} k_y \right) \\ \sin k_y= 2\cos\left( \frac{\sqrt{3}}{2} k_x \right)\sin\left( \frac{1}{2} k_y \right)
$$

By dividing the first equation by the second, we easily obtain $k_y = 0$, which means the second equation above is automatically satisfied. Substituting this result into the top equation though then gives that $k_x = \pm \tfrac{4\pi}{3\sqrt{3}}$ (these momenta are those contained within the first Brillouin zone). We find then that this condition is closed at two inequivalent points in momentum space, known as the $K$ and $K'$ points,

$$
{\boldsymbol K} = \left(\tfrac{4\pi}{3\sqrt{3}}, 0 \right), \hspace{10pt} {\boldsymbol K'} = -\left(\tfrac{4\pi}{3\sqrt{3}}, 0 \right)
$$

In order to find where the spectrum is gapless, we also need to find where $d_z({\boldsymbol k})=0$. Substituing the nearest neighbours and the $K$ and $K'$ points into the expression for $d_z$, we find that to satisfy $d_z=0$, we require

$$
M = \pm 3\sqrt{3}t_2\sin \varphi
$$

where the plus sign is for the $K$ point and the minus is at the $K'$ point. So we have now identified that when this condition is satisfied, the specturm will have a gap closure (at either the $K$ or $K'$ point). We can therefore plot a phase diagram of the Haldane model of $M$ vs $\varphi$ and calculate the invariant in each regime. For the Haldane model, the invariant is the Chern number and the result is shown below.


```{figure} ../../_static/plots/Haldane_Chern.svg
:width: 100%
:height: 300

The Chern number for the Haldane model. Changes is Chern number occur when the bulk gap closes.
```

```{note}
Sometimes in the literature, the $-1$ and $+1$ phases will be the other way around. This corresponds to letting $\varphi \rightarrow -\varphi$ in the original model
```

The final thing we wish to demonstrate is the edge modes. To do this we consider the model on a cylinder, with periodic boundary conditions in the $y$ direction and open boundary conditions in the $x$. In this setup, the chiral edge mode will appear as a mode on each edge propagating in opposite directions as we sketch below. We also plot the spectrum for $M=2, \varphi=\pi/2$, in this setup and clearly highlight the edge modes.

```{figure} ../../_static/figs/CylinderEdgeSketch.svg
:width: 100%
:height: 200

A sketch of how chiral edge modes appear on a cylinder geometry.
```

```{figure} ../../_static/plots/Haldane_Cylinder.svg
:width: 100%
:height: 300

The energy spectrum of the Haldane model in a cylinder setup. The colour shows the localisation of the edge modes. 
```

## Summary

In this lecture, we have introduced two key models in the field of topological insulators. These are the SSH model and the Haldane model. We have demonstrated that both contain topological phases, characterised by non-trivial invariants which are related to the presence of protected edge modes. These ideas that we will carry forward into future lectures. In the next lecture we will look to build on the Haldane model in order to explore different types of topological phases with different invariants.

---

## References

```{bibliography}
:filter: docname in docnames
```