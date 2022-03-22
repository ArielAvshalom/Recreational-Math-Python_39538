# Advanced Python : Recreational Math 

Submitted by Team 2:
 
* []() [Azaan Ali](https://github.com/AzaanDev)
* []() [James Yoo](https://github.com/jamyooes)
* []() [Neslie Fernandez](https://github.com/nesquickcoding)
* []() [Adeebur Rahman](https://github.com/adeeburrahman)

Our Recreational Math consist of:

* []() Prime Numbers
* []() Narcisstic Numbers
* []() Perfect Numbers
* []() Amicable Numbers 

# User Stories

The following functionality is completed:

* [x] Error Code
* [x] Fixed Code 
* [x] Code Documented

# Errors Found

## Errors with Prime numbers code
* Considers 1 a prime number; 
  * Fixed by manually setting **1** to **false**.
  * Segment function incorrectly starts at the wrong value when checking if the multiple of primes are the wrong values. 
* Example:
  * if prime[i] is **3** and our starting value was **31** then **37** would be consider not prime. 
  * This is hard error to find or fix because it is hard to identify minimum number we need to start at for each prime. 
  * This is fixed with a if statement that calculates the correctly starting value for each prime

## Errors with Narcissistic numbers code
* The error for the Narcissistic number code is that the code skipped the first two narcissistic numbers (0 and 1) from the loop. 
   * The fix was to set the increment to -1. 
   * The error is not so obvious unless someone carefully traces the code and knows how narcissistic numbers work.
* Another error is that the code will keep running forever if a user entered a number greater than 88 in the **narc** function 
  because the 88th narcissistic number is the largest narcissistic number in **(base-10)** **(115132219018763992565095597973971522401)**
  and the code will keep incrementing until the max number in python. 
* It is not obvious to know what the largest narcissistic number is unless one looked it up prior to the program

## Errors with Perfect numbers code
* The error can be found in the **perfect_num** and **print_perfect_number** function. 
   * When looping through the numbers form 0 to 10,000, the error we pick up is that **0** is printed as a valid perfect number. 
   * Error such as these can easily be overlooked if the user fails to read the definition of what is considered a Perfect number.
* The integer 0 is not considered a perfect number because the definition of perfect number states that it's a positive integer. 
* To fix this we will be including another requirement in our if statement, in order to make sure the for loop does not considered 0 as a perfect number.
   * We will need to modify the if statement:
   * For the **perfect_num** function
     * Inside the for loop we will include an if statement **if(num == 0): return False**
   * For the **print_perfect_number** function
     * if statement will be changed from **if(perfect_num(i))** to **if(i != 0 and perfect_num(i))**

## Errors with Amicable numbers code
* When the **sum_proper_divisors** function is called on a perfect square, it incorrectly adds the square root twice. 
  * This was fixed by changing the range to 2 to n and adding divisors indvidually. 
  * This error isn't obvious because it only applies to perfect squares.
* The **get_amicables** function prints duplicate pairs. 
   * This was fixed by changing the function to use one for loop. 
   * This error isn't obvious because you have to run the code to discover it.
* The **get_amicables** function prints pairs that have the same value but by definiton amicable numbers are different. 
   * This was fixed by adding a greater than check. 
   * This error isn't obvious because you have to run the code to discover it.
