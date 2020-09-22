# To print first 10 numbers of the Fibonacci series. i.e. 0 1 1 2 3 5 8...
# Made By: Shivang Gupta
a = 1
b = c = 0
for i in range(10):
    print(a, end='   ')
    b, c = a, b
    a = b + c
