import matplotlib.pylab

##pylab.plot([1,2,3,4], [1,2,3,4])
##pylab.plot([1,4,2,3], [5,6,7,8])
##pylab.show()

##pylab.figure(1)
##pylab.plot([1,2,3,4], [1,2,3,4])
##pylab.figure(2)
##pylab.plot([1,4,2,3], [5,6,7,8])
##pylab.savefig('firstSaved')
##pylab.figure(1)
##pylab.plot([5,6,7,10])
##pylab.savefig('secondSaved')
##pylab.show()

principal = 10000 #initial investment
interestRate = 0.05
freqComp = 12
years = 20
values = []
for i in range(freqComp*years + 1):
    values.append(principal)
    principal += principal*(interestRate/freqComp)
pylab.plot(values)

pylab.title('5% Growth, Compounded Annually')
pylab.xlabel('Years of Compounding')
pylab.ylabel('Value of Principal ($)')

pylab.show()

