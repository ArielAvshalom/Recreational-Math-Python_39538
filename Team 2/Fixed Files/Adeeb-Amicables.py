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
    # include 1 in the sum but not num (proper divisors)
    ret = 1
    # loop from 2, num/2 inclusive to get all divisors
    for i in range(2, num // 2 + 1):
        # add i if it is a divisior
        if num % i == 0:
            ret += i
    # return final sum
    return ret


def get_amicables(num):
    """
    This function prints all amicable pairs up to integer num

    param: int
         positive int that is the limit to print amicable pairs up to

    return: None
    """
    # check all numbers up to num
    for i in range(num):
        # get the sum of divisors for i
        i_sum = sum_proper_divisors(i)
        # check if the sum is greater than i to skip duplicates
        # check the sum of the divisors of the new number is equal to the original number
        if i_sum > i and sum_proper_divisors(i_sum) == i:
            print(i, i_sum)

get_amicables(25000)
