'''
A. Leshchenko

Goldbach Conjecture: Every positive even integer can be written as the sum of two primes.

This algorithm finds two primes that sum to a given even integer (or reports that no such primes can be found).
First, it checks that n is an even integer. Then it iterates over all two-number partitions of n and returns the
first one for which both numbers are primes. Primality is checked using a helper function that tries to divide
n by every value smaller than it (other than one), and returns False if no such value was found.

Parameters
    ----------
    n : integer
    
    Returns
    -------
    i, n-1 : two prime integers, if found
'''

def goldbach(n):
    if not n%2 == 0:
        raise Exception('That\'s not an even number!')

    def is_prime(n):
        for i in range(2,n):
            if n%i == 0:
                return False
        return True

    for i in range(n//2,1,-1):
        if is_prime(i):
            if is_prime(n-i):
                return (i,n-i)
    else: return 'No pair of primes found!'

print(goldbach(72728))
