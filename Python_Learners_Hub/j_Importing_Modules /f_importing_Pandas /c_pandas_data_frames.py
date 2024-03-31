import pandas as pd

data_dict = {'Name': ['alice','bob','charlie'],
             'Age': [25,30,22],
             'City': ['New York', 'France', 'UK']}

df_from_dict = pd.DataFrame(data_dict)
print("DataFrame from dictionary: ")
print(df_from_dict)

data_list_of_dict = [{'name':'david','age':28, 'city': 'chicago'},
                      {'name':'Eva','age':35, 'city': 'Canada'}]

df_from_list_of_dict = pd.DataFrame(data_list_of_dict)
print("DataFrame from list of dictionary: ")
print(df_from_list_of_dict)

# data frames can be created from both dictionary of list and from list of dictionary.
