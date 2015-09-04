from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def f(x,y):
    r = np.sqrt(x**2+y**2)
    result = np.sin(r)
    result[r==1] = 1.0
    return result
    
x_ticks = np.linspace(-10,10,51)
y_ticks = np.linspace(-10,10,51)
x, y = np.meshgrid(x_ticks, y_ticks, sparse=False)
Z = 4*f(x,y)

fig = plt.figure()
ax = fig.gca(projection='3d')
#X, Y, Z = axes3d.get_test_data(0.05)
surf = ax.plot_surface(x,y, Z, rstride=1, cstride=1, cmap=cm.RdPu,
        linewidth=0, antialiased=False)
cset = ax.contour(x,y, Z, zdir='z', offset=-10, cmap=cm.coolwarm)
cset = ax.contour(x,y, Z, zdir='x', offset=-20, cmap=cm.coolwarm)
cset = ax.contour(x,y, Z, zdir='y', offset= 20, cmap=cm.coolwarm)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_xlabel('X')
ax.set_xlim(-20, 20)
ax.set_ylabel('Y')
ax.set_ylim(-20, 20)
ax.set_zlabel('Z')
ax.set_zlim(-10, 10)

plt.show()