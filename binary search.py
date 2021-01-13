# list indexs

li = []
sli = []
n = int(input("Enter the No of elements: "))
for i in range(n):
    li.append(int(input("Enter an element: ")))
e = int(input("Enter an element to be searched: "))
sli = sorted(li)


def binary(beg=0, end=n - 1):
    while True:
        mid = (beg + end) // 2
        if sli[mid] == e:
            return (sli[mid])
            break
        if beg > end:
            return (-1)
            break
        elif sli[mid] > e:
            end = mid - 1
        else:
            beg = mid + 1


ans = binary()
if ans == -1:
    print("The element is not present in the list.")
else:
    print("The element is found at position: ", li.index(ans) + 1)
