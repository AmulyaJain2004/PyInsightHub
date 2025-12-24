import pandas as pd

# a = [7,5,9]
# # myvar = pd.Series(a) 
# myvar = pd.Series(a, index=["p","q","r"]) # set the index of series to "p", "q" and "r". If not given it will be default integer index starting from 0 as we saw in above example.
# print(myvar)

data_list = [10,20,30,40,50]
series_from_list = pd.Series(data_list) # create a series from the list

data_dict = {'a' : 10,'b':20, 'c':30,  'd':40, 'e':50}
series_with_index = pd.Series(data_dict)

print("series from list: ")
print(series_from_list)
print("\nseries with index: ")
print(series_with_index)
