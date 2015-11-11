# Dash Insert
# Using python, have the function DashInsert(str) insert dashes ('-') between each two odd numbers in string.
# For example: if str is 454793 the output should be 4547-9-3. Don't count zero as an odd number.

string = str(235)
print(string)
str_list = []

L = len(string)

length = range(0, L-1)

for i in length:
    print(string[i])

    if int(string[i]) % 2 == 0:
        str_list += string[i]
        print(str_list)

    elif int(string[i]) % 2 != 0 & int(string[i + 1]) % 2 == 0:
        str_list += string[i]
        print(str_list)

    elif int(string[i]) % 2 != 0 & int(string[i + 1]) % 2 != 0:
        str_list += (string[i] + "-")
        print(str_list)

str_list += string[L-1]
print (str_list)


        # while(int(j)%2 != 0):
        #     if (int(string[i+1]) %2 != 0):
        #         str_list += (j + "-")
        #     else:
        #         str_list += j
        #
        #     print(str_list)
