
import numpy
from matplotlib.pyplot import *
import random

#x = [-7.30000, -4.10000, -1.70000, -0.02564,
#     1.50000, 4.50000, 9.10000]
#y = [-0.80000, -0.50000, -0.20000, 0.00000,
#     0.20000, 0.50000, 0.80000]
import math

# calculates the mean
def mean(x) :
    sum = 0.0
    for i in x:
         sum += i
    return sum / len(x) 

# calculates the sample standard deviation
def sampleStandardDeviation(x):
    sumv = 0.0
    for i in x:
         sumv += (i - mean(x))**2
    return math.sqrt(sumv/(len(x)-1))

# calculates the PCC using both the 2 functions above
def pearson(x,y):
    scorex = []
    scorey = []

    for i in x: 
        scorex.append((i - mean(x))/sampleStandardDeviation(x)) 

    for j in y:
        scorey.append((j - mean(y))/sampleStandardDeviation(y))

# multiplies both lists together into 1 list (hence zip) and sums the whole list   
    return (sum([i*j for i,j in zip(scorex,scorey)]))/(len(x)-1)
def NormalDist(mean, SD, num = 15):
	y = []
	for i in range(0,num):
		y.append(random.gauss(mean,SD))
	return y

x = numpy.linspace(1,15,15)
#y = numpy.linspace(2,14,15)
#y = y + numpy.random.randint(4, size = 15)
#y = random.sample(range(15), 15) # purely random number between 0-15
#y = NormalDist(10,5) # y = random normal distribution
stdy = numpy.std(y)
ave_y = mean(y)
coefficients = numpy.polyfit(x, y, 1)
polynomial = numpy.poly1d(coefficients)
ys = polynomial(x)
r = pearson(x,y)
print coefficients
print polynomial
print ave_y
print 'STD = ', stdy
print 'r = ', r
close()
grid(True)
plot(x, y, 'o')
plot(x, ys)
errorbar(x,y,stdy, fmt = None, color = 'r', )
ylabel('Random value y')
xlabel('Integer x')
title('Correlation Matrix \n Random data plus best fit line')
text(6,6,polynomial)
rvalue = 'Pearson r =', round(r,2)
text(1,10,rvalue)
xlim(-.5,16)
ylim(0,16)
show()


