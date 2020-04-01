import matplotlib.pyplot as plt
import math
import numpy as np
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rcParams.update({'font.size': 25})

filename = 'rotate/gps.txt'
X,Y = [],[]
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        value = [float(s) for s in line.split()]
        X.append(value[0])
        Y.append(value[1])
the = 0
# the = 0.671
Xc,Yc,Xs,Ys = [],[],[],[]
Xc[:] = [math.cos(the)*x for x in X]
Ys[:] = [-math.sin(the)*y for y in Y]
Xs[:] = [math.sin(the)*x for x in X]
Yc[:] = [math.cos(the)*y for y in Y]
X = [Xc[i] + Ys[i] for i in range(len(X))]
Y = [Xs[i] + Yc[i] for i in range(len(Y))]
outF = open("rotate/gps_.txt", "w")
for i in range(len(X)):
    outF.write("%f\t%f\n" %(X[i],Y[i]))
outF.close()
plt.plot(X, Y, color='black', linestyle='-', linewidth=2, label='Ground Truth')
plt.plot(X[len(X)-1], Y[len(Y)-1], color='black', marker="d", markersize=14,label='End')

filename = 'rotate/all.txt'
X,Y = [],[]
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        value = [float(s) for s in line.split()]
        X.append(value[0])
        Y.append(value[1])
Xc,Yc,Xs,Ys = [],[],[],[]
Xc[:] = [math.cos(the)*x for x in X]
Ys[:] = [-math.sin(the)*y for y in Y]
Xs[:] = [math.sin(the)*x for x in X]
Yc[:] = [math.cos(the)*y for y in Y]
X = [Xc[i] + Ys[i] for i in range(len(X))]
Y = [Xs[i] + Yc[i] for i in range(len(Y))]
outF = open("rotate/all_.txt", "w")
for i in range(len(X)):
    outF.write("%f\t%f\n" %(X[i],Y[i]))
outF.close()
plt.plot(X, Y, color='red', linestyle='-', linewidth=2, label='All')

filename = 'rotate/back.txt'
X,Y = [],[]
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        value = [float(s) for s in line.split()]
        X.append(value[0])
        Y.append(value[1])
Xc,Yc,Xs,Ys = [],[],[],[]
Xc[:] = [math.cos(the)*x for x in X]
Ys[:] = [-math.sin(the)*y for y in Y]
Xs[:] = [math.sin(the)*x for x in X]
Yc[:] = [math.cos(the)*y for y in Y]
X = [Xc[i] + Ys[i] for i in range(len(X))]
Y = [Xs[i] + Yc[i] for i in range(len(Y))]
outF = open("rotate/back_.txt", "w")
for i in range(len(X)):
    outF.write("%f\t%f\n" %(X[i],Y[i]))
outF.close()
# plt.plot(X, Y, color='cyan', linestyle='-', linewidth=2, label='Fr-Bl-Br')

filename = 'rotate/one.txt'
X,Y = [],[]
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        value = [float(s) for s in line.split()]
        X.append(value[0])
        Y.append(value[1])
Xc,Yc,Xs,Ys = [],[],[],[]
Xc[:] = [math.cos(the)*x for x in X]
Ys[:] = [-math.sin(the)*y for y in Y]
Xs[:] = [math.sin(the)*x for x in X]
Yc[:] = [math.cos(the)*y for y in Y]
X = [Xc[i] + Ys[i] for i in range(len(X))]
Y = [Xs[i] + Yc[i] for i in range(len(Y))]
outF = open("rotate/one_.txt", "w")
for i in range(len(X)):
    outF.write("%f\t%f\n" %(X[i],Y[i]))
outF.close()
# plt.plot(X, Y, color='green', linestyle='-', linewidth=2, label='Single')

filename = 'rotate/lr.txt'
X,Y = [],[]
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        value = [float(s) for s in line.split()]
        X.append(value[0])
        Y.append(value[1])
Xc,Yc,Xs,Ys = [],[],[],[]
Xc[:] = [math.cos(the)*x for x in X]
Ys[:] = [-math.sin(the)*y for y in Y]
Xs[:] = [math.sin(the)*x for x in X]
Yc[:] = [math.cos(the)*y for y in Y]
X = [Xc[i] + Ys[i] for i in range(len(X))]
Y = [Xs[i] + Yc[i] for i in range(len(Y))]
outF = open("rotate/lr_.txt", "w")
for i in range(len(X)):
    outF.write("%f\t%f\n" %(X[i],Y[i]))
outF.close()
# plt.plot(X, Y, color='blue', linestyle='-', linewidth=2, label='Fr-L-R')

plt.plot(0, 0, color='gold', marker='*', markersize=20, label='Start')
# plt.plot(X[len(X)-1], Y[len(Y)-1], color='black', marker="d", markersize=14,label='End')

# plt.annotate('ekf', xy=(100, 1), xytext=(50, 10),arrowprops=dict(facecolor='green', shrink=0.05))
# plt.annotate('gps', xy=(100, -2), xytext=(50, -10),arrowprops=dict(facecolor='blue', shrink=0.05))

plt.xlabel('x (m)')
plt.ylabel('y (m)')
# plt.ylim((-25,175))
# plt.xlim((-25,175))
plt.xlim((-50,500))
plt.ylim((-350,200))
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)

plt.title('Scene-1')
plt.legend(numpoints=1,loc='upper left',ncol=2)
plt.show()