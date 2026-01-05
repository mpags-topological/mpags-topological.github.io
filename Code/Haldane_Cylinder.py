import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

from matplotlib.collections import LineCollection
from matplotlib.colors import Normalize
import matplotlib.cm as cm

def Ham(N, ky, t1, t2, M, phi):
    H = np.zeros((2*N, 2*N), dtype=complex)

    for i in range(N):
        H[2*i, 2*i] = M
        H[2*i+1, 2*i+1] = -M

        H[2*i, (2*i+1)] += t1*np.exp(1j*ky)
        H[(2*i+1), 2*i] += t1*np.exp(-1j*ky)

        if i > 0:
            H[2*i, (2*(i-1)+1)] += t1*np.exp(-1j*ky/2)
            H[(2*(i-1)+1), 2*i] += t1*np.exp(1j*ky/2)

        if i < N-1:
            H[2*i, (2*(i+1)+1)] += t1*np.exp(-1j*ky/2)
            H[(2*(i+1)+1), 2*i] += t1*np.exp(1j*ky/2)

            H[2*i, 2*(i+1)] += t2*np.exp(1j*phi)*np.exp(1j*3*ky/2)
            H[2*(i+1), 2*i] += t2*np.exp(-1j*phi)*np.exp(-1j*3*ky/2)

            H[2*i+1, 2*(i+1)+1] += t2*np.exp(-1j*phi)*np.exp(1j*3*ky/2)
            H[2*(i+1)+1, 2*i+1] += t2*np.exp(1j*phi)*np.exp(-1j*3*ky/2)

            H[2*i, 2*(i+1)] += t2*np.exp(1j*phi)*np.exp(-1j*3*ky/2)
            H[2*(i+1), 2*i] += t2*np.exp(-1j*phi)*np.exp(1j*3*ky/2)

            H[2*i+1, 2*(i+1)+1] += t2*np.exp(-1j*phi)*np.exp(-1j*3*ky/2)
            H[2*(i+1)+1, 2*i+1] += t2*np.exp(1j*phi)*np.exp(1j*3*ky/2)

        if i > 2:
            H[2*i, 2*(i-2)] += t2*np.exp(1j*phi)
            H[2*(i-2), 2*i] += t2*np.exp(-1j*phi)

            H[2*i+1, 2*(i-2)+1] += t2*np.exp(-1j*phi)
            H[2*(i-2)+1, 2*i+1] += t2*np.exp(1j*phi)

    return H

# Parameters
N=100
t1 = 1.0
t2 = 1
M = 2
phi = -np.pi/2

ky= np.linspace(-np.pi/3, np.pi/3, 101)

E_k = [ [] for i in range(2*N)]
Average_X = [ [] for i in range(2*N)]

site_positions = np.array([np.floor(j/2)+1 for j in range(2*N)])

for k in tqdm(ky):
    H = Ham(N, k, t1, t2, M, phi)
    energies, eigenvecs = np.linalg.eigh(H)

    idx = energies.argsort()[::-1]   
    energies_sort = energies[idx]
    eigenvecs_sort = eigenvecs[:,idx]

    probs = np.abs(eigenvecs_sort)**2  #Calculate the probabilities of each state
    x_av = np.dot(site_positions, probs)  #Calculate the average position for each state

    for i in range(2*N):
        E_k[i].append(energies_sort[i])
        Average_X[i].append(x_av[i])

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "Times"})
plt.rcParams['font.size'] = '38'


# Set up color normalization and colormap
norm = Normalize(vmin=1, vmax=N)
cmap = cm.coolwarm  # Choose a colormap   cm.inferno looks more appealing in my opinion. coolwarm gives a diverging colourbar so easier to indentify the interesting modes


fig, ax = plt.subplots(figsize=(16,10))
for i in range(2*N):
    points = np.array([ky, E_k[i]]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    # Create a LineCollection with the segments and colors
    lc = LineCollection(segments, cmap=cmap, norm=norm)
    lc.set_array(Average_X[i])
    lc.set_linewidth(2) 
    ax.add_collection(lc)
    ax.autoscale()
cbar=plt.colorbar(lc, ax=ax, label=r'$\langle x \rangle$')
cbar.set_label(r'$\langle x \rangle$', rotation=0, labelpad=15)
plt.xlim([-np.pi/3, np.pi/3])
plt.xticks([-np.pi/3, 0, np.pi/3],
           [r'$-\pi/3$', '0', r'$\pi/3$'])
plt.ylim([-3, 3])
plt.ylabel(r'$\varepsilon$', rotation=0)
plt.xlabel(r'$k_y$', labelpad=-12)
plt.savefig('../mpags-topological/_static/plots/Haldane_Cylinder.svg')

#plt.show()

