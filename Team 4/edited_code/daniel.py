'''
The Pancake Flipping Problem: 
The goal is to get the largest number in the array at the end (bottom) using reversals only
Unsorted: [5, 4, 3, 2, 1] -->  Sorted: [1, 2, 3, 4, 5]
The simplest pancake sorting algorithm uses at most 2n -3 flips. 
Similar to selection sort we bring the largest number to the top of the array with one flip.
Then we take it to the end of the array with another flip.
We continue to do this until the array is sorted.
'''

from numpy import random

def create_random_array():
    '''
    Creates a random array of max size 20.
    The array will have only values up to 100 ordered randomly.

    @Args: None
    
    @Return: A random array of max size 20

    '''
    max_num = 20
    max_len = random.randint(max_num)
    arr = random.randint(100, size=(max_len))
    return arr

def find_largest(arr, size):
    '''
    Finds the largest value in a given array

    @Arg1: The array we'd like to find the largest value of
    @Arg2: The specified size of the array or the size of the 
    portion of the array you'd like to find the largest value of

    @Return: The largest value in the array or splice of the array

    '''
    index = 0
    for i in range(size):
        if arr[i] > arr[index]:
            index = i
    max = arr[index]
    return max, index

def reverse(arr, k):
    '''
    Reverses the order of the values in the array from a specified splice.

    @Arg1: The array that we will reverse the order of
    @Arg2: The specified size of the array or the size of the 
    portion of the array you'd like to reverse 

    @Return: Reverse ordered array
    '''
    a = 0
    while a < k :
        arr[a], arr[k] = arr[k], arr[a]
        a += 1
        k -= 1
    return arr

def sort(arr, size):
    '''
    Sorts the array from smallest (beginning) to largest (end) in at most 2n - 3 flips
    by checking whether the largest number is at the end of the array if its not then using
    reversals only it moves the largest number to the beginning (Index position 0) and then using
    another reversal it moves it to the end of the array,
    repeating this with the array but with the size - 1 each time until its sorted
    
    Also keeps track of the number of moves

    @Arg1: The array that we will sort
    @Arg2: The size of the array

    @Return1: The sorted array
    @Return2: Moves Required to sort the array
    '''
    moves_required = 0
    dsize = size
    while dsize > 1:
        li = find_largest(arr, dsize)[1]
        if li != size - 1:
            arr = reverse(arr, li)
            moves_required += 1
            arr = reverse(arr, dsize - 1)
            moves_required += 1
        dsize -= 1

    return arr, moves_required

def create_and_sort():
    '''
    Helper function that creates an array, sorts the array and 
    displays the presorted array and sorted array. 

    @Args: None
    @Return: None
    '''
    ex = create_random_array()
    print(f"The array pre-sort: {ex}")
    len_ = len(ex)
    ex, moves = sort(ex, len_)
    print(f"The array post-sort: {ex} with {moves} moves used")

if __name__ == '__main__':

    create_and_sort()





