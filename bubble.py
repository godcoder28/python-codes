l = [3, 5, 65, 85, 24, 16, 54]
n = len(l)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
print(l)

l = [3, 5, 65, 85, 24, 16, 54]
for i in l:
    for j in range(0, l.index(i)):
        x = l.index(i)
        if l[x] < l[x - 1]:
            l[x], l[x - 1] = l[x - 1], l[x]
print(l)
