x = int(input("Enter number to check whether it's perfect: "))

factors = []
for i in range(1, x):
    if x // i == x / i:
        factors.append(i)
if sum(factors) == x:
    print("The number is a perfect number.")
else:
    print("The number is a not a perfect number.")
