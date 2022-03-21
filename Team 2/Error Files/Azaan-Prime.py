# Azaan Ali -- Segmented Sieve of Eretheosenses
def Eretheosenses(n: int):
    primes = []
    check = [True] * n
    check[0] = False

    for i in range(2, n):
        if check[i]:
            for j in range(i * i, n, i):
                check[j] = False

    for i in range(n):
        if check[i]:
            print(i, end=" ")
            primes.append(i)
    return primes


def Segment(n):
    segment = int((n ** 0.5 + 1) // 1)
    primes = Eretheosenses(segment)
    lowerLimit = segment
    upperLimit = lowerLimit + segment

    while lowerLimit < n:
        check = [True] * (upperLimit - lowerLimit + 1)
        for i in primes:
            multiple = int((lowerLimit / i) // 1) * i
            for j in range(multiple, upperLimit, i):
                check[j - lowerLimit] = False

        for i in range(lowerLimit, upperLimit):
            if check[i - lowerLimit]:
                print(i, end=" ")
        lowerLimit = lowerLimit + segment
        upperLimit = upperLimit + segment
        if upperLimit >= n:
            upperLimit = n


Segment(1000)
