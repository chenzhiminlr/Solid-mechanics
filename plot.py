import matplotlib.gridspec as gridspec
from matplotlib.ticker import MultipleLocator
import matplotlib as mpl
mpl.rcParams['font.family'] = 'Arial'
import matplotlib.pyplot as plt 
import pickle5 as pickle

# Load data
with open('sigma_strength.pkl','rb') as f:
    sigma = pickle.load(f)
with open('theory_strength.pkl','rb') as f:
    theory = pickle.load(f)
with open('sigma_toughness.pkl','rb') as f:
    sigma_toughness = pickle.load(f)
with open('theory_toughness.pkl','rb') as f:
    theory_toughness = pickle.load(f)

# Plot
fig = plt.figure(tight_layout=True,figsize=(6,3))
gs = gridspec.GridSpec(10, 10)
gs.update(wspace=10, hspace=0.2)
ax = fig.add_subplot(gs[0:,0:5])
ax.plot(sigma[0][0],theory[0][0],'^',color='#3C5E8A',label=r'1 GPa',fillstyle='full',markersize=8,markeredgecolor='k',markeredgewidth=0.5)
ax.plot(sigma[1][0],theory[1][0],'o',color='#CC1E13',label=r'5 GPa',fillstyle='full',markersize=8,markeredgecolor='k',markeredgewidth=0.5)
ax.plot([0,100],[0,100],color='k',linewidth=1.,linestyle='--')
ax.legend(frameon=False,loc='upper left',fontsize=8)
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.xaxis.set_minor_locator(MultipleLocator(2.5))
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(MultipleLocator(2.5))
ax.tick_params(axis='both', which='major', direction = 'out',labelsize = 10)
ax.tick_params(axis='both', which='minor', direction = 'out',labelsize = 10)
ax.set_xlim(10,30)
ax.set_ylim(10,30)
ax.set_xlabel(r'$Strength_{sim}$ (GPa)',fontsize=10)
ax.set_ylabel(r'$Strength_{pred}$ (GPa)',fontsize=10)
ax.text(-0.2, 0.92, 'a', fontsize=16, transform=ax.transAxes, weight='bold')

ax = fig.add_subplot(gs[0:,5:])
ax.plot(sigma_toughness[0][0],theory_toughness[0][0],'^',color='#3C5E8A',label=r'1 GPa',fillstyle='full',markersize=8,markeredgecolor='k',markeredgewidth=0.5)
ax.plot(sigma_toughness[1][0],theory_toughness[1][0],'o',color='#CC1E13',label=r'5 GPa',fillstyle='full',markersize=8,markeredgecolor='k',markeredgewidth=0.5)
ax.plot([0,100],[0,100],color='k',linewidth=1.,linestyle='--')
ax.legend(frameon=False,loc='upper left',fontsize=8)
ax.xaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(2))
ax.yaxis.set_minor_locator(MultipleLocator(1))
ax.tick_params(axis='both', which='major', direction = 'out',labelsize = 10)
ax.tick_params(axis='both', which='minor', direction = 'out',labelsize = 10)
ax.set_xlim(0.05,4)
ax.set_ylim(0.05,4)
ax.set_xlabel(r'$Toughness_{sim}$ (J/m$^3$)',fontsize=10)
ax.set_ylabel(r'$Toughness_{pred}$ (J/m$^3$)',fontsize=10)
ax.text(-0.2, 0.92, 'b', fontsize=16, transform=ax.transAxes, weight='bold')

# Save
plt.savefig('FIG.svg', format='svg', transparent=True, bbox_inches = 'tight')