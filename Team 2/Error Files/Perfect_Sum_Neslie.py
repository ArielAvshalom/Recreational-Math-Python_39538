# -*- coding: utf-8 -*-
"""
Author: Neslie Fernandez
Group: 2

Perfect Number

A Perfect Number: 
    
    A positive integer that is equal to the sum of it's divisors, excluding the number itself.
    For example:
       
        6 has a divisor of 1,2, and 3
        By getting the sum of it's divisors: 1 + 2 + 3 = 6
        Therefore 6 is a perfect number.
    6, 28, 496, 8128
    
"""

# This function takes in an integer and returns a true or false value whether a integer is a Perfect Number or Not.
def perfect_num(num): 
    """
    This function checks whether a number is a perfect number
   
    Parameters: 
    ------------------------
    num : integer value 
    
   Returns:
   ------------------------
   a boolean True or False value 
    
    """
    
    # We will store our values into a list 
    myList = []
    
    # For loop starts ranging 
    for i in range(1,num):
        # if the number is a perfect divisor of that index 
        # We append it to the list 
        if(num % i == 0):
            myList.append(i)
            
    # If the sum of our list equals to our input num
    # then we return True, otherwise False. 
    if(sum(myList) == num):
        return True
    else:
        return False

# This function prints out a perfect number starting from 0 to 10,000.
def print_perfect_num():
    """
    This function prints out the perfect number from 0 to 10,000
    
    Parameters: 
    ------------------------
    None
    
   Returns:
   ------------------------
   prints an integer 
   perfect number from 0 to 10,000, this case it will be 6,28,496,8128

    """
    # out for loop will start a range from 0 to 10,001 (not include 10,001) 
    for i in range(10001):       
        # if the current index number satisfies our perfect_num method 
        # we print out the index number
        # otherwise we ignore it
        if(perfect_num(i)):
            print(i)


   
# Test Drive
#print(perfect_num(6))
#print(perfect_num(28))
#print(perfect_num(496))
#print(perfect_num(8128))
#print(perfect_num(3))
#print(perfect_num(-28))
#print_perfect_num()