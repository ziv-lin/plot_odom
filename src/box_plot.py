import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rcParams.update({'font.size': 30})

filename = "error.txt"
data = np.genfromtxt(filename)
print('number of pose: ',len(data))
fold = int(round(len(data)/8))
labels = range(0,450,50)
# fold = int(round(len(data)/10))
# labels = range(0,550,50)
chunks = [data[x:x+fold,1] for x in xrange(0, len(data), fold)]
plt.boxplot(chunks, boxprops=dict(linewidth=3), medianprops=dict(linewidth=2.5, linestyle='-'), labels=labels, sym ="o")
# plt.boxplot(chunks, sym ="o")
plt.xlabel('Distance (m)')
plt.ylabel('Translation error (m)')
plt.title('Scene-2')
plt.show()