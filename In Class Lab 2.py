# #1
# i = 100
# j = 0
# while i <= 500:
#     e = i % 200
#     if (e < 100):
#         i = i + 100
#
#     w = i%20
#     if (w < 10):
#         if ( i < 500):
#             i = i + 10
#
#     q = i%2
#     if (q == 0):
#         if ( i < 500):
#             i = i +1
#
#
#     print(i)
#     if ( i < 497):
#         i = i +2
#
#
#
# # #2
# mylist = ["1","4","0","6","9"]
# mylist.sort()
# #Gets size of list
# size = len(mylist)
# print("size:", size)
#
# n = 0
# int_mylist = []
# while n < size:
#     a = mylist[n]
#     print(a)
#     # Converts str into int
#     int_a = int(a)
#     int_mylist.append(int_a)
#     n = n +1
#
# print("New list:",int_mylist)


#3
word = 0
fileName = "lab2file.txt"
file = open(fileName, 'r')
line =file.readline()
while line != "":
    for str in line.split(" "):
        word = word + 1
        print(str)
    line = file.readline()

    print(word)



    # sen_len = len(sentence)
    # #print(sen_len)
    # letters = 0
    # words = len(sentence.split())
    # integers = 0
    # count = 0
    # for letter in sentence:
    #     count = count + 1
    #     if letter == '0':
    #         integers = integers + 1
    #     if letter == '1':
    #         integers = integers + 1
    #     if letter == '2':
    #         integers = integers + 1
    #     if letter == '3':
    #         integers = integers + 1
    #     if letter == '4':
    #         integers = integers + 1
    #     if letter == '5':
    #         integers = integers + 1
    #     if letter == '6':
    #         integers = integers + 1
    #     if letter == '7':
    #         integers = integers + 1
    #     if letter == '8':
    #         integers = integers + 1
    #     if letter == '9':
    #         integers = integers + 1
    #     if letter == ' ':
    #         count = count - 1
    #         letters = letters -1
    #
    # letters = count - integers
    # print(sentence)
    # print('Letters: ', letters)
    # print('Words: ', words)
    #
    # print('Integers: ', integers)
    #
    #
    #
