#Chrisitan Rodas
#490-0003
#Question 4
#This program takes in a string and finds the longest substring of repeating characters
#First it takes in user input
#then saves it to a list so that it can be iterated through
#during the iteration, it counts if the letter are repeated
#Finally, it outputs final result

#asks user for input
user_str = str(input("Enter a string: "))
str_list= []

#puts the user string's letter's into a list
for letter in user_str:
    #print(letter)
    if letter != " ":
        str_list.append(letter)



print(str_list)
#print(str_list[1])

list_len = len(str_list)
print("length", list_len)

#sets base value
i = 1
substring = 1
substring_letter = ""
#iterates through the list and matches the current letter to the prevoius letter
while i < list_len:
    x = str_list[i]
    j = i - 1
    y = str_list[j]
    print("x:",x,"y",y)

#if letters are repeated, then it adds to substring length
    if x == y:
        print("repeat")
        substring = substring + 1
        substring_letter = y
    i += 1

#outputs longest substring and the corresponding letter
print("Longest substring is:",substring," and the letter is: ",substring_letter)




# usr_str = str(input("Enter a string"))
# char_nums = 256
#
# #This function takes in the user's string, finds the size and sets base values
# def longest_substring(user_str):
#     length = len(user_str)
#     max_l =1
#     current_l = 1
#     p_index = 0 #This will store the prevoius index of the stirng
#
# #For repeating characters
#     found = [-1] * char_nums
#     found[ord(user_str[0])]
#
# #iterates through the string, counting repeating letters
#     for i in range(1,length):
#         p_index = found[ord(user_str[i])]
#
#         if p_index == -1 or (i-current_l > p_index):
#             current_1 = current_l + 1
#
#         else:
#             if current_1 > max_l:
#                 max_l = current_l
#
#
#             current_l = i - p_index
#
#         found[ord(user_str[i])] = 1
#
#     if current_1 > max_l:
#         max_l = current_1
#     return max_l
#
# length = longest_substring(usr_str)
# print("The longest substring is: ", str(length))