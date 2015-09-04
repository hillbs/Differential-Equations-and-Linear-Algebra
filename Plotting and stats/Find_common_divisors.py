				
#!/usr/bin/python
# Filename: Find_common_divisors.py
import matplotlib.pylab as pl

def findCommonDivisors(n1, n2):
    """assumes that n1 and n2 are positive ints
       returns a tuple containing the common divisors of n1 and n2"""
    divisors = () # the empty tuple
    for i in range(1, min(n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            divisors = divisors + (i,)
    return divisors

def findDivisors(n):
    """assumes that n is a positive int
       returns a tuple containing the divisors of n"""
    divisors = () # the empty tuple
    for i in range(1, n + 1):
        if n%i == 0:
            divisors = divisors + (i,)
    return divisors
    
def prod_sum(prod, diff):
	factors = findDivisors(prod)
	difference = []
	if len(factors) == 2:
		print 'This is a prime number; there are only two factors', prod,' and 1.'
	print 'Equation to solve: x * y =',prod,' and |x-y| =', diff
	print
	if factors :#len(factors)%2 == 0:
		for n in range(0,len(factors)/2):
			k = len(factors)-n - 1
			#print n, ' ',k 
			print factors[n], ' ' ,factors[k]
			difference.append(factors[k]-factors[n])
			if factors[k]-factors[n] == diff:
				print 'Solution:',factors[n], '*', factors[k] ,'=', factors[n]*factors[k], 
				print ' and ',factors[k], '-', factors[n], '=', diff 
	print 'Differences: ', difference
	print 'Factors: ',factors
#	pl.close()
#	pl.grid()
#	pl.plot(range(1,len(factors)+1),factors)
#	pl.plot(range(1,(len(factors)/2) + 1), difference)
#	pl.show()
	return factors, difference

if __name__ == "__main__":
	try:
		print 'These are the points where the two functions are equal'
		print '='*60
#	prod_sum(60,7)
		factors = prod_sum(144,7)
		print '='*60
	except OverflowError:
		print 'Number too large Seth'
	


