def salary():
    file = open("employee.dat", 'rb')
    for i in pickle.load(file):
        print(i)
        salary = i.split(':')[2]

        if salary >= 20000 and salary <= 50000:
            print(i)


salary()


def main():
    Moves = [90, 70, 50, 30]
    Queen = Moves
    Moves[2] += 33
    L = len(Moves)
    for i in range(L):
        print('Now @', Queen[L - i - 1], '#', Moves[i])


main()

import pickle


def a():
    f = open('employee.dat', 'rb')
    s = pickle.load(f)
    print(s)

    l = s.split(':')
    if 20000 <= int(l[2]) <= 40000:
        print(':'.join(l))
    f.close()


a()

import csv


def storecsv():
    data = input("enter csv data: ")
    with open('file7.csv', mode='w') as file:
        writing = csv.writer(file, delimiter=',')
        writing.writerow(data.split(','))


storecsv()
