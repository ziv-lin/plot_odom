import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

pose = np.genfromtxt('error.txt')

plt.subplot(2,1,1)
plt.xlabel('distance (m)')
plt.ylabel('translation error (m)')
plt.plot(pose[:,0],pose[:,1],color='magenta',linewidth=1.5,label='total error')
plt.plot(pose[:,0],pose[:,2],color='orange',linewidth=1.5,label='x error')
plt.plot(pose[:,0],pose[:,3],color='teal',linewidth=1.5,label='y error')
plt.xticks(range(0,450,50))
plt.yticks(np.arange(0,1,0.1))
plt.legend(loc='upper left')

plt.subplot(2,1,2)
plt.xlabel('distance (m)')
plt.ylabel('error / distance')
plt.plot(pose[:,0],pose[:,4],color='red',linewidth=1.5)
plt.xticks(range(0,450,50))
plt.hlines(0.002, 0, 450, colors='teal', linestyles='dashed', linewidth=1.5)

plt.show()