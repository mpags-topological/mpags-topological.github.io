# Lecture 2 - Topological Insulators I

In this lecture we will begin to introduce some key topological models - namely the Su-Schrieffer-Heeger (SSH) model and the Haldane Model. Through these we will focus on a couple of key features of topological physics - invariants and edge modes. Additionally these models will serve as introductory examples to the class of systems known as topological insulators. As the name suggests these are insulating materials that have topological properties.


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

The Haldane model is defined on the honeycomb lattice <span style="color:red;">(INSERT FIG)</span> and consists on three terms.


First, we have the onsite terms where the different sublattices have an energy difference of $2M$
$$
H_{\rm site}=M\sum_{i\in A}a^\dagger_ia_i - M\sum_{i \in B} b_i^\dagger b_i
$$

<span style="color:red;">NEED TO DEFINE WHAT I MEAN BY THE SUBSCRIPTS. USE THE VECTORS DEFINED IN THE FIGURE</span>

There are also nearest neighbout hopping terms
$$
H_{\rm n.n.} = t_1\sum_{\langle i, j \rangle} \left( b_{i+j}^\dagger a_i + a_i^\dagger b_{i+j}\right)
$$
and next nearest neighbour hopping terms
$$
H_{\rm n.n.n.} = t_2\sum_{\langle i, j \rangle} \left( {\rm e}^{-i\varphi}a_{i+j_1}^\dagger a_i + {\rm e}^{i\varphi}a_i^\dagger a_{i+j_1}\right) + t_2\sum_{\langle i, j \rangle} \left( {\rm e}^{i\varphi}b_{i+j_2}^\dagger b_i + {\rm e}^{-i\varphi}b_i^\dagger a_{i+j_2}\right)
$$
We emphasise that the next nearest neighbour hopping terms have an additional phase associated with them. This phase is precisely what allows for the quantum Hall physics without the magnetic field.

As with the SSH model, the first step is to obtain the energy spectrum in momentum space. Through this we can identify the parameters at which gaps in the spectrum close and therefore obtain the different topological regimes. These regimes can subsequently be characterised through invariants and topological edge states.

Using that for this model we can write $\sum_{i \in A} \rightarrow \tfrac{1}{2}\sum_i$, the Fourier transform can be expressed in the same way as for the SSH model, $H=\sum_{\bm k} \Psi_{\bm k}^\dagger H_{\bm k} \Psi_{\bm k}$, with 

$$
H_{\bm k} = \left(\begin{matrix}\frac{M}{2}+t_2\sum_j \cos (\varphi+{\bm k}\cdot\tilde{\bm R}_j) &\frac{t_1}{2}\sum_j {\rm e}^{i {\bm k}\cdot{\bm R}_j} \\\frac{t_1}{2}\sum_j {\rm e}^{-i {\bm k}\cdot{\bm R}_j} & -\frac{M}{2}+t_2\sum_j \cos (\varphi-{\bm k}\cdot\tilde{\bm R}_j) \end{matrix}\right)
$$

In order to diagonalise this, it can be convenient to express this in the form $H_{\bm k}= d_0({\bm k}) \sigma_0 + {\bm d}({\bm k})\cdot {\bm \sigma}$ as then the energy takes the simple form

$$
E({\bm k}) = d_0({\bm k}) \pm \sqrt{d_x^2({\bm k}) + d_y^2 ({\bm k}) + d_z^2({\bm k})}
$$
<span style="color:red;">MENTION HOW THIS FORM IS MORE GENERAL - IS IT ANY TWO BAND MODEL????</span>

For the Haldane model, 
$$
d_0({\bm k})= t_2\sum_j \cos \varphi \cos({\bm k}\cdot\tilde{\bm R}_j)\\
d_x({\bm k})=\frac{t_1}{2}\sum_j \cos({\bm k}\cdot {\bm R}_j) \\
d_y({\bm k})=-\frac{t_1}{2}\sum_j \sin({\bm k}\cdot {\bm R}_j) \\
d_z({\bm k})= \frac{M}{2}-t_2\sum_j \sin \varphi \sin({\bm k}\cdot\tilde{\bm R}_j)
$$

We now wish to look at where the spectrum is gapless. In order to identify these points we need $d_x^2({\bm k}) + d_y^2 ({\bm k}) + d_z^2({\bm k})=0$ for a given ${\bm k}$. As each of the components are real, this condition means that we need $d_x({\bm k}) = d_y ({\bm k}) = d_z({\bm k})=0$ for a given ${\bm k}$.

To find the parameters at which this occurs, let's start by considering $d_x({\bm k}) = d_y ({\bm k})=0$ and finding how to satisfy this. In particular, we will find the ${\bm k}$ at which this is satisfied. Then, by substituting this into $d_z({\bm k})=0$, we can find the parameters (and the ${\bm k}$) at which the spectrum is gapless.

Starting with the $x$ and $y$ components we need to solve

$$
\sum_j \cos({\bm k}\cdot{\bm R}_j) = \sum_j \sin({\bm k}\cdot{\bm R}_j) = 0
$$

Using that for the honeycomb lattice we have depicted, ${\bm R}_1 = \hat{\bm y}$, ${\bm R}_2=-\tfrac{\sqrt{3}}{2}\hat{\bm x}-\tfrac{1}{2}\hat{\bm y}$, ${\bm R}_3=\tfrac{\sqrt{3}}{2}\hat{\bm x}-\tfrac{1}{2}\hat{\bm y}$, we find that the above conditions lead to the following equations

$$
\cos k_y= -2\cos\left( \frac{\sqrt{3}}{2} k_x \right)\cos\left( \frac{1}{2} k_y \right) \\ \sin k_y= 2\cos\left( \frac{\sqrt{3}}{2} k_x \right)\sin\left( \frac{1}{2} k_y \right)
$$

By dividing the first equation by the second, we easily obtain $k_y = 0$, which means the second equation above is automatically satisfied. Substituting this result into the top equation though then gives that $k_x = \pm \tfrac{4\pi}{3\sqrt{3}}$ (these momenta are those contained within the first Brillouin zone). We find then that this condition is closed at two inequivalent points in momentum space, known as the $K$ and $K'$ points,

$$
{\bm K} = \left(\tfrac{4\pi}{3\sqrt{3}}, 0 \right), \hspace{10pt} {\bm K'} = -\left(\tfrac{4\pi}{3\sqrt{3}}, 0 \right)
$$

In order to find where the spectrum is gapless, we also need to find where $d_z({\bm k})=0$. Substituing the nearest neighbours and the $K$ and $K'$ points into the expression for $d_z$, we find that to satisfy $d_z=0$, we require

$$
M = \pm 3\sqrt{3}t_2\sin \varphi
$$

where the plus sign is for the $K$ point and the minus is at the $K'$ point. So we have now identified that when this condition is satisfied, the specturm will have a gap closure (at either the $K$ or $K'$ point). We can therefore plot a phase diagram of the Haldane model of $M$ vs $\varphi$ and calculate the invariant in each regime. For the Haldane model, the invariant is the Chern number and the result is shown below.

<span style="color:red;">INSERT FIG</span>

The final thing we wish to demonstrate is the edge modes. To do this we consider the model on a cylinder, with periodic boundary conditions in the $y$ direction and open boundary conditions in the $x$. In this setup, the chiral edge mode will appear as a mode on each edge propagating in opposite directions as we sketch below. We also plot the spectrum in this setup and clearly highlight the edge modes.

<span style="color:red;">INSERT FIG</span>

## Summary