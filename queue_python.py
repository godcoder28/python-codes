data = [5, 6, 7, 9, 10]
    
def insert(queue):
    element = int(input("Enter element to be pushed: "))
    queue.append(element)
    return 'The element was inserted in the queue'

def pop(queue):
    try:
        queue.pop(0)
        return 'First element was popped out of queue.'
    except:
        return 'Queue is empty'
while True:
    choice = input("Choose the operation you want to perform:\
1)insert 2)pop 3)view 4)quit: ")

    if choice == 'insert':
        print(insert(data))
    elif choice == 'pop':
        print(pop(data))
    elif choice == 'view':
        print(data)
    else:
        exit()
    choice = input("Do you want to continue (y/n)? ")
    if choice == 'y':
        continue
    else:
        break
