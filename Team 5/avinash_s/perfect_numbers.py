def is_prime(n):
    for i in range(n):
        if i**2 != i:
            if n % i == 0:
                return False
    return True

def gen_mprime(k):
    while not is_prime(2**k - 1):
        k+=1
        # print(k)
    return k, 2**k -1


def gen_perfect(p):
    return (p*(p+1))/2

# print(is_prime(1))
# print(gen_mprime(6))

k = 1
for i in range(int(input('How many perfect numbers do you want to generate? '))):
    k +=1
    a = gen_mprime(k)
    k = a[0]
    mp = a[1]
    print(gen_perfect(mp))
