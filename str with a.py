l = []
n = int(input("Enter No of strings in list: "))
for i in range(n):
    l.append(input("Enter String: "))
for i in l:
    l1 = list(i)
    if l1[0] == "a" or l1[0] == "A":
        print(i)
