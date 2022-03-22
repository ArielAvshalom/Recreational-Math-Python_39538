#Generating a perfect number
"""
Basic Background: Perfect numbers are numbers which equals to sum of all existing proper factors
(numbers which are divisible to it excluding itself)
        Another definition, perfect # are said to be equal to sum of all of factors (including itself) which is twice the current number.

eg: 6 = 1+2+3
    28 = 1+2+4+7+14
    496 = 1+2+4+8+16+31+62+124+248

    Mersenne primes proof 
         2^n -1 = Prime number
        Pattern: If 2^n -1 is prime, then n must have been prime 

    Open questions
    Perfect numbers so far tends to be only even numbers so far. Odd perfect numbers have still not proven yet. 


Errors introduced and found:
- factors including itself. (correction: Should only be proper factors)
- factors can't be 0.
- number shouldn't be started at 0. (should start from 1)
- limit_num shouldn't have 1 added to it. 
"""


"""Corrected format"""
def generate_perfect(limit_num):
    """
    Function description:
    Generate perfect numbers upto user specified limit.
    @params gets a integer as input which is limit number upto which you want to generate prime numbers
    @returns array of integers where each element is a perfect number. 
    """
    ans = []
    num = 1
    while num != limit_num:
        temp_sum = 0
        for factors in range(1, num):
            if num % factors == 0:
                temp_sum += factors
        if temp_sum == num:
            ans.append(num)
        num += 1
    return ans



if __name__ == "__main__":
   user_input = int(input("Up to what limit you want to get perfect numbers: "))
   ans = generate_perfect(user_input)
   print(ans)
