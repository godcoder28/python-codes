file = open('data.txt', 'r')
counter = 0
data = file.read()
words = data.split()
print(words)
for i in words:
    if i== 'this':
        counter +=1
print("no of times this: ", counter)
