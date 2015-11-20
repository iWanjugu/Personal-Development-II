#  Using python, have a function that takes in a sentence
#  being passed and return the largest word in the string. If there are two or more
#  words that are the same length, return the first word from the string with that length.
#  Ignore punctuation and assume sentence will not be empty.

def longest_word(str):
    #split the string into a list of individual words
    word_list = str.split(" ")
    print(word_list)

    length_word = []  # will hold a list of the lengths of each word in the word_list
    for i in word_list:
        L = len(i)
        length_word += [L]
    print(length_word)

    # finding the index for the word with the longest length
    ind = (j for j, x in enumerate(length_word) if x == max(length_word))

    for j in ind:
        #Longest word will be at index 'ind'
        long_word = word_list[j]
        print(long_word)
        break;


longest_word("Android is almosts over!")


#-------------------------------------------------------------------------------
# #other solutions
# #more working code
# def longest_word(sentence):
#     #use list comprension
#     #return sorted(sentence.split(" "),key=len,reverse=True)[0]
#     #return max(sentence.split(" "),key=len)
# print(longest_word("Hello there bro how was you lovely day"))
#
#
#
# # check if this works which is a shorter version of
# stringlist = (['halla', 'hello', 'yahoo', 'hello'])
# print max(stringlist, key=len)
#
#
#
# # tversion of this one
# def longest_word(lists):
#     length = 0
#     longest = ''
#     for item in lists:
#         x = len(item)
#     if x > length:
#         length = x
#         longest = item
#     elif x == length:
#         if item not in list:
#             longest = longest + ' ' + item
#     return longest
# print longest_word(['halla', 'hello', 'yahoo', 'hello'])