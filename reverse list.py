#WAP To input a list and print the reverse of the list.
#Made by. Shiavng Gupta
L1=[]
L2=[]
n=int(input("Enter No of Elements in the list: "))
for i in range(n):
    x=int(input("Enter the Element: "))
    L1.append(x)
for j in range(n):
    L2.append(L1[n-1-j])
print("Reverse of the List entered is: ",L2)
