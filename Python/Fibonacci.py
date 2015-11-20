# Fibonacci
# By definition, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number
# is the sum of the previous two.
#
# For example, the first ten Fibonacci numbers are:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
#
# Write a function that accepts a number and returns the number at that position in the fibonnaci sequence.
from Tools.Scripts.treesync import raw_input


def fibonacci():
    num = raw_input('Enter the item Number: ')
    num = int(num)
    # num = 5
    num_index = num - 1

    first_num = 0
    second_num = 1
    fib = [first_num, second_num]

    next_num = 0

    while num <= 2:
        next_num = fib[num_index]
        # print (next_num)
        break

    for i in fib:
        ind = (j for j, x in enumerate(fib) if x == i)
        for j in ind:
            # print(i) #the number in the list
            # print(j) #the index position of the number n the list (i)
            while len(fib) - 2 < j < num_index:
                last_num = fib[j]
                # print(last_num)
                second_last_num = fib[j - 1]
                # print(last_num)
                next_num = last_num + second_last_num
                fib += [next_num]
    print(fib)
    print(next_num)

fibonacci()
