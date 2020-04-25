# Write a program to accept principal rate of interest time and compute simple interest and compound interest?
# Date. 25/04/2019
#MADE BY: Shivang Gupta

p = float(input("Enter Pricipal Amount:"))
r = float(input("Enter Rate Of Interest:"))
t = float(input("Enter Time In Years:"))
amount = 0
choice = input("Do you want Simple Interest or Compound Interest [Enter SI/CI]:")
choice=choice.lower()
if choice == "si":
    amount=p + (p*r*t/100)
else:
    amount=p*(((r/100)+1)**t)
print("Total Amount To Be Paid With Interest Is:", amount)
