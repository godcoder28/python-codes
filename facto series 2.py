x = int(input("Enter a number: "))


def series(n):
    answer = 1
    for i in range(1, n + 1):
        factorial = 1
        j = i
        while j >= 1:
            factorial *= j
            j -= 1
        answer += (1 / factorial)
    return answer


print("The of series 1+1/1!+1/2!+⋯+1/n! till given no. = ", series(x))
