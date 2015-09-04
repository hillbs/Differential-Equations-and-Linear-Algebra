import pandas
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rv_discrete
df = pandas.read_csv('Ebola.txt',  usecols=(1,2,3,4,5,6))
df = df.sort('Year', ascending=False )
grouped = df.groupby('Country')
# The next section is generating its own pmf to estimate the probability
#that a country will have a death based on mortality rate.
#xk = ['Congo', 'Gabon', 'Sudan', 'Uganda', Guinea, Liberia, Nigeria, SL]
xk = [1,2,3,4,5,6]
pk = [976.0/4233.0, 150.0/4233.0, 180.0/4233.0, 283.0/4233.0, 494/4233.0 , 897/4233.0 , 7/4233.0 , 476/4233.0  ]#check = 1
loaded = rv_discrete(values=(xk, pk))      
samples = loaded.rvs(size=1000)
bins = np.linspace(0, 8, 16)
plt.title(r'$Probability\ distribution\ of\ deaths\ against\ past\ deaths$')
h = plt.hist(samples, bins=bins, normed=True, label='Predicted cases by country', color='g')
s = plt. stem(xk, loaded.pmf(xk), markerfmt= 'ro', linefmt='r-')
plt.text(6, .7, ' 1 = Congo\n 2 = Gabon\n 3 = Sudan\n 4 = Uganda\n 5 = Guinea\n 6 = Liberia\n 7 = Nigeria\n 8 = Sierra ', fontsize=10)
plt.grid()
plt.show()

# Summary of main dataframe structure
print df.head()
