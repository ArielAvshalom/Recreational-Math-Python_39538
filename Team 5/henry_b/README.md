# CSCI 39538: Homework 2: Recreational Math with Implicit Errors
The objective of this assignment was to select a recreational math problem, then after completing it, purposely add errors for other team members to debug. 

## Prime Number Generator
`prime_gen.py` is a script that produces prime numbers by two different methods:
- range: finds all the prime numbers from 1 to limit (inclusive)
- digits: prints a set of random prime numbers of a certain digit size

## Contents
- `prime_gen.py` - Main driver to parse arguments for prime number generator
- `prime.py` - Contains the faulty methods of generating prime numbers, either by a range or number of digits
- `solution.py` - The corrections made by the code reviewing group
- `hab_solution.py` - The original implementation/solution by the coder
- `SOLUTIONS.md` - Explanation of the errors added to the program

## How to use
1. Clone and navigate into the root of the repo
2. type `python prime_gen.py` and provide the desired arguments. There are two mutually exclusive arguments:
    1. `--range`/`-r` `LIMIT` - Finds all the prime numbers from 1 up to `LIMIT` (inclusive). `LIMIT` must be a positive integer
    
    For example: `python prime_gen.py -r 10` should output `[2, 3, 5, 7]`
    
    2. `--digits`/`-d` `DIGITS` `SIZE` Prints a prime number with `DIGITS` amount of digits, and will continue to find `SIZE` amount of prime numbers of that digit size. `DIGITS` and `SIZE` must be positive integers.
    
    For example: `python prime_gen.py -d 10 5` should print `[7768103059, 6872570119, 2456328697, 1585648489, 1313618821]`
3. A third optional argument `-s`/`--solution` will use the corrections made by the review members.
4. A fourth optional argument `-o`/`--original` will use the original implementation/solution from the coder, displaying the correct output.
__*By default, the script uses the faulty generators, so use the optional arguments if you want to see the correct output.*__ 

## Implicit Errors
There are at least 5 intentional implicit errors in `prime.py`, as well as a way to drastically improve `range_n_1()`'s runtime. For the list of errors and their explanations, [see the readme for the solutions here](./SOLUTIONS.md).

## Resources
[Wikipedia Entry for Sieve of Atkin](https://en.wikipedia.org/wiki/Sieve_of_Atkin)

## Team:
### Coder:
### - Henry Baum
### Review Members: 
### - Dewan S.
### - Avinash S.
### - Max S.
