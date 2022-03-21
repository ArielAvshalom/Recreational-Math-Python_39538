from functools import cache

@cache
def sum_proper_divisors(num: int):
    ret = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            ret += i
            ret += num / i
    return ret

def get_amicables(num):
    for i in range(num):
        i_sum = sum_proper_divisors(i)
        for j in range(num):
            if i_sum == j and sum_proper_divisors(j) == i:
                print(i, j)
                break

get_amicables(25000)