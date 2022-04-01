# Azaan Ali -- Segmented Sieve of Eretheosenses
def Eretheosenses(n: int):
    """
    This function returns an array of all primes from 2 to n.
    Prints all primes in that range.

    param: int
         Integer to calculate primes up to that value

    return: array
         Returns an array of all primes up to n
    """
    primes = []
    check = [True] * n
    check[0] = check[1] = False

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
    """
    Creates an array of primes from 2 to sqrt(n), then calculates the 
    remaining range in segments of sqrt(n) up to n. Calculates the remanining primes by removing the multiples of 
    each primes from the list and printing the primes.

    param: int
        Integer to calculate primes up to that value

    """
    segment = int((n ** 0.5 + 1) // 1)
    primes = Eretheosenses(segment)
    lowerLimit = segment
    upperLimit = lowerLimit + segment

    while lowerLimit < n:
        check = [True] * (upperLimit - lowerLimit + 1)
        for i in primes:
            multiple = int((lowerLimit / i) // 1) * i
            if multiple < lowerLimit:
                multiple += i
            if multiple > i * i:
                startVal = multiple
            for j in range(startVal, upperLimit, i):
                check[j - lowerLimit] = False

        for i in range(lowerLimit, upperLimit):
            if check[i - lowerLimit]:
                print(i, end=" ")
        lowerLimit = lowerLimit + segment
        upperLimit = upperLimit + segment
        if upperLimit >= n:
            upperLimit = n


Segment(100000)
