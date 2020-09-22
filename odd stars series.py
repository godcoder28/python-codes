i = 1
while i <= 5:
    j = 1
    while j <= i:
        if j % 2 == 1:
            print(j, end='  ')
        else:
            print('*', end='  ')
        j = j + 1
    i = i + 1
    print('\n')
