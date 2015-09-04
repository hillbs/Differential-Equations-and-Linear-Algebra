import math
import matplotlib.pylab as plt

def Benford(d):
	'''Returns the probability that the first digit will be d'''
	P = math.log10(1 + (1.0/(float(d)))) 
	return P
	
def Output():
	y = []
	for i in range(1,10): # min and max x
		 y.append(Benford(i))
	return y

plt.close()
print Output()	
y = Output()
x = plt.arange(1,10)
plt.axis([0,10,0,.5])
plt.xticks([k for k in range(1,10)]) 
plt.plot(x,y, 'bo', markersize = 9)
plt.title("Benford's Law \n A decimal probability distribution")
plt.xlabel('Decimal digit (d)')
plt.ylabel('P(d) will occur')
plt.show()
plt.savefig('Benford.pdf')
#plt.close()
