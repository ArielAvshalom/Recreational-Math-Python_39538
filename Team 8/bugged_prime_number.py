def prime(x, y):
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
    return list_pn


if __name__ == "__main__":
    user_input = int(input("Limit for Prime Numbers: "))
    list_Pn = prime(user_input)
    print(list_Pn)