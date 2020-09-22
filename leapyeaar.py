# WAP to input an year and check whether it's a leap year or not?
# Date: 9/7/19
# Made By. Shivang Gupta
year = int(input("Enter a Year: "))
if year % 100 == 0:
    if year % 400 == 0:
        print("The year is a leap year.")
    else:
        print("The year is not a leap year.")
elif year % 4 == 0:
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")
