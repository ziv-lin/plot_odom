import matplotlib.pyplot as plt
import math
import numpy as np
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

filename = 'gps_02/gps.txt'
X,Y = [],[]
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        value = [float(s) for s in line.split()]
        X.append(value[1])
        Y.append(value[2])

# s = 0.996
s = 0.999
X[:] = [(x - X[0])*s for x in X]
Y[:] = [(y - Y[0])*s for y in Y]

# the = -0.671
the = -0.702
Xc,Yc,Xs,Ys = [],[],[],[]
Xc[:] = [math.cos(the)*x for x in X]
Ys[:] = [-math.sin(the)*y for y in Y]
Xs[:] = [math.sin(the)*x for x in X]
Yc[:] = [math.cos(the)*y for y in Y]

X = [Xc[i] + Ys[i] for i in range(len(X))]
Y = [Xs[i] + Yc[i] for i in range(len(Y))]

outF = open("gps_unorder.txt", "w")
for i in range(len(X)):
    outF.write("%f\t%f\n" %(X[i],Y[i]))
outF.close()

filename = 'gps_02/ekf.log'
X1,Y1 = [],[]
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        value = [float(s) for s in line.split()]
        X1.append(value[4])
        Y1.append(value[5])

X1[:] = [x - X1[0] for x in X1]
Y1[:] = [y - Y1[0] for y in Y1]

outF = open("ekf_unorder.txt", "w")
for i in range(len(X1)):
    outF.write("%f\t%f\n" %(X1[i],Y1[i]))
outF.close()

plt.plot(X, Y, linewidth=3)
plt.plot(X1, Y1, linestyle=':', linewidth=3)
# plt.annotate('ekf', xy=(100, 1), xytext=(50, 10),arrowprops=dict(facecolor='green', shrink=0.05))
# plt.annotate('gps', xy=(100, -2), xytext=(50, -10),arrowprops=dict(facecolor='blue', shrink=0.05))
# plt.ylim((-200,500))
# plt.xlim((-200,500))
# plt.gca().set_aspect('equal', adjustable='box')
plt.show()