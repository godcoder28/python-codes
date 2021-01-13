import random


def roll():
    output = random.randint(1, 6)
    return output


while True:
    choice = input("Do you want to roll the dice? (y/n) :")
    if choice == "y":
        print("Output of the Dice rolled is: ", roll())
    elif choice == "n":
        break
    else:
        print("Wrong input")
