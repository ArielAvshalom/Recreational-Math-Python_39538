#there is a bug here
# this one has no user input
c = 0
for n in range(4, 10):
    for d in range(1, n+1):
        if n % d == 0:
            c = c+1
        if c > 2 or n == 1:
            print(f"{n} not prime")
    if c == 2:
        print(f"{d} is prime")