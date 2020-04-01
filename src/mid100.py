import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

# pose = np.genfromtxt('mid_03/mid100_0.log')
# plt.plot(pose[:,4]-pose[0,4], pose[:,5]-pose[0,5], color='cyan', linewidth=1.5, label='MID-100')

pose = np.genfromtxt('mid_03/mid100_and_back.log')
plt.plot(pose[:,4]-pose[0,4], pose[:,5]-pose[0,5], color='cyan', linestyle='-', linewidth=1.5, label='MID-100-Back')
outF = open("rotate/back.txt", "w")
for i in range(len(pose)):
    outF.write("%f\t%f\n" %(pose[i,4]-pose[0,4],pose[i,5]-pose[0,5]))
outF.close()

pose = np.genfromtxt('mid_03/mid100_and_lr.log')
plt.plot(pose[:,4]-pose[0,4], pose[:,5]-pose[0,5], color='blue', linestyle='-', linewidth=1.5, label='MID-100-LR')
outF = open("rotate/lr.txt", "w")
for i in range(len(pose)):
    outF.write("%f\t%f\n" %(pose[i,4]-pose[0,4],pose[i,5]-pose[0,5]))
outF.close()

pose = np.genfromtxt('mid_03/mid100_one_lidar.log')
plt.plot(pose[:,4]-pose[0,4], pose[:,5]-pose[0,5], color='green', linestyle='-', linewidth=1.5, label='MID-100-One')
outF = open("rotate/one.txt", "w")
for i in range(len(pose)):
    outF.write("%f\t%f\n" %(pose[i,4]-pose[0,4],pose[i,5]-pose[0,5]))
outF.close()

pose = np.genfromtxt('mid_03/ekf.log')
plt.plot(pose[:,4]-pose[0,4], pose[:,5]-pose[0,5], color='black', linestyle='-', linewidth=1.5, label='ALL')
outF = open("rotate/all.txt", "w")
for i in range(len(pose)):
    outF.write("%f\t%f\n" %(pose[i,4]-pose[0,4],pose[i,5]-pose[0,5]))
outF.close()

filename = 'mid_03/gps.txt'
X,Y = [],[]
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        value = [float(s) for s in line.split()]
        X.append(value[1])
        Y.append(value[2])
# s = 0.999
s = 0.999
X[:] = [(x - X[0])*s for x in X]
Y[:] = [(y - Y[0])*s for y in Y]

the = -0.676
# the = -0.702
Xc,Yc,Xs,Ys = [],[],[],[]
Xc[:] = [math.cos(the)*x for x in X]
Ys[:] = [-math.sin(the)*y for y in Y]
Xs[:] = [math.sin(the)*x for x in X]
Yc[:] = [math.cos(the)*y for y in Y]
X = [Xc[i] + Ys[i] for i in range(len(X))]
Y = [Xs[i] + Yc[i] for i in range(len(Y))]
plt.plot(X, Y, color='red', linewidth=2, label='GPS GT')
outF = open("rotate/gps.txt", "w")
for i in range(len(X)):
    outF.write("%f\t%f\n" %(X[i],Y[i]))
outF.close()

plt.legend(loc='lower left')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
# plt.ylim((-50,250))
# plt.xlim((-50,250))
# plt.gca().set_aspect('equal', adjustable='box')
# plt.hlines(0.003, 0, 600, color = 'teal', linestyles = "dashed")
# plt.xticks(range(0,600,50))
# plt.yticks(np.arange(0,2,0.2))
plt.show()