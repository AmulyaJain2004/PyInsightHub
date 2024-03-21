import pandas as pd

mydataset = {
    'cars':["bmw","volvo","ford"],
    'passing': [3,7,4]
}

myvar = pd.DataFrame(mydataset)
print(myvar)
