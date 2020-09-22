# WAP to print sum of series 1**2+ 3**2+5**2.........121**2
# Date 05/08/2018
# Made By. Shivang Gupta
x = 1
sum1 = 0
while x <= 121:
    sum1 = (x ** 2) + sum1
    x = x + 2
print("The Sum Is: ", sum1)
