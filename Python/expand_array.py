__author__ = 'iWanjugu'

#EXPAND THE ARRAY

#You are given a character array like this a3b1c1d1e4f0g11.
#You will have to expand the array by repeating the characters denoted by the following numbers.
#For example the above character array will be expanded to aaabcdeeeeggggggggggg.
#The given array will have more than enough trailing spaces such that you can modify the array in place.

str = "a3b1"

print(str)
print(str [1])
#
# j = len(str)
# print(j)
range (0,100000)
exp = []

str_ = list(str)

for i in str_:
    # print(i)
    if i.isalpha():
        print(i)
        pos = (i for i, x in enumerate(str_) if x == i)
        for z in pos:
            print(z)
