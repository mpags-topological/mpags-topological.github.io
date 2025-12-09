# Lecture 4 - Topological Superconductors

In this lecture, we turn our attention from topological insulators to topological superconductors. These systems have gained increasing interest in recent years, both due to their interesting fundamental physics but also for their potential use in realising a topological quantum computer.

## The Kitaev Chain

There are many models named after Kitaev (and even others that are referred to the Kitaev chain), but here we refer to the model of a one-dimensional $p$-wave spinless superconductor. The Hamiltonian is 

$$
H = -t\sum_{m=1}^{N-1}\left(c_{m+1}^\dagger c_m + c_m^\dagger c_{m+1}\right) - \mu\sum_{m=1}^Nc_m^\dagger c_m + \sum_{m=1}^{N-1}\Delta c_m c_{m+1} + \Delta^*c_{m+1}^\dagger c_m^\dagger
$$

As is the usual first step, we explore the bulk spectrum by performing the Fourier transform

$$
H = \sum_k (-2t \cos k -\mu)c_k^\dagger c_k + \sum_k(i\Delta \sin k \hspace{3pt}c_{-k}c_k-i\Delta \sin k \hspace{3pt} c_k^\dagger c_{-k}^\dagger)
$$

One of the key differences of this compared to the models we have looked at so far is that $k$ and $-k$ are mixed. This is a feature of superconductors and the standard way to solve Bardeen-Cooper-Schrieffer (BCS) superconductors is to use a Bogoliubov transformation that mixes electron (with energy-momentum $E,k$) and hole ($E,-k$) operators. The resulting eigenstates (quasiparticles) of the theory are known as Bogoliubov quasiparticles. We effectively perform the same transformation here by writing the Hamiltonian in Bogoliubov-de Gennes (BdG) form. This symmetrises $k$ and $-k$ and in this case leads to

$$
H = \frac{1}{2}\sum_k \Psi_k^\dagger H_k \Psi_k, \hspace{20pt} H_k= \left(\begin{matrix} \varepsilon_k & \tilde{\Delta}_k^*\\ \tilde{\Delta}_k & -\varepsilon_k \end{matrix}\right)
$$

where $\Psi_k = (c_k \hspace{5pt} c_{-k}^\dagger)^{\rm T}$, $\varepsilon_k = -2t\cos k - \mu$, and $\tilde{\Delta}_k=2i\Delta\sin k$.

It is then straightforward to obtain the energy spectrum

$$
E(k) = \pm \sqrt{\varepsilon_k^2 - |\tilde{\Delta}_k|^2}=\pm \sqrt{(2t \cos k +\mu)^2 + 4|\Delta|^2\sin^2 k}
$$

For $\Delta\neq0$, the gap closes at two points; $(1): \mu=-2t$ (at $k=0$), and $(2):\mu=2t$ (at $k=\pi$). 

Therefore, we have now identified where the different topological phases occur. In order to find out which are the topologically non-trivial phases, we can calculate a $\Z_2$ invariant. However, in this course we will focus on a more intuitive approach that focuses on the topological edge states.

### Majorana Modes

By writing the pairing amplitude in the form $\Delta = |\Delta|{\rm e}^{i\phi}$, we can introduce Majorana operators  (often called Majorana fermions) in the following way

$$
\gamma_{2m-1}= {\rm e}^{i\phi/2}c_m + {\rm e}^{-i\phi/2}c_m^\dagger
\\ \gamma_{2m} = -i\left({\rm e}^{i\phi/2}c_m - {\rm e}^{-i\phi/2}c_m^\dagger \right)
$$

We wish to make a few notes regarding the introduction of these operators

1. Both $\gamma_{2m-1}$ and $\gamma_{2m}$ are associated with the site $j$. 
2. The Majorana operators obey anticommutation relations, $\{\gamma_m, \gamma_n\} = 2\delta_{m,n}$, as well as $\gamma_{2m}^\dagger = \gamma_{2m}$ and $\gamma_{2m}^2=1$.
3. In theory, we can write any fermionic Hamiltonian in terms of these Majorana fermions, although this is often not useful.

Using these operators, we can rewrite the Hamiltonian in the form

$$
H = \frac{i}{2}\sum_m\left(-\mu \gamma_{2m-1}\gamma_{2m} + (t+|\Delta|)\gamma_{2m}\gamma_{2m+1} +(-t+|\Delta|)\gamma_{2m-1}\gamma_{2m+2} \right)
$$

As we have found with previous models, one of the benefits of the topological protection is that we can study specific parameters and providing we don't close a bulk gap, the effects remain robust. 

Let's start with $t=|\Delta|=0, \mu \neq0$. This means that depending on the sign of $\mu$, we can satisfy either $\mu<-2t$ or $\mu >2t$. For these parameter the Hamiltonian simply reduces to

$$
H=-\frac{i\mu}{2}\sum_m \gamma_{2m-1}\gamma_{2m} = -\mu\sum_j c_m^\dagger c_m
$$

Here, we have effectively paired the Majorana fermions belonging to the same lattice site. As we saw with the SSH model, all sites are paired up in this limit and the edges aren't particularly relevant. This is therefore the trivial regime. The second equality above, allows us to easily understand this ground state. For $\mu <0$, adding a spinless fermion to the lattice costs energy and so the ground state is simply the empty (vacuum state). For $\mu>0$, the opposite happens and the ground state is the completely filled state.

The region we now need to understand is $-2t<\mu<2t$. To analyse this we take $t=|\Delta|>0, \mu=0$. In this limit the Hamiltonian becomes 

$$
H = it\sum_j \gamma_{2m} \gamma_{2m+1} 
$$

<span style="color:red;">be careful with sum limits in this lecture</span>

We are now effectively pairing Majoranas between different sites. As we saw with the SSH model this leaves modes at the ends of the system, which do not appear in the Hamiltonian and therefore are zero-energy modes. The key difference here is that we have a pair of **Majorana** zero modes. If we want to ask whether or not the Majorana mode is there we actually have to consider the occupation of corresponding fermionic mode, which in this case is non-local. The fermionic operator is given by $f=\tfrac{1}{2}(\gamma_1+i\gamma_{2N})$ and therefore the occupation of this mode also costs no energy in the limit of a large system size. The non-local nature of this mode (along with the fact that occupied/unoccupied represents two states) gives some initial indication that such a setup could be used to create a topologically protected qubit!


<span style="color:red;">Insert summary of what we have found</span>


## p+ip Superconductor

We now turn our attention to two dimensions (although we still assume the system is spinless). The Hamiltonian is 

$$
H = -t\sum_{m,n}(c_{m+1, n}^\dagger c_{m,n} + c_{m, n+1}^\dagger c_{m,n} + c_{m,n}^\dagger c_{m+1, n} + c_{m,n}^\dagger c_{m, n+1}) - \mu\sum_{m,n}c_{m,n}^\dagger c_{m,n} \\ + \sum_{m,n} (\Delta c_{m,n}c_{m+1, n} + i\Delta c_{m,n}c_{m, n+1} + \Delta^* c_{m+1,n}^\dagger c_{m,n}^\dagger -i\Delta^*c_{m, n+1}^\dagger c_{m,n}^\dagger)
$$

