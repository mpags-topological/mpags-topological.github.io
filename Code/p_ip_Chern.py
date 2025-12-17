# Calculate the Chern number for the Haldane model

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm



def Ham(kx, ky, t, mu, Delta):
    """
    p+ip Hamiltonian
    This has been vectorised to work with kx and ky arrays
    """
    H = np.zeros((len(kx), len(ky),2, 2), dtype=complex)
    H[...,0,0] = -2*t*(np.cos(kx)+np.cos(ky)) - mu
    H[...,1,1] = 2*t*(np.cos(kx)+np.cos(ky)) + mu
    H[...,0,1] = -2*1j*Delta*(np.sin(kx) - 1j*np.sin(ky))
    H[...,1,0] = 2*1j*Delta*(np.sin(kx) + 1j*np.sin(ky))
    return H


def Chern(N, t, mu, Delta):
    chern  = 0


    # Define the points in the Brillouin zone which is a parallelogram formed by the reciprocal lattice vectors
    kx_values = np.linspace(-np.pi, np.pi, N, endpoint=False)  # Don't inlcude endpoint as it is same as starting point due to PBCs
    ky_values = np.linspace(-np.pi, np.pi, N, endpoint=False)

    kx, ky = np.meshgrid(kx_values, ky_values, indexing='ij')  # Create a meshgrid for the kx and ky values

    # The rest of the code should now proceed as the square lattice case
    # Check this by reproducing the Haldane model results


    H = Ham(kx, ky, t, mu, Delta)
    _, eigenvec = np.linalg.eigh(H)

    eigenvecs_Array = eigenvec[..., 0]  # Only interested in the lowest band as this is the filled band

    #Shape is (N,N, 2,2) -> (N,N,2,1) where 2 is the size of the eignevector
    # For every (kx,ky) we have 1 eigenvector

    # Shift eigenvectors to get neighbors in order to compute overlaps.
    # The roll naturally incoprporates periodic boundary conditions
    eigvecs_right = np.roll(eigenvecs_Array, shift=-1, axis=0)  # Shift along kx (right neighbor)
    eigvecs_up = np.roll(eigenvecs_Array, shift=-1, axis=1)     # Shift along ky (up neighbor)
    eigvecs_diag = np.roll(eigvecs_right, shift=-1, axis=1)     # Diagonal neighbor (right and up)

    # Compute overlaps for all plaquettes and bands simultaneously

    P1 = np.einsum('ijk,ijk->ij', np.conj(eigenvecs_Array), eigvecs_right)
    P1 /= np.abs(P1)

    P2 = np.einsum('ijk,ijk->ij', np.conj(eigvecs_right), eigvecs_diag)
    P2 /= np.abs(P2)

    P3 = np.einsum('ijk,ijk->ij', np.conj(eigvecs_diag), eigvecs_up)
    P3 /= np.abs(P3)

    P4 = np.einsum('ijk,ijk->ij', np.conj(eigvecs_up), eigenvecs_Array)
    P4 /= np.abs(P4)

    # Compute the plaquette phase for all plaquettes and bands, by combining the 4 overlaps
    plaquette_phase = 1j * np.log(P1 * P2 * P3 * P4)  #Shape (N, N, 2)
    # Sum over the bands and plaquettes

    chern = np.sum(plaquette_phase)

    chern = chern/(2*np.pi)
    chern = chern.real #Take real part to get rid of very small imaginary part due to numerical errors. Then want absolute value

    return round(chern,2)   


t= 0.5
Delta = 0.5
N=21
mu_values = np.linspace(-10, 10, 1000)


Chern_values = []
for mu in tqdm(mu_values):
    chern_number = Chern(N, t, mu, Delta)
    Chern_values.append(chern_number)


plt.rcParams['font.size'] = '18'


plt.figure(figsize=(16,10))

plt.plot(mu_values, Chern_values)
plt.xlabel(r'$\mu$')
plt.ylabel(r'$C$', rotation=0, labelpad=15)
plt.savefig('../mpags-topological/_static/plots/p_ip_Chern.svg')
plt.yticks([-1, 0, 1], ['-1', '0', '1'])
plt.xticks([-10, -8,-6, -4 ,-2, 0, 2,4,6,8,10], 
           ['-10', '-8','-6', '-4' ,'-2', '0', '2','4','6','8','10'])
plt.show()
