#WAP To input a string and check whether it is a palindrome or not.
#Made By: Shivang Gupta
x=str(input("Enter A String: "))
for i in range(len(x)):
    if x[i]==x[len(x)-1-i]:
        if i==len(x)-1:
            print("The String Is  A Pallindrome.")
    else:
        print("The String Is Not A Pallindrome.")
        break
