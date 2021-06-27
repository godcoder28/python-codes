data = [5, 6, 7, 9, 10]
    
def push(stack):
    element = input("Enter element to be pushed: ")
    stack.append(element)
    return 'The element was pushed in staack'

def pop(stack):
    try:
        stack.pop()
        return 'Last element was popped out of stack'
    except:
        return 'Stack is empty'
while True:
    choice = input("Choose the operation you want to perform:\
1)push 2)pop 3)view 4)quit: ")

    if choice == 'push':
        print(push(data))
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
