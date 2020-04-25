#Q. WAP to print the sum of squares upto n?
#Date: 24/04/19
#MADE BY: Shivang Gupta
num1 = int(input("Enter A No:"))
if (num1<1):
    print("The No. Is a -ve or 0")
else:    
    x = 1
    ans = 0
    while (x<=num1):
        ans=ans+(x**2)
        x=x+1
    print("the ans is: ", ans)    

