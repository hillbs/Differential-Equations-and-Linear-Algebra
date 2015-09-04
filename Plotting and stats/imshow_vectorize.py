import numpy as np
import matplotlib.pylab as pl
def sinc(x):
    if x == 0:
        return 1.0
    else:
        w = np.pi * x
        return np.sin(w)/w
        
vsinc = np.vectorize(sinc) # allows functions to operate on arrays
x = np.linspace(-50,50,1001)
#pl.plot(x, vsinc(x))
#pl.grid()
#pl.show()

y = vsinc(x)
y = x[:,np.newaxis] # creates two 1 dim arrays that can havea binary operation on them
data = x*y
pl.imshow(data) # really cool quick function to illustrate data
pl.show()