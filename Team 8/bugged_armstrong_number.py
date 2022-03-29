def narcissistic():
    num = int(input("Pick a whole number: "))
    n = num
    s = 0
    while(n != 0):
        digit = n % 10
        s = digit ^ 3
        n /= 10
    if(s == n):
        return True
    else:
        return False

if __name__ == "__main__":
    narcissistic()