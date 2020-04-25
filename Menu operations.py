#W.A.P to display a menu and perform the operation based on the choice?
#Date. 15/07/19
#Made By. Shivang Gupta
ans=0
print("""Choose from one of the operation below: \n 1)Addition \n 2)Subtraction 
 3)Multiplication \n 4)Division \n 5)Floor Division \n 6) Modulus \n 7)Exit""")
x=input("Enter the Operation:")
if x=='exit':
    exit
else:
    a=int(input("Enter the first Operant:"))
    b=int(input("Enter the second Operant:"))
    if x == 'addition':
        ans=a+b
    elif x=='subtraction':
        ans=a-b
    elif x=='division':
        ans=a/b
    elif x=='multiplication':
        ans=a*b
    elif x=="floor division":
        ans=a//b
    elif x=='modulus' :
        ans=a%b
    print("The answer to your operation is:",ans)

