# Fnu Tsering
# Recreational Math (Group 3)

"""
Number 6174 is known as Kaprekar’s constant after the Indian mathematician D. R. Kaprekar.
This constant is special because if you take any four-digit number (in which all four digits are NOT identical)
and you follow Kaprekar's procedure, it can be converted into Kaprekar’s constant in at most 8 iterations.

Kaprekar's Procedure:
1. 	Start with a 4-digit number where the 4 digits aren't all be the same (at least 2 digits must be unique).
	Leading 0s are allowed.
2.	Take the 4-digit number and produce 2 new numbers from it by rearranging its digits
	in descending and ascending orders.
3.  Subtract the smaller number (ascending order) from the bigger number (descending order).
4.  Take the difference and check to see if that number is Kaprekar's constant 6174.
	If yes, then you have arrived at the Kaprekar's constant.
	Else, take that number and repeat steps 2-4.
"""


def generate_kaprekar(n, count=1):
    num_str = str(n)


    # Rearrange digits of n in ascending order
    digits_asc_list = sorted(num_str)
    num_in_asc = int("".join(digits_asc_list))

    # Rearrange digits of n in descending order
    digits_desc_list = sorted(num_str, reverse=True)
    num_in_desc = int("".join(digits_desc_list))

    # Get the difference between the two numbers by subtracting the smaller number from the bigger number.
    diff = num_in_desc - num_in_asc

    # If the difference is the 3-digit number 999, add a leading 0 to it to make sure number has 4 digits.
    if len(num_str) == 3:
        diff = int(f"0{diff}")

    print(diff)

    # Check to see if the difference is the Kaprekar's constant. If not, apply the procedure on that number.
    if diff == 6174:
        print(f"Arrived at Kaprekar's constant.\nTook {count} iterations.")
        return diff
    else:
        generate_kaprekar(diff, count + 1)  # recursive call with the new number


if __name__ == '__main__':
    while True:  # Keep prompting user for the number until the conditions are met
        num = (input("Enter a 4-digit number in which all digits are NOT identical: "))
        all_digits_same = all(digit == str(num)[0] for digit in str(num))  # returns True if all digits are same in num
        if len(str(num)) == 4 and not all_digits_same:
            break
    kaprekar_constant = generate_kaprekar(num, count=1)


"""
ERROR FOUND BY Serrin Doscher:
    Leading 0's do not allow the code to run
    Fix: remove int from line 55 when asking for input
    
ERRORS FOUND BY Perla, Escano, Estrealla:
    The code gets stuck in loop with leading 0's
"""