import numpy as np
import matplotlib.pyplot as plt

def heaviside(x):
    """See http://stackoverflow.com/a/15122658/554319"""
    y = 0.5 * (np.sign(x) + 1)
    y[np.diff(y) >= 0.1] = np.nan
    print y
    return y

x = np.linspace(-1, 1)
plt.plot(x, heaviside(x))
plt.ylim(-1, 2)
plt.show()