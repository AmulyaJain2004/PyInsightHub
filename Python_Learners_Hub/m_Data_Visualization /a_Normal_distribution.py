from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 

# x= random.normal(loc=1 , scale=2, size=(2,3)) 
# '''
# loc : float or array_like of floats
#     Mean ("centre") of the distribution.
# scale : float or array_like of floats
#     Standard deviation (spread or "width") of the distribution. Must be non-negative.
# '''
#print(x)

#using sns.distplot(random.normal(size=1000), hist = False) distplot is deprecated
# or use below function or or use sns.kdeplot
sns.displot(random.normal(size=1000), kind='kde' ) # kde = kernel density estimate only curve not histogram
plt.show() # in normal distribution is also known as Bell Curve.
