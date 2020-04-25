"""To print following patterns on screen:
54321
5432
543
54
5
Made By: Shivang Gupta"""
for i in range(5):
    for j in range(5,i,-1):
        print(j,end='  ')
    print('\n')
