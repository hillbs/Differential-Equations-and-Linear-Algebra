import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca()
t = np.linspace(-4, 4, 100)
x = 2*np.exp(-t)+np.exp(-6*t)
y = 1*np.exp(-t)-2*np.exp(-6*t)
ax.plot(x, y, label='parametric curve')
ax.set_xscale('log')
ax.set_yscale('log')
ax.legend()
plt.show()