for i in range(1,1001):
    prime = False
    for j in range(2,i//2+1):
        if i%j==0:
            prime = True
            break
    if not prime:
        print(i)
