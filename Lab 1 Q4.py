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

