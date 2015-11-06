__author__ = 'iWanjugu'
# Make larger number
# Solve the problem below using PYTHON
# Given a number whose digits are unique, find the next larger number that can be formed with those digits.
# For example: 241 will output 421, 27 will output 72 and 68734 will outyput 87643


num = 573
str = str(num)
# print (str[0])

g = []
for i in str:
    # print (i)
    g = g + [int(i)]
print(g)



while len(g) >= 1:
    q = []
    mg = max(g)

    # add maxto new list
    q = q + [mg]
    t=map(str, q)

    # remove max from previous list
    g.remove(mg)

print(t)

large = "".join(t)
