"""
Author: Aaron
Find prime number(s) 1 to n.
Parameters:
    n: An integer to find prime numbers up to.
Returns:
    List of prime number(s) up to n.
Implicit errors corrected.
Implicit errors:
    raise Exception(f"Not valid: {e}")
    custom error e is not defined so causes error.
    return Not False to return True
    Typo error added on purpose. Return True is more efficient.
"""
def prime_number_find(n):

    if n <= 0:
        raise Exception("Not valid")

    prime_numbers = []

    def is_prime(x):
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    for j in range(1, n + 1):
        if is_prime(j):
            prime_numbers.append(j)
    return prime_numbers

