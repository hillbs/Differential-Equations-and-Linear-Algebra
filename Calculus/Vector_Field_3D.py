from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from mayavi import mlab

#fig = plt.figure()
#ax = fig.gca(projection='3d')
#
x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.8))

u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
     np.sin(np.pi * z))

mlab.quiver3d(x, y, z, u, v, w)
#def V(x, y, z):
#    """ A 3D sinusoidal lattice with a parabolic confinement. """
#    return (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) * np.sin(np.pi * z))
#X, Y, Z = np.mgrid[-2:2:100j, -2:2:100j, -2:2:100j]
#mlab.contour3d(X, Y, Z, V)
plt.show()