# WAP To input a list and perform bubble sort.
# Made By: Shivang Gupta
L1 = []
n = int(input("Enter No of Elements in the list: "))
for i in range(n):
    x = int(input("Enter the Element: "))
    L1.append(x)
for i in range(n):
    for j in range(n - i - 1):
        if L1[j] > L1[j + 1]:
            L1[j], L1[j + 1] = L1[j + 1], L1[j]
print("The sorted List is: ", L1)
