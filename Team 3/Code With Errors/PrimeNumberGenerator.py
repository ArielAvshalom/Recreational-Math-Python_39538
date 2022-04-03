# Perla Escano Estrella
# CSCI 39538
# Recreational Math Assignment
""" 
Prime numbers are whole numbers greater than 1, that have only two factors: 1 and the number itself.
Prime numbers are divisible only by the number 1 or itself. 

The following code generates all the prime numbers up to the number the user denotes.


"""
n = int(input("Hi, I am a prime number generator!\n Up to what number would you like me to generate the primes? : "))

for x in range(2, n):
    is_prime = True
    for y in range(2, x):
        if x % y == 0:
            is_prime = False

    if is_prime:
        print(x)

"""
ERROR FOUND BY Serrin Doscher
    Number inputted is not included in the output
    Fix: Line 14 change to for x in range(2, n+1)

"""