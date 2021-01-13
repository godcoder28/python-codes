x = int(input("Enter a number to find factorial: "))


def factorial(i):
    if i == 1:
        return 1
    else:
        return (i * factorial(i - 1))


print("Factorial of the number is: ", factorial(x))
