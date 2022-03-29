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

def get_length(arr):
    return len(arr)

def find_largest(arr, size):
    index = 0
    for i in range(size):
        # print(f"the current i is {i}")
        if arr[i] > arr[index]:
            index = i
    max = arr[index]
    # print(max)
    return max, index

def reverse(arr, k):
    a = 0
    while a < k :
        arr[a], arr[k] = arr[k], arr[a]
        a += 1
        k -= 1
    return arr

def sort(arr, size):
    moves_required = 0
    # BUG HERE because we declare the size to be the full length of the array everytime, so we need to pass the size in the function itself
    # size = len(arr)
    dsize = size
    while dsize > 1:
        # BUG HERE : giving the wrong array size to the find_largest function
        li = find_largest(arr, size)[1]
        num = find_largest(arr, size)[0]
        print(num)
        if li != size - 1:
            arr = reverse(arr, li)
            moves_required += 1
            arr = reverse(arr, size - 1)
            moves_required += 1
        dsize -= 1

    return arr, moves_required



if __name__ == '__main__':
    ex = create_random_array()
    print(f"The array pre-sort: {ex}")
    len_ = len(ex)
    ex, moves = sort(ex, len_)
    print(f"The array post-sort: {ex} with {moves} moves used")
    # ex = reverse(ex, 2)
    # print(ex)
    # print(find_largest(ex))





