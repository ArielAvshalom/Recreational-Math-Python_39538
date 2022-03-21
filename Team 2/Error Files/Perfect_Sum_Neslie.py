# -*- coding: utf-8 -*-
"""
Author: Neslie Fernandez
Perfect Num

A Perfect Number: 
    A positive integer that is equal to the sum of it's divisors, excluding the number itself.
    For example:
        6 has a divisor of 1,2, and 3
        1 + 2 + 3 = 6
        Therefore 6 is a perfect number.
    6,28,496,8128
"""

def perfect_num(num): 
    """
    This function checks whether a number is a perfect number
    This returns a true or false value
    """
    myList = []
    for i in range(1,num):
        if(num % i == 0):
            myList.append(i)
    if(sum(myList) == num):
        return True
    else:
        return False


def print_perfect_num():
    """
    This function prints out the perfect number from 0 to 1000
    """
    for i in range(1000):
        if(perfect_num(i)):
            print(i)


'''     
# Test Drive
print(perfect_num(6))
print(perfect_num(28))
print(perfect_num(496))
print(perfect_num(8128))
print(perfect_num(3))
'''

