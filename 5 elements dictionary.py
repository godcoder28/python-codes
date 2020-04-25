#WAP To input 5 elements in a dictionary and print them on screen?
#Made By. Shivang Gupta
dictionary={}
n=int(input("Enter No of elements in the dictionary: "))
for i in range(n):
    a=input("Enter Item: ")
    b=int(input("Enter It's quantity: "))
    dictionary[a]=b
print("The Dictionary formed is: ",dictionary)
