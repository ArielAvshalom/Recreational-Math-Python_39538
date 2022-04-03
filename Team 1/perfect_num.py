# Author: Andrew Alagna
# Team 1
# We already completed this before class and only copied our code to the repo.
def isPerfect( n ):
    """ Finding if a number is perfect or not.
    A Perfect Number N is defined as any positive integer where the sum of its divisors minus the number itself equals N.

    Args: n (integer): any number
    Output: true or false (string): outputs if the number is perfect or not
    Description:
        First we set a vairable to keep track of our sum.
        Then we iterate through all of the numbers leading up to N to check for divisors.
        If it is a divisor, we add it to our running sum.
        At the end of our loop, we check if the sum of the divisors is equal to N.

    @ Implicit errors and comments for code review:
        One edge case is if you input a number too large such as 999999999999
        Another error is that our running sum vairable sum0 must start at 0, not 1.
        We also need the condition to make sure sum0 >= 6 so we dont count 0 as perfect.
        We can increase optimization by adding an if statement returning false when the running sum > n.
        if sum0 > n:
                    return False
    """

    sum0 = 1 # must change to 0 to get correct sum.
    for i in range(1,n):
        #  if sum0 > n:
                    # return False  -- will slightly improve optimization
        if n % i == 0:
            sum0 += i

    if sum0 == n: print(f"{n} is a perfect number!") # must include 'and sum0 >= 6'

if __name__ == '__main__':
    # Test the first 4 perfect numbers -- 6, 28, 496, 8128
    for i in range(9999):
        isPerfect(i)
