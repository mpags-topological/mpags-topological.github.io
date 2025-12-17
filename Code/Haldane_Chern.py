# Calculate the Chern number for the Haldane model

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm



def Ham(kx, ky, t1, t2, M, phi):
    """
    Haldane model Hamiltonian
    This has been vectorised to work with kx and ky arrays
    """

    d0 = t2*np.cos(phi)*(np.cos(-np.sqrt(3)*kx) + np.cos(0.5*(np.sqrt(3)*kx + 3*ky)) + np.cos(0.5*(np.sqrt(3)*kx - 3*ky)))
    dx = 0.5*t1*(np.cos(ky) + np.cos(0.5*(-np.sqrt(3)*kx-ky)) + np.cos(0.5*(np.sqrt(3)*kx-ky)))
    dy = -0.5*t1*(np.sin(ky) + np.sin(0.5*(-np.sqrt(3)*kx-ky)) + np.sin(0.5*(np.sqrt(3)*kx-ky)))
    dz = 0.5*M - t2*np.sin(phi)*(np.sin(-np.sqrt(3)*kx) + np.sin(0.5*(np.sqrt(3)*kx + 3*ky)) + np.sin(0.5*(np.sqrt(3)*kx - 3*ky)))

    H = np.zeros((len(kx), len(ky),2, 2), dtype=complex)
    H[...,0,0] = d0 + dz
    H[...,1,1] = d0 - dz
    H[...,0,1] = dx - 1j*dy
    H[...,1,0] = dx + 1j*dy
    return H


def Chern(N, t1, t2, M, phi):
    chern  = 0


    # Define the points in the Brillouin zone which is a parallelogram formed by the reciprocal lattice vectors
    alpha_values = np.linspace(0, 1, N, endpoint=False)  # Don't inlcude endpoint as it is same as starting point due to PBCs
    beta_values = np.linspace(0, 1, N, endpoint=False)

    alpha, beta = np.meshgrid(alpha_values, beta_values, indexing='ij')  # Create a meshgrid for the kx and ky values


    # Want to convert to kx, ky coordinates as Hamiltonian is defined in these coordinates
    kx = 2*np.pi*(alpha-beta)/np.sqrt(3)
    ky = 2*np.pi*(alpha+beta)/3

    # The rest of the code should now proceed as the square lattice case
    # Check this by reproducing the Haldane model results


    H = Ham(kx, ky, t1, t2, M, phi)
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



t1 = 1
t2 = 1 

N = 21

phi_values = np.linspace(-np.pi, np.pi, 250)
M_values = np.linspace(-6, 6, 250)

Chern_values = []
for M in tqdm(M_values):
    for phi in phi_values:
        chern_number = Chern(N, t1, t2, M, phi)
        Chern_values.append(chern_number)

Chern_values = np.array(Chern_values).reshape(len(M_values), len(phi_values))


plt.rcParams['font.size'] = '18'


plt.figure(figsize=(16,10))

plt.imshow(Chern_values, extent=[phi_values[0], phi_values[-1], M_values[0], M_values[-1]],
           origin='lower', aspect='auto', cmap='viridis', interpolation='bicubic', rasterized=True)

#plt.pcolormesh(phi_values, M_values, Chern_values, shading='gouraud')
cbar = plt.colorbar(label=r'Chern Number')
cbar.set_ticks([-1, 0, 1])
cbar.set_ticklabels(['-1', '0', '1'])
cbar.set_label(r'$C$', rotation=0, labelpad=15)
plt.xlabel(r'$\varphi$')
plt.ylabel(r'$M$', rotation=0)
plt.yticks([-3*np.sqrt(3), 0, 3*np.sqrt(3)], [r'$-3\sqrt{3}$', '0', r'$3\sqrt{3}$'])
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$'])

plt.savefig('../mpags-topological/_static/plots/Haldane_Chern.svg')
#plt.show()
