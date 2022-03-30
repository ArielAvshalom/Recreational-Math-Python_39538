'''
Generating Kaprekar Numbers: 
The goal is to generate Kaprekar Numbers from 1 to a user inputted number.
generate_Kaprekar(300) -->  1, 9, 45, 55, 99, 297
We iterate through all the numbers, square them, then check both halves.
We print if the number is Kaprekar
'''


def generate_Kaprekar(end):
    # iterate
    for i in range(end):
        # get the square
        sqr = i ** 2
        digits = str(sqr)

        # and get the num of its digits
        length = len(digits)
        split = int(length/2)

        while length % 2 == 0:
            # split the squares into two halves
            left = int(digits[:split])
            right = int(digits[split:])

            # add the two halves to see if their sum is equal to the original number
            if (left + right) == i:
                print("Number: " + str(i) + " Square: " + str(sqr))
            break

if __name__ == '__main__':
    generate_Kaprekar(10000)
