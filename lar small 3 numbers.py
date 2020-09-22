# WAP To input three numbers and find largest and smallest amongst them.
# Made By- Shivang Gupta
x = int(input("Enter a No: "))
y = int(input("Enter 2nd No: "))
z = int(input("Enter 3rd No: "))
if x > y and x > z:
    print("The largest no is:", x)
    if y > z:
        print("The smallest no is: ", z)
    else:
        print("The smallest no is: ", y)
elif y > x and y > z:
    print("The largest no is :", y)
    if x > z:
        print("The smallest no is: ", z)
    else:
        print("The smallest no is: ", x)
else:
    print("The largest no is :", z)
    if x > y:
        print("The smallest no is: ", y)
    else:
        print("The smallest no is: ", x)
