from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-2, 2, 0.25)
xlen = len(X)
Y = np.arange(-2, 2, 0.25)
ylen = len(Y)
X, Y = np.meshgrid(X, Y)
Z = X**2 + Y**2
Z2 = 4 - X**2 -Y**2
surf = ax.plot_surface(X, Y, (Z), rstride=1, cstride=1,   linewidth=0, color='g',alpha=0.5, antialiased=False)
surf2 = ax.plot_surface(X, Y, (Z2), rstride=1, cstride=1, linewidth=0, alpha=0.7, antialiased=False)
plt.show()
