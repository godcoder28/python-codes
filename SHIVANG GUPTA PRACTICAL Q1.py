#Made By: Shivang Gupta
#Set: 2
#Q1.
#Date: 17/09/2019
q=int(input("""Menu: \n1.To Check whether a number is an armstrong number 
2.To check whether the string is a pallindrome 
3. to input a list and search an element using linear search \n"""))
if q==1:
    x=input("Enter A No: ")
    s=0
    for i in x:
        s+=int(i)**3
    print("The Number is an Armstrong Number")if s==int(x) else print("The Number is NOT an Armstrong Number")
elif q==2:
    x=input("Enter A string To be checked: ")
    x2=x[-1:-(len(x)+1):-1]
    if x==x2:
        print("The string is a pallindrome.")
    else:
        print("The string is not a pallindrome.")
else:    
    l=[]
    n=int(input("Enter No of elements: "))
    for i in range(n):
        l.append(int(input("Enter Element: ")))
    e=int(input("Enter element to be searched: "))
    for j in range(n):
        if e==l[j]:
            print("The Element is found at position: ",j+1)
            break
        if j==n-1:
            print("The element is not in the list")
input("Press enter to Quit")
