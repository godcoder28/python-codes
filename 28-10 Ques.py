n = input("Enter no")
n = int(n)
while n != 0:
    print("The Number is: ", n)
    n = n // 10

name = "surjeet singh sodhi"
a = 0
b = 1
for x in name[-1:-6:-1]:
    print(a, end=' ')
    c = a + b
    a = b
    b = c
