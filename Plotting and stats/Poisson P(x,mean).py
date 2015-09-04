import math
def poisson_probability(actual, mean):
    '''Calculates the probability that an actual event, like 3 house sales, will occur on any one 
    day where the mean is 5 sales'''
    # naive:   math.exp(-mean) * mean**actual / factorial(actual)
    # iterative, to keep the components from getting too large or small:
    
    p = math.exp(-mean)
    for i in xrange(actual):
        p *= mean
        p /= i+1
    return float(p)
    
print poisson_probability(1,3) + poisson_probability(0,3)

# Or use the inbuilt function
x = round(poisson_probability(4,3),11)
print x
