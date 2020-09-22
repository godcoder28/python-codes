l = [1, 2, 3, 4, 5]
y = []
for i in range(1, len(l)):
    y.append(l[i])

y.append(l[0])

print(l, y)
l.insert(0, l.pop())
print(l)
