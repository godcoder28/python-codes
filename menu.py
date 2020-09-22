"""WAP to make a menu driven programme:  a) To print reverse of a string
b) To check if a given no is an armstrong no or not?    c) To input the radius and print it's area?"""
# Made By: Shivang Gupta
a = int(input("Enter The Ques No. to be done: "))


def rev():
    x = input("Enter the string: ")
    ans = x[-1:-(len(x) - 1):-1]
    return (ans)


def arm():
    x = input("Enter the no: ")
    s = 0
    for i in x:
        s += int(i) ** 3
    ans = "It's an Armstron No" if s == int(x) else "It's not an Armstrong No."
    return (ans)


def circle():
    x = input("Enter the radius: ")
    return (3.14 * int(x) ** 2)


if a == 1:
    print(rev())
print(arm()) if a == 2 else print("Area of the circle is: ", circle())
input("Press Enter To Quit")
