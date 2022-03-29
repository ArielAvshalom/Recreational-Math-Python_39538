def check_factors(num, factors):
    """
    check if the num is divisible by any of the numbers in the factors list
    ### Parameters
    1. num : int
    2. factors : [int]
   

    ### Returns
    - bool
        - returns True if num is divisible by a number in the list and false if not
    """
    for factor in factors:
        if num % factor  == 0:
            return True
    return False


def natural_generator():
    """
    generate all natural numbers starting at 2

    ### Returns
    - generator
        - return a generator that finds the next natural number
    """
    start = 1;
    while True:
        start += 1
        yield start

#generate all prime numbers start at 2
def prime_generator():
    """
    Generating Primes using the sieve of sieve of eratosthenes
    -A prime is defined as an number that is divisible by one and itself

    Description: We begin with a list of natural numbers. We start with 2 and assume it to be prime and 
    filter all multiples of two from our list. That will give us a new list of natural numbers. Then we move
    to our next number in our new list which is three. We then filter from our new list all multiples of three
    to generate our new list. If we keep on repeating this procedure, we will eventually be left with a list
    of all prime numbers. 
    

    ### Returns
    - generator
        - return a generator that finds the next prime number
    """
    factors = []
    gen = natural_generator();
    start = next(gen)

    if start == 2:
        factors.append(start)

    while True: 
        value = next(gen)
        if not check_factors(value, factors):
            factors.append(value)
            yield value

def main():
    number_of_primes = int(input("How many primes would you like?: "))

    #generates all the primes up to value specified in the user input
    gen = prime_generator()
    for i in range(number_of_primes):
        number = next(gen)
        print(number)


"""
checks if number if prime 
algoritm from wikipedia
https://en.wikipedia.org/wiki/Primality_test#Python
"""
# def is_prime(n: int) -> bool:
#     """Primality test using 6k+-1 optimization."""
#     if n <= 3:
#         return n > 1
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i ** 2 <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

#check the first million primes
# for i in range(1000000):
#     number = next(gen)
#     if not is_prime(number):
#         print(f"{number} is not a prime, stopped at iteration {i}")
#         break;
#     else:
#         print(f"{number} is prime")

if __name__ == "__main__":
    main()





