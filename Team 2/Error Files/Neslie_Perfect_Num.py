# -*- coding: utf-8 -*-
"""
Author: Neslie Fernandez
Team: 2

Perfect Number : Error 

A Perfect Number: 
    A positive integer that is equal to the sum of it's divisors, excluding the number itself.
    For example:
       
        6 has a divisor of 1,2, and 3
        By getting the sum of it's divisors: 1 + 2 + 3 = 6
        Therefore 6 is a perfect number.
        
    6, 28, 496, 8128
    
	Can you spot the error with the 2 methods given below?
	
"""

# This function takes in an integer and returns a true or false value whether a integer is a Perfect Number or Not.
def perfect_num(num): 
    """
    This function checks whether an input number is a perfect number.
   
    Parameters: 
    ------------------------
    num : integer value 
    
    Returns:
    ------------------------
    prints out a boolean True or False value 
    """
    
    # We will store our values that fits the divisor criteria based on the input num into this list 
    myList = []
    
    # For loop starts the range from 1 to the number. 
    for i in range(1,num):        
        # number divided by the index has a remainder of 0
        # it is then considered a divisor 
        # thus we add it to our list
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
    This function prints out the perfect number from 0 to 10,000.
    
    Parameters: 
    ------------------------
    None
    
    Returns:
    ------------------------
    prints out integers that are considered perfect number from 0 to 10,000 
    This case it will be 6, 28, 496, 8128
    """
    # out for loop will start a range from 0 to 10,001 (not including 10,001) 
    for i in range(10001):       
        # if the current index number satisfies our perfect_num function
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
#print(perfect_num(0))
#print_perfect_num()
