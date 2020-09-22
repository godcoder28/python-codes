# Wap to input a list and perform insertion sort.
# Made By- Shivang Gupta
li = []
n = int(input("Enter the No of elements: "))
for i in range(n):
    li.append(int(input("Enter an element: ")))


def insertion_sort(li):
    for i in range(1, n):
        item = li[i]
        j = i - 1
        while item < li[j] and j >= 0:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = item
    return (li)


print("The sorted List is: ", '\n', insertion_sort(li))
input("Press Esc to Quit")
