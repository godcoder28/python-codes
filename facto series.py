# WAP to print sum of series 1 + x/2! +x/3!........x/n!
# Date 05/08/2018
# Made By. Shivang Gupta
def facto(i):
    ans = 1
    while i >= 1:
        ans = ans * i
        i = i - 1
    return (ans)


n = int(input("Enter a no: "))
x = int(input("Enter a constant: "))
j = 1
ser = 0
while j < n:
    ser = ser + (x / facto(j + 1))
    j = j + 1
print("The ans is: ", ser + 1)
