def fibonacci_generator(n):
    a, b = 0,1 
    count = 0
    while count < n:
        yield a 
        a, b = b, a+b 
        count +=1
    
n = int(input())
fib_gen = fibonacci_generator(n)

for fib_number in fib_gen:
    print(fib_number)
