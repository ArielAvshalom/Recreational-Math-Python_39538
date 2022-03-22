from functools import cache

@cache
def sum_proper_divisors(num: int):
    ret = 1
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            ret += i
    return ret

def get_amicables(num):
    for i in range(num):
        i_sum = sum_proper_divisors(i)
        if sum_proper_divisors(i_sum) == i and i_sum > i:
            print(i, i_sum)


get_amicables(25000)