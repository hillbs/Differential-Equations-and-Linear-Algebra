import numpy as np
import matplotlib.pylab as plt
import matplotlib.axes 

def rDist(r,sd1 = 10, sd2 = 10):
	mup = 50 + (100*(r/2))
	mlow = 50 - (100*(r/2))
	y2 = np.random.normal(mup,sd1,10000)
	y1 = np.random.normal(mlow,sd1,10000)
	plt.grid(True)
	plt.hist(y1,50, label = '$Control\ Group$', alpha = .7, color = 'b')
	plt.hist(y2,50, label = '$Experimental\ Group$', alpha = .5, color = 'g')
	plt.xlim(0, 100)
	plt.legend(	loc= 'right')
	plt.title('$Binomial\ Effect\ Size\ Display\ (BESD).$')
	plt.xlabel('Bin number for each one percentage bin')
	plt.ylabel('Frequency of each value occurring')
	plt.axvline(mup, ms = 3, color= 'r')
	plt.axvline(mlow, ms = 3, color = 'r')
	plt.show()
	return

def normScatter():
	x3 = np.arange(1000)
	y3 = np.random.normal(50, 1,1000)
	y4 = np.random.normal(50, 10,1000)
	plt.axis([0,1000,0,100])
	plt.title('Normal Distribution Scatter Plot')
	plt.xlabel('Order of generation (i)')
	plt.ylabel('Value of number generated (y[i])')
	plt.plot(x3,y3, 'b+', label = 'SD = 1')
	plt.plot(x3,y4, 'g+', label = 'SD = 10')
	plt.legend( loc = 'upper right', markerscale = 2, shadow = True, frameon = True)
	plt.show()
	return
	
plt.close()	
rDist(.22)
#normScatter()	
