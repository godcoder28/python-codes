#WAP To add the odd numbers up to(and including) a given value N and print the result.
#Made By: Shivang Gupta
n=int(input("Enter An Odd No:"))
s=0
for i in range(1,n+1,2):
    s+=i
print("Print Sum of First N odd Numbers Is: ",s)
