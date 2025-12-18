import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes




#Define the Hamiltonian

t1 = [1, 0.6]
t2 = [0.6,1]

N = 15 # There are 2N sites in total

H1 = np.zeros((2*N, 2*N), dtype=np.float64)
H2 = np.zeros((2*N, 2*N), dtype=np.float64)


for i in range(N):
    H1[2*i-1, 2*i] = t2[0]
    H1[2*i, 2*i-1] = t2[0]
    H1[2*i+1, 2*i] = t1[0]
    H1[2*i, 2*i+1] = t1[0]
    H1[-1,0] = 0
    H1[0,-1] = 0   

    H2[2*i-1, 2*i] = t2[1]
    H2[2*i, 2*i-1] = t2[1]
    H2[2*i+1, 2*i] = t1[1]
    H2[2*i, 2*i+1] = t1[1]
    H2[-1,0] = 0
    H2[0,-1] = 0   

energies1 = np.linalg.eigh(H1)[0]
eigenvectors1 = np.linalg.eigh(H1)[1]

energies2 = np.linalg.eigh(H2)[0]
eigenvectors2 = np.linalg.eigh(H2)[1]


index1 = np.argmin(np.abs(energies1)) 
index2 = np.argmin(np.abs(energies2))



# #This gives the probability of being on each site for one of the middle energy eignevalues
Probabilities1 =[]
Probabilities2 =[]
for i in range(2*N):
    prob1 = np.conjugate(eigenvectors1[i][index1]) * eigenvectors1[i][index1]  
    prob2 = np.conjugate(eigenvectors2[i][index2]) * eigenvectors2[i][index2]
    Probabilities1.append(prob1)
    Probabilities2.append(prob2)

plt.rcParams['font.size'] = '14'

fig, (ax1, ax2) = plt.subplots(1,2,figsize=(16,8), layout='constrained')

for i in range(2*N):
    ax1.bar(i+1, Probabilities1[i], color='tab:blue')
    ax2.bar(i+1, Probabilities2[i], color='tab:blue')

ax1.set_title(r'$t_1=1$, $t_2=0.6$', fontsize=16)
ax2.set_title(r'$t_1=0.6$, $t_2=1$', fontsize=16)

ax1.set_xlabel('Site', fontsize=14)
ax2.set_xlabel('Site', fontsize=14)
ax1.set_ylabel(r'$|\psi|^2$', fontsize=14, rotation=0, labelpad=10)
ax2.set_ylabel(r'$|\psi|^2$', fontsize=14, rotation=0, labelpad=10)

ax1.set_xticks([1,5,10,15,20,25,30])
ax2.set_xticks([1,5,10,15,20,25,30])

axins1 = inset_axes(ax1, width="25%", height="20%", loc="upper right",borderpad=1)
axins2 = inset_axes(ax2, width="25%", height="20%", loc="upper center",borderpad=1)

axins1.axhline(y=0, linestyle='--', color='black')
axins2.axhline(y=0, linestyle='--', color='black')

# Plot energy spectrum
for i in range(2*N):
    if i == index1:
        axins1.plot(np.full(1, i+1), energies1[i], 'o', markersize=3, color="tab:orange")
    else:
        axins1.plot(np.full(1, i+1), energies1[i], 'o', markersize=3, color="black")
    if i == index2:
        axins2.plot(np.full(1, i+1), energies2[i], 'o', markersize=3, color="tab:orange")
    else:
        axins2.plot(np.full(1, i+1), energies2[i], 'o', markersize=3, color="black")





# Labels and ticks

axins1.set_ylabel(r'$\varepsilon$', rotation=0, fontsize=16, labelpad=2)
axins1.set_xticks([])
axins1.tick_params(axis="both", labelsize=12, colors='black')

axins2.set_ylabel(r'$\varepsilon$', rotation=0, fontsize=16, labelpad=2)
axins2.set_xticks([])
axins2.tick_params(axis="both", labelsize=12, colors='black')

plt.savefig('../mpags-topological/_static/plots/SSH_RealSpace.svg')
#plt.show()
