# FIND MISSING ELEMENT
#
# There is an array of non-negative integers.
# A second array is formed by shuffling the elements of the first array and deleting a random element.
# Given these two arrays, find which element is missing in the second array.
# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
#
#  first array = [4,1,0,6,2,9,6,8,7,5,3]
#
#  second array = [6,4,7,2,1,0,8,3,9]


a = [4,1,0,6,2,9,6,8,7,5,3]
b = [6,4,7,2,1,0,8,3,9]

# print (a==b)
# print(a)
# print(b)

missing = (x for x in a if x not in b)
print(list(missing))
