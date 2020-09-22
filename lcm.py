# WAP to input two numbers and print their LCM and HCF?
# Made By. Shivang Gupta
# Date. 19/08/19
def main():
    x = int(input("Enter A No: "))
    y = int(input("Enter Second No:"))
    i = 1
    while True:
        if (x * i) % y == 0:
            lcm = x * i
            break
        i = i + 1
    for j in range(1, min(x, y) + 1):
        if x % j == 0 and y % j == 0:
            hcf = j
    return ("The HCF is: ", hcf, "The LCM is: ", lcm)


print(main())
