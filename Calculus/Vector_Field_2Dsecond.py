import matplotlib.pyplot as plt
import numpy as np
from mayavi import mlab
x, y,z = np.meshgrid(np.arange(-0.8, 1, 0.2),np.arange(-0.8, 1, 0.2),np.arange(-0.8, 1, 0.2))
u = -y
v = x
w = z
mlab.quiver3d(x, y,z, u, v, w)
plt.show()