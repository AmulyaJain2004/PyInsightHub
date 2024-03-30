from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 

# x = random.poisson(lam=2, size=10)
# print(x)

sns.kdeplot(random.normal(loc=50, scale=7, size=1000), label='Normal Distribution')
sns.kdeplot(random.poisson(lam=50, size=1000), label='Poisson Distribution')

plt.legend()
plt.show()
