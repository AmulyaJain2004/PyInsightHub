a, b = map(str, input().split())
try:
    num = int(a) / int(b)
    print(num)
except ValueError as v:
    print(v)
except ZeroDivisionError as e:
    print(e)
