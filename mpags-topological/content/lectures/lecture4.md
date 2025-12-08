# Lecture 4 - Topological Superconductors

In this lecture, we turn our attention from topological insulators to topological superconductors. These systems have gained increasing interest in recent years, both due to their interesting fundamental physics but also for their potential use in realising a topological quantum computer.

## The Kitaev Chain

There are many models named after Kitaev (and even others that are referred to the Kitaev chain), but here we refer to the model of a one-dimensional $p$-wave spinless superconductor. The Hamiltonian is 

$$
H = -t\sum_{j=1}^{N-1}\left(c_{j+1}^\dagger c_j + c_j^\dagger c_{j+1}\right) - \mu\sum_{j=1}^Nc_j^\dagger c_j + \sum_{j=1}^{N-1}\Delta c_j c_{j+1} + \Delta^*c_{j+1}^\dagger c_j^\dagger
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