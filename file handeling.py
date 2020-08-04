file = open('xy.dat', 'r+')
l = file.read()
l2 = l.replace(' ', '\n').split('\n')
print(l2)


def DISPLAYWORDS(m):
    for i in m:
        print(i, end=' ') if len(i) <= 4 else print(end='')

DISPLAYWORDS(l2)
