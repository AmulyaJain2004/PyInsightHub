from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 

# x = random.uniform(size=(5,10))
# print(x)
# for uniform distribution
sns.kdeplot(random.uniform(size=1000))
plt.show()
