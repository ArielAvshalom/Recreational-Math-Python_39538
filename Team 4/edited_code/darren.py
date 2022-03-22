
def generate_Kaprekar(end):
    # iterate
    # BUG HERE THE LAST NUMBER IS NOT LOOKED AT WHATSOEVER
    for i in range(end):
        # get the square
        sqr = i ** 2
        digits = str(sqr)

        # and get the num of its digits
        length = len(digits)
        split = int(length/2)

        while length % 2 == 0:
            # split the squares into two halves
            # BUG HERE : WE DONT WANT ODD NUMBER OF DIGITS FOR A SQUARE NUMBER
            left = int(digits[:split])
            right = int(digits[split:])

            # add the two halves to see if their sum is equal to the original number
            if (left + right) == i:
                print("Number: " + str(i) + " Square: " + str(sqr))
            break

if __name__ == '__main__':
    generate_Kaprekar(10000)
