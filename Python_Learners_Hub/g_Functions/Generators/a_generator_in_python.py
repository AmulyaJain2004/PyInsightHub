# In Python, a generator is a special type of iterator that can be used to generate a sequence of values. 
# Unlike normal functions that return a single value using the return statement, generators use the yield statement to produce a series of values, one at a time.
# Generators are useful for generating large sequences of values without storing them all in memory at once, which can be memory-efficient. 
# They are also used for lazy evaluation, where values are generated only when needed.
def my_generator():
    yield 1
    yield 2
    yield 3

# Create a generator object
gen = my_generator()

# Iterate over the generator to retrieve values
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

# Attempting to retrieve more values will raise a StopIteration exception
# print(next(gen))  # Uncommenting this line will raise StopIteration
