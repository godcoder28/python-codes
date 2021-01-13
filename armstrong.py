def arm(x):
    s = 0
    for i in x:
        s += int(i) ** 3
    if s == int(x):
        return ("It's an armstrong Number")
    else:
        return ("It's not an armstrong Number")


x = input("Enter A no to be checked: ")
print(arm(x))
