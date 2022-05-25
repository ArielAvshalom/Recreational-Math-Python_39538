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

Errors corrected after code review:

1. Check that user input is positive
2. Add special case for 2, since it is a positive even integer that cannot be broken down into the sum of two primes
3. is_prime() doesn't need to divide n by all integers up to n-1 to check if n is prime -- only up to n//2+1
4. No 'else' needed on last line

'''

def goldbach(n):
    
    if n == 2:
        return '2 is a special case: (1,1) if you consider 1 to be prime, otherwise 2 is an exception.'
    if not (n%2 == 0 and n>0):
        return Exception('That\'s not a positive even number!')
    
    def is_prime(n):
        for i in range(2,n//2+1):
            if n%i == 0:
                return False
        return True

    for i in range(n//2,1,-1):
        if is_prime(i):
            if is_prime(n-i):
                return (i,n-i)
    return 'No pair of primes found!' 

print(goldbach(72728))
