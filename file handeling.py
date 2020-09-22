"""
file = open('xy.dat', 'r+')
l = file.read()
l2 = l.replace(' ', '\n').split('\n')
print(l2)


def DISPLAYWORDS(m):
    for i in m:
        print(i, end=' ') if len(i) <= 4 else print(end='')

DISPLAYWORDS(l2)
"""

# =============Q1

"""
file = open("book.txt", 'w+')
file.write("line 6")
file.write("\nline 2")
file = open("book.txt", 'r')
print(file.read())
file.close()
"""
# =============Q2
"""
file1 = open("abc.txt", 'r+')
file2 = open("apj.txt", 'r+')
file2.write(file1.read())
file2 = open("apj.txt", 'r')
print(file2.read())
"""
# =============Q3
"""
file = open("connect.txt", 'r')


def data(f):
    for i in f.readlines():
        print("Name:- ", i.split(' ')[0], " Phone:- ", i.split(' ')[1])


data(file)
"""
# =============Q4
"""
file = open("connect.txt", 'r')


def count(f):
    for i in f.readlines():
        ans = ''

"""
# =============Q5
"""
f = None
for i in range(5):
    with open("abc.txt", "w") as f:
        print(f.closed, '1')
        if i > 2:
            print(f.closed, '2')
            break
        print(f.closed, '3')
    print(f.closed)"""

n = int(input("Enter No of lines: "))
file = open("f.txt", 'r')
x = file.readlines()
for i in range(n):
    print(x[i])
