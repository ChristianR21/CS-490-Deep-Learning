#1
#Differences between Python 2 and 3
#in python 2 print is treated as a statement, not as a function
#python 2 has more libraries at the moment
#python 3 uses different syntax for error handling

#2 Take in 3 integers and then output the reverse of that
Number = int(input("Please Enter any Number: "))
Reverse = 0
while (Number > 0):
    Reminder = Number % 10
    Reverse = (Reverse * 10) + Reminder
    Number = Number // 10

print("Reverse is = %d" % Reverse)

user_num1 = int(input("Enter 1st num"))
user_num2 = int(input("Enter 2nd num"))
num3 = user_num2 + user_num1
print ("Added: " , num3)

#3
#Enter a sentence and then output the num of words, integers, and words
sentence = input("Enter a sentence")
sen_len = len(sentence)
print(sen_len)
letters = 0
words = len(sentence.split())
integers = 0
count = 0
for letter in sentence:
    count = count + 1
    if letter == '0':
        integers = integers + 1
    if letter == '1':
        integers = integers + 1
    if letter == '2':
        integers = integers + 1
    if letter == '3':
        integers = integers + 1
    if letter == '4':
        integers = integers + 1
    if letter == '5':
        integers = integers + 1
    if letter == '6':
        integers = integers + 1
    if letter == '7':
        integers = integers + 1
    if letter == '8':
        integers = integers + 1
    if letter == '9':
        integers = integers + 1
    if letter == ' ':
        count = count - 1

letters = count-integers
print ('Letters: ', letters)
print ('Words: ', words)
print ('Integers: ', integers)


