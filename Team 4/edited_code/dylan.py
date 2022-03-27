"""
perfect numbers are numbers whose factors (excluding itself) sum to itself

------------------------------------

e.g.

The factors of 6 are 1, 2, 3, and 6

1+2+3=6, so 6 is a perfect number. 

------------------------------------

"""



import math

def get_divisors(num):
	returnarray=[]

    # Correction
	for i in range(1, (num) + 1):
		if (num % i) == 0 and i != num:
			returnarray.append(i)

	# square_root=int(math.sqrt(num))
	
	# for i in range(square_root, 0, -1):
	# 	if num % i == 1:
	# 		returnarray+=[int(i),int(num/i)]
	
	# returnarray.append(1)
	return returnarray


def generate_perfect_numbers(amount):
	# Correction 
	for num in range(1, amount):
		if sum(get_divisors(num)) == num:
			print(num)


if __name__ == "__main__":

	get_divisors(8)
	generate_perfect_numbers(100)