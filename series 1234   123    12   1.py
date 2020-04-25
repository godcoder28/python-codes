#WAP to print the series
"""
1 2 3 4
1 2 3
1 2
1   """
#Date 05/08/2018
#Made By. Shivang Gupta
i=1
while i<=4:
    j=1
    while j<=5-i:
        print(j,end='  ')
        j=j+1
    i=i+1
    print('\n')
