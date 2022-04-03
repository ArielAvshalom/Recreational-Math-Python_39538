#Serrin Doscher
#CSCI 39538
#Recreational Math (Group 3)

"""
An automorphic number is a number which is present in the last digit(s) of its square.
Example: 25 is an automorphic number as its square is 625 and 25 is present as the last digits.

A number is said to be a Magic number if the sum of its digits are calculated
till a single digit is obtained by recursively adding the sum of its digits.
If the single digit comes to be 1 then the number is a magic number.
"""

#====== Automorphic Number ======#
def Automorphic(number):
    square_num = number * number
    number_length = len(str(number))
    last_digits = int(str(square_num)[-number_length:])

    if last_digits == number:
        (print(f'{number} squared is {square_num}\n'
              f'This is an Automorphic number\n'))


    else:
        (print(f'{number} squared is {square_num}\n'
              f'This is NOT an Automorphic number\n'))

    return 0

#====== Magic Number ======#
def MagicNum(number):
    digits = [int(x) for x in str(number)]

    digit_sum = 0
    if (number == 1):
        return True
    if (number < 10):
        return False

    while (number != 0):
        digit_sum += int(number % 10)
        number = int(number // 10)

    print(*digits, sep=' + ', end=' = ')
    print(digit_sum)
    return MagicNum(digit_sum)

user_num = int(input("Enter a number: "))

Automorphic(user_num)

if MagicNum(user_num):
    print(f'{user_num} is a Magic Number')
else:
    print(f'{user_num} is NOT a Magic Number')


"""
ERRORS FOUND BY Fnu, Tsering
    The one I found is that the last_digits extracted from the number 
    is a string while number is integer so when comparing last_digits to number, 
    it always evaluates to false even if the number is same.
    
    Wrong operator used. Used division instead of modulus operator to extract the digits
    of the number, which gives incorrect value for the sum of the digits.
     Fix: digit_sum += int(number % 10)
     
    Too many print statements in 21 and 26
ERRORS FOUND BY Perla, Escano, Estrealla
    #1 line 18: last_digits  should have an int casting  
        last_digits = int(str(square_num)[-number_length:])
    #2 Line 42: wrong output: need to mod number not divede 
        fix: digit_sum += int(number % 10)
    #3 Line 21, 26: Two print statements, printing None
        fix: remove the first print on both lines
"""