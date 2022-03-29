## CSCI 39538: Homework 2: Recreational Math Spec 
## Team 6: Code Review

## Brang Mai
#### Topic: Perfect Numbers
##### Definition 1: A perfect number is a positive integer that equals the sum of its divisors except itself.
##### Definition 2: A perfect number is a positive integer that is half the sum of all its divisors including itself.
Some perfect numbers: 6, 28, 496, 8128, 33550336

* Errors:
The function, “is_perfect_number(test_num, method)”, returns true if the “test_num” argument is a perfect number, and returns false otherwise. The “method” argument is used to check a perfect number by the two definitions listed above. Checking perfect numbers by method 1 produces the correct answers. However, checking by method 2 does not give the correct ones.

* Solutions:
The method 2 requires the “test_num” argument to be added to the sum of its divisors. Once the computation logic is right, some perfect numbers will be correct. To have all perfect numbers correct, the injected function that prevents the checking of extremely large, time consuming and computationally costly numbers must be removed.

## **Christopher Sostre**
The code asks the user what number they want to stop at when defineing prime numbers.
First it takes a number to see if it is divisible by more than two numbers and if it is, it’s not a prime number. If it is divisible by only two numbers it is a prime number, and it tells that to the user. It also tells the user what isn’t a prime number and why (by that I mean what is the third number it is divisible by).

* The errors:
The code only initialize c (count) once to 0.
There is no way the code can tell the user that a
number is a prime number since there is no break statement and c keeps going up and never stoping ever (or until it iterates through all the numbers).


## Israel Arcos
#### Topic: Narcissistic Numbers


## Vicky Cao
#### Topic: Amicable Numbers
##### Explanation: Amicable numbers are two different natural numbers, where the factor of the first number is equal to the second number and vice versa.
For example, the smallest amicable numbers are 220 and 284. The factors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, and 110. When the factors of 220 are added together, we get 284. 
The factors of 284 are 1, 2, 4, 71, and 142. The factors of 284 added together are equal to 220.

* Errors: 
In line 4, the code was switched from s=1 to s=2. The changed the sum of all proper divisors of a number, which would output that amicable numbers are not amicable numbers.
In line 15, ‘and a!=b’ was removed. 
