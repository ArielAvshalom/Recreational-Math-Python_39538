#Updatedversion


# Line: As Python is case sensitive list_pn was changed to list_Pn
# Line 17: There is no starting value


def prime(x, y):
    """

    :param x: Integer
        the start of the range
    :param y: Integer
        the end of the range
    :return: List
        List of all the prime numbers in the rnge from x to y
    """
    list_Pn = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i / 2) + 1):
                if i % j == 0:
                    break
            else:
                list_Pn.append(i)
    return list_Pn


if __name__ == "__main__":
    user_input = int(input("Limit for Prime Numbers: "))
    list_Pn = prime(0, user_input)
    print(list_Pn)
