"""
An Armstrong number is a number that is equal to the sum of cubes of its digits. 
For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.

407 = 4^3 + 0^3 + 7^3

Errors in code:
- Line 26: improper syntax for cubing digits
- Line 25: Need to add the cube of the digit to the total sum
- Line 27: Need to round 
- Line 30: n should be num

"""


def is_armstrong_number():
  """
  @no params
  @returns True if the user input is an armstrong number,
  else returns False
    """
  num = int(input("Pick a whole number: "))
  n = num
  s = 0
  while(n != 0):
    digit = n % 10
    s += digit ** 3
    n /= 10
    n = round(n)
  if(s == num):
    return True
  else:
    return False

if __name__ == '__main__':
  is_armstrong_number()