# Write a program to accept height in centimetre and convert into feet and inches?
# Date. 25/04/2019
# MADE by: Shivang Gupta

cms = int(input("Enter Height In CMs:"))
inch = cms / 2.5
feet = int(inch // 12)
inch2 = (inch % 12)
g = float("{0:.2f}".format(inch2))
print("Height In Feet & Inches Is:", feet, "ft", g, "''")
