nosl = []
nos = open("nos.txt", 'r')
for i in nos.readlines():
    nosl.append(i)
for i in nosl:
    if i == '\n':
        nosl.remove(i)
nosf = []
for i in nosl:
    nosf.append(i[0:10])
print(nosf)

names = []
nam = open("names.txt", 'r')
for i in nam.readlines():
    names.append(i[0:len(i) - 1])
print(names)

print(len(nosf), len(names))

RESULTS = ['apple', 'cherry', 'orange', 'pineapple', 'strawberry']

resultFyle = open("output1.csv", 'w')

# Write data to file
for r in nosf:
    resultFyle.write(r + "\n")
resultFyle.close()
