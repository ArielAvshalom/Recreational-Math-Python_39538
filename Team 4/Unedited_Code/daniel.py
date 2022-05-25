# pancake flipping problem
# The goal is to get the largest number in the array at the end (bottom)
# so 1 2 3 4 5
# using reversal only
# The simplest pancake sorting algorithm performs at most 2n − 3 flips. In this algorithm, a kind of selection sort,
# we bring the largest pancake not yet sorted to the top with one flip; take it down to its final position with one more flip; and repeat this process for the remaining pancakes.
from numpy import random

def create_random_array():
    max_num = 20
    max_len = random.randint(max_num)
    arr = random.randint(100, size=(max_len))
    return arr

def find_largest(arr, size):
    index = 0
    for i in range(size):
        if arr[i] > arr[index]:
            index = i
    max = arr[index]
    return max, index

def reverse(arr, k):
    a = 0
    while a < k :
        arr[a], arr[k] = arr[k], arr[a]
        a += 1
        k -= 1
    return arr

'''
BUG HERE: Need to pass the size of the array in the function. We need to call reverse function multiple times with a decreasing array size.
If we dont pass the size it becomes extremely difficult to monitor the size of the unsorted segment of the array.
'''
def sort(arr):
    moves_required = 0
    size = len(arr)
    while size > 1:
        '''
        BUG HERE : We declare the size to be the full length of the array everytime, so we need to pass the size in the function itself
        It isn't immediately obvious until you see that because we are using incorrect size of the array we are actually getting the wrong largest number 
        in the splice of that array
        In addition to making cutting the array short by 1 as well
        ''' 
        li = find_largest(arr, size - 1)[1]
        if li != size - 1:
            arr = reverse(arr, li)
            moves_required += 1
            '''
            BUG HERE : We declare the size to be the full length of the array everytime, so we need to pass the size in the function itself
            It isn't immediately obvious until you see that because we are using incorrect size of the array we are actually getting the wrong largest number 
            in the splice of that array
            ''' 
            arr = reverse(arr, size - 1)
            moves_required += 1
        size -= 1

    return arr, moves_required

'''
We also added a function that creates an array and sorts using the other function for a clearer respresentation of what we are doing.
'''

if __name__ == '__main__':
    ex = create_random_array()
    print(f"The array pre-sort: {ex}")
    ex, moves = sort(ex)
    print(f"The array post-sort: {ex} with {moves} moves used")
    # ex = reverse(ex, 2)
    # print(ex)
    # print(find_largest(ex))





