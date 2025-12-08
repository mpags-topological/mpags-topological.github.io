# Lecture 2 - Topological Insulators I

In this lecture we will begin to introduce some key topological models - namely the SSH model and the Haldane Model. Through these we will focus on a couple of key features of topological physics - invariants and edge modes. Additionally these models will serve as introductory examples to the class of systems known as topological insulators. As the name suggests these are insulating materials that have topological properties.


## The SSH Model

The SSH model is a simple model that demonstrates topological properties. In this model we have unit cells consisting of two different sublattices, $A$ and $B$. The intracell and intercell hopping strengths are given by $t_1$ and $t_2$ respectively.

<img src="../../_static/figs/SSH_Model.svg" width="100%" height="200"></img>


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

<iframe src="../../_static/plots/ssh_dispersion.html" width="100%" height="800" style="border:none;"></iframe>

From the expression for the energy, as well as the plot we make a couple of remarks. First if $|t_1| \neq |t_2|$, then the spectrum is gapped (no modes that cross zero energy) for all $k$. The system in this phase is an insulator. However when $|t_1| = |t_2|$, it can be possible to close the gap, such that the system becomes a conductor. The gap closes at 

$$
k=0 \hspace{4pt}\mathrm{for } \hspace{4pt} t_1=-t_2\\ k=\pi  \hspace{4pt}\mathrm{for} \hspace{4pt} t_1=t_2
$$

It is precisely at these points that a topological phase transition can occur. We now need to identify when we are in the topological phase and try to understand its properties. Let's begin by calculating the topological invariant. To do this we write $H_k$ in the form


$$
H_k = \left(\begin{matrix}0 &t_1+t_2\cos k-it_2\sin k \\t_1+t_2cosk +it_2 \sin k &0 \end{matrix}\right) = d_0(k) \sigma_0 + {\bm d}(k)\cdot {\bm \sigma}
$$

with

$$
d_0 = d_z=0,\\
d_x = t_1 + t_2 \cos k, \hspace{5pt} d_y = t_2 \sin k
$$

In the above the notation $\sigma_0$ is the identity and ${\bm \sigma}$ is a three-dimensional vector of Pauli matrices. Using these definitions, the invariants is defined as 

$$
\nu = \frac{1}{2\pi}\int {\rm d}k \left(\frac{{\bm d}}{|{\bm d}|}\times \frac{\partial}{\partial k} \frac{{\bm d}}{|{\bm d}|}\right)_z
$$

Notice the subscript $z$, so when we expand out the cross-product, it doesn't look too dissimilar from the Chern number. However, it is different and in this case is known as the Winding number. The reason for this name is that as $k$ goes from $0\rightarrow 2\pi$, the vector ${\bm d}$ traces a circle and this invariant simply counts how many time the vector winds around the origin. 

Performing this integral gives $\nu=1$ for $|t_1|<|t_2|$ and $\nu = 0$ otherwise. The non-zero winding signifies a non-trivial topological phase which we will now demonstrate by considering the edge states. 

### Edge States

Let's start by considering the case where $|t_1|>|t_2|$. To do this we will look at $t_1=1, t_2=0$. In this case, it is easy to see that all sites are "paired up"

INSERT FIGURE

Therefore there are no edge states in this regime, which is consistent with the trivial value of the invariant.

Now if we consider the opposite limit of $t_1=0, t_2=1$, we can see that the pairing now misses out the two edge modes.

INSERT FIGURE

If we look at the Hamiltonian in this limit,

$$
H = \sum_{n=1}^{N-1} \left(a_{n+1}^\dagger b_n+b_n^\dagger a_{n+1}\right)
$$

we see that $a_1$ and $b_N$ (the edges of the system) are no longer involved in the Hamiltonian. This means that we can add a mode to these sites at no energy cost - we have zero-energy (gapless) edge modes. This is consistent with $\nu \neq 0$ found earlier.

Even away from the the values of parameters considered here, the topological edge states are found to be robust, as we demonstrate numerically below. This is the topological protection we expect for these modes.


## The Haldane Model

We now turn to the Haldane Model, which was the first model of type of matter known as a Chern insulator. A Chern insulator shows the physics of the quantum Hall effect without the magnetic field. Here, we will introduce the model and demonstrate that it has a non-trivial Chern number which can be associated to robust edge modes via the bulk-boundary correspondence.

The Haldane model is defined on the honeycomb lattice (INSERT FIG) and consists on three terms.


First, we have the onsite terms where the different sublattices have an energy difference of $2M$
$$
H_{\rm site}=M\sum_{i\in A}a^\dagger_ia_i - M\sum_{i \in B} b_i^\dagger b_i
$$

NEED TO DEFINE WHAT I MEAN BY THE SUBSCRIPTS. USE THE VECTORS DEFINED IN THE FIGURE

There are also nearest neighbout hopping terms
$$
H_{\rm n.n.} = t_1\sum_{\langle i, j \rangle} \left( b_{i+j}^\dagger a_i + a_i^\dagger b_{i+j}\right)
$$
and next nearest neighbour hopping terms
$$
H_{\rm n.n.n.} = t_2\sum_{\langle i, j \rangle} \left( {\rm e}^{-i\phi}a_{i+j'}^\dagger a_i + {\rm e}^{i\phi}a_i^\dagger a_{i+j'}\right) + t_2\sum_{\langle i, j \rangle} \left( {\rm e}^{i\phi}b_{i+\tilde{j}}^\dagger b_i + {\rm e}^{-i\phi}b_i^\dagger a_{i+\tilde{j}}\right)
$$
We emphasise that the next nearest neighbour hopping terms have an additional phase associated with them. This phase is precisely what allows for the quantum Hall physics without the magnetic field.

