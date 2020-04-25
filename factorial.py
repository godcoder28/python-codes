#WAP To accept a number and print it's factorial.
#Made By: Shivang Gupta
def facto(i):
    ans=1
    while i >= 1:
        ans*=i
        i-=1
    return(ans)
i=int(input("Enter A No: "))
print("Factorial of ",i," is: ",facto(i))
