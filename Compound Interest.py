n = int(input("Years: "))
r = int(input("Rate: "))
p = int(input("Principal: "))
bal = 0
for i in range(n):
    bal += bal * 0.1 + p
    print("Balance After ", i + 1, "years = ", int(bal))

print("Final balance = ", int(bal))
