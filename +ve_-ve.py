# Write a program to accept a number and check whether it is positive negative or zero?
# Date. 25/04/2019

x = int(input("Enter A No To Be Checked:"))
if x < 0:
    print("It's A Negative No.")

else:
    if x == 0:
        print("The No. Is 0")
    else:
        print("It's A Positive No.")
