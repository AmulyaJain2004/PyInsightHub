from numpy import random
x= random.randint(1000) #for random integer from 0 to 1000
print(x) 

x = random.rand() #for random floating point values
print(x)

x = random.randint(1000, size=(5)) #random elements in array ranging from 0 to 1000 and size of array =5
print (x)
  
x = random.randint(1000, size=(3, 5)) #random elements in 2d array ranging from 0 to 1000 with 3 rows and 5 columns containing that range
print (x)

x = random.choice([3,7,6,5]) #choice method random value from the array
print(x)

x = random.choice([3,7,6,5], size = (4,2)) #choice method random value from the array and generates a 2d array of 4 rows and 2 columns by choosing random values from array
print(x)
