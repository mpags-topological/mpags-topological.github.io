# Lecture 2 - Topological Insulators I


## The SSH Model

The SSH model is a simple model that demonstrates topological properties. In this model we have unit cells consisting of two different sublattices, $A$ and $B$. The intracell and intercell hopping strengths are given by $t_1$ and $t_2$ respectively.


The Hamiltonian is given by 

$$
H = t_1\sum_n \left(b_n^\dagger a_n+a_n^\dagger b_n\right)+t_2\sum_n \left(a_{n+1}^\dagger b_n+b_n^\dagger a_{n+1}\right).
$$

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

INSERT AN INTERACTIVE PLOT HERE?

<iframe src="../../_static/plots/ssh_dispersion.html" width="100%" height="800" style="border:none;"></iframe>

## The Haldane Model

## Exercises

Maybe something to do with Haldane model - calculate the Chern number?