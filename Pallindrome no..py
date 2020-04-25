#WAP To accept a number and check whether it is a palindrome or not.

x=str(input("Enter A No: "))
for i in range(len(x)):
    if x[i]==x[len(x)-1-i]:
        if i==len(x)-1:
            print("The No. Is  A Pallindrome.")
    else:
        print("The No Is Not A Pallindrome.")
        break
