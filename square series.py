"""WAP to print the series
1
1 4
1 4 9
1 4 9 16
"""
#Date 05/08/2018
#Made By. Shivang Gupta
i=1
while i<=4:
    j=1
    while j<=i:
        print(j**2,end='   ')
        j=j+1
    i=i+1
    print('\n')
