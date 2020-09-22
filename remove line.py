f = open("text.txt", 'r')
f2 = open("modified.txt", 'w+')
for i in f.readlines():
    print(i)
    if not "line 3" in i:
        f2.write(i)
