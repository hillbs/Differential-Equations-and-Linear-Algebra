import matplotlib.pylab as plt

def DrugElim(n, kr):
	'''Drug elimination based on days = n
	kr is the % drug left after 24 hours plus the new dose'''
#k is 0.5**1/(elim half life/24)	
#	kr = 0.5**(1/(float(t)/24.0))
	if n == 1:
		return 1 + kr
	else:
		return 1 + (kr*DrugElim(n-1, kr))

def yofdrug_elim(i,p):
	y = []
	ans = 0
	for num in range(1,i+1):
		ans = DrugElim(num,p)
		y.append(ans)
	return y

def plotTitration(d, l):
#	d = days
#	l = loss
	y =  yofdrug_elim(d,l)
	x = range(d)
	plt.close()
	plt.axis([min(x)-0.5,max(x)+0.5, 1, 1.1*max(y)])
	plt.plot(x,y, 'b^')
	plt.title('Drug titration rate')
	plt.xlabel('Days')
	plt.ylabel('Percentage of dose in plasma')
	plt.show()

plotTitration(6,.6)
