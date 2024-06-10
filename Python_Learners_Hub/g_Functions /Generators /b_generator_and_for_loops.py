# We can use a for loop to iterate over the values produced by a generator function. 
# When we use a for loop with a generator, the loop iterates over the values yielded by the generator one at a time, without needing to explicitly call the next() function.
def my_generator():
    yield 1
    yield 2
    yield 3

# Create a generator object
gen = my_generator()

# Iterate over the generator using a for loop
for value in gen:
    print(value)
# We use a for loop to iterate over the values produced by the generator. 
# The for loop automatically calls next() on the generator object gen and retrieves the yielded values one by one until the generator is exhausted.
# Using a for loop with a generator is a clean and concise way to iterate over the values produced by the generator without having to manually manage the iteration using next() calls. 
# It simplifies the code and makes it easier to work with generators in Python.
