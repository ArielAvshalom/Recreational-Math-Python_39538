def is_armstrong_number(num):
    """
    Task: Determine if a number is an Armstrong number
    Definition: a number that is equal to the sum of each of its cubed digits
    Ex. 153 -> 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 , IS ARMSTRONG

    Arg: num: any whole number
    Output: True or False

    Process:
        Create array to hold cubed digits for later summation
        Iterate through the input via a while loop as long as the input > 1
            Store number divided by 10 as digit
            digit^3 appended to array
            Divide input var by 10

        if sum of digits in arr == input,
            return true if yes
        else return false

    IMPLICIT ERRORS
    1. not copying original input into a variable  if( sum(cubed_digits) == num <----- ):
       (will be comparing sum to num not same as original), one solution: make num copy and == copy instead

    2. int(num // 10 <--------), solution: % instead as it will be the digit

    3. 1 as input won't work bc while num > 1: prevents 1 from having a cube be put in arr so arr is empty ,
       one solution: base case of arg 1, another solution: change 1 to 0 and num /= 10 -> //=
    """

    cubed_digits = []
    while num > 1:
        digit = int(num // 10)
        cubed_digits.append(digit * digit * digit)
        num /= 10

    if sum(cubed_digits) == num:
        return True
    else:
        return False



def is_armstrong_number_fixed(num):
    copy = num
    cubed_digits = []
    while num >= 1:
        digit = int(num % 10)
        cubed_digits.append(digit * digit * digit)
        num /= 10

    if sum(cubed_digits) == copy:
        return True
    else:
        return False



#These should work, all other numbers in between should fail
# arr = [0, 1, 153, 370, 371, 407]
# for v in arr:
#     print(is_armstrong_number(v))







