15#WAP To input a no and check whether It's an Armstrong No. or not?
#Made By: Shivang Gupta
def arm(x):
    s=0
    for i in x:
        s+=int(i)**3
    print("It's an armstrong Number") if s==int(x) else print("It's not an armstrong Number") 
    return('')
x=input("Enter A no to be checked: ")
print(arm(x),end='')
