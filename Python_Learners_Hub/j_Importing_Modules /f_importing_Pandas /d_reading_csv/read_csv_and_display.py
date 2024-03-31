import pandas as pd

file_path = 'D:/mycodes1_4_24/Python/Numpy_Matplotlib_SciPy_Pandas/pandas/tips.csv'
df = pd.read_csv(file_path)

print("DataFrame from CSV: ")
print(df)

# Set the maximum number of rows to display
pd.set_option('display.max_rows', 99)

print("\nMax Rows Setting: ")
print(pd.options.display.max_rows)
