# Given a sorted array of unknown length and a number to search for, return the index of the number in the array.
# Accessing an element out of bounds throws exception.
# If the number occurs multiple times, return the index of any occurrence. If it isn’t present, return -1.

def searchArr(n):

    arr = [1,2,3,4,5,6,3,10,77,3]
    # finding the index for number n
    ind = (i for i, x in enumerate(arr) if x == n)
    print (list(ind))

searchArr(3)