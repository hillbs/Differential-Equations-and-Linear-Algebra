import matplotlib as plt
import numpy as np

x1 = plt.pylab.arange(0,500)
y1 = np.random.normal(100,15,500000)
plt.pylab.hist(y1, bins = 100, color = 'g')
plt.pylab.show()
