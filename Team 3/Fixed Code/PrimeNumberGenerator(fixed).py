# Perla Escano Estrella
# CSCI 39538
# Recreational Math Assignment
""" 
Prime numbers are whole numbers greater than 1, that have only two factors: 1 and the number itself.
Prime numbers are divisible only by the number 1 or itself. 

The following code generates all the prime numbers up to the number the user denotes.


"""
n = int(input("Hi, I am a prime number generator!\n Up to what number would you like me to generate the primes? : "))

for x in range(2, n+1):
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

ERROR FOUND BY Fnu Tsering
    Error: The value that user inputs is not checked to see it's prime or not, 
    	   so if user input value is a prime number, it is not printed as one of the prime numbers.
    	   
	Fix: Add 1 to n in the outer for loop so that it also checks the input number to see if it's prime or not.

    
"""
