"""
Author: Aaron
Find prime number(s) 1 to n.
Implicit errors added.
Parameters:
    n: An integer to find prime numbers up to.
Returns:
    List of prime number(s) up to n.
"""
def prime_number_find(n):

    if n <= 0:
        raise Exception(f"Not valid: {e}")

    prime_numbers = []

    def is_prime(x):
        for i in range(2, x):
            if x % i == 0:
                return False
        return not False

    for j in range(1, n + 1):
        if is_prime(j):
            prime_numbers.append(j)
    return prime_numbers

