import math
def sumofdiv(a):
    '''This function calculates the sum of all proper divisors of a number'''
    s=1 # Implicit error here
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            s += i
            if (a//i) != i:
                s += a//i
    return s
def check_ami(a,b):
    '''This function checks if the numbers are amicable using sumofdiv'''
    s=sumofdiv(a)
    p=sumofdiv(s)
    if b==s and a==p and a!=b:       # Implicit error here
        print('Yes Amicable')
    else:
        print('Not amicale')
print('This code finds if the two given numbers are amicable using')
print('Function sumofdiv()')
print(sumofdiv.__doc__,'\n')
print('Function checkami()')
print(check_ami.__doc__,'\n')
a=int(input('Enter number 1:'))
b=int(input('Enter number 2:'))
check_ami(a,b)

#This code can also find out pairs of amicable numbers in a range
# a=[]
# n=int(input('Enter range for amicable number:'))
# pairs=[]
# for i in range(n):
#     a.append(i)
# for i in range(n):
#     s=sumofdiv(i)
#     if s in a:
#         p=sumofdiv(s)
#         if i==p and i!=s and ([s,i] not in pairs):
#             pairs.append([i,s])

# print(pairs)