i = int(input("What prime number do you want to stop at: "))
for n in range(1, i + 1):
    c = 0
    for d in range(1, n+1):
        if n % d == 0:
            c = c + 1
        if c > 2 or n == 1:
            if c == 3:
                print(f"{n} is not a prime number because it is also divisible by {d} ")
                break
    if c == 2:
        print(f"{n} is prime")