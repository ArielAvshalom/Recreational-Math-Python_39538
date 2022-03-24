# Adeebur Rahman
# Python program that prints all amicables up to 25000
# Amicable numbers are two different natural numbers related in such a way that the sum of the proper divisors of each is equal to the other number
# The smallest pair of amicable numbers is (220, 284)

from functools import cache

@cache
def sum_proper_divisors(num: int):
    """
    This function returns the sum of proper divisors of a positive integer num

    param: int
         the positive integer to calculate the proper divisors sum

    return: int
         the sum of the proper divisors of num
    """
    ret = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            ret += i
            ret += num / i
    return ret

def get_amicables(num):
    """
    This function prints all amicable pairs up to integer num

    param: int
         positive int that is the limit to print amicable pairs up to

    return: None
    """
    for i in range(num):
        i_sum = sum_proper_divisors(i)
        for j in range(num):
            if i_sum == j and sum_proper_divisors(j) == i:
                print(i, j)
                break

get_amicables(25000)
