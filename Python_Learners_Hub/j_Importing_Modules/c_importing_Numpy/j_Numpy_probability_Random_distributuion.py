#numpy random data distribution

from numpy import random as rn
x = rn.choice([3,5,7,9], p=[0.1,0.3,0.6,0.0], size=(100)) #probabilities distribution using random choice distribution
print(x)

x = rn.choice([3,5,7,9], p=[0.1,0.3,0.6,0.0], size=(3,5)) #2d array
print(x)
