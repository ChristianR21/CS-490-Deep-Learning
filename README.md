# CS-490-Deep-Learning

#Question 1
#This program will compute the net amount of a bank accounted based on a transaction
#log from the log console input.

#Program Summary:
# Program asks user for starting balance and will then open the banking program
# A menu will open showing the availabe options and will rerun if invalid input is selected
# User can begin to commit transaction (*prevents user from withdrawing more than available funds)
# Program ends when user selects 4

#The menu function will print the available options for the user
def menu(starting_amount):
    u_num = '0'
    balance = starting_amount - 0

    while (u_num != '4'):   #This will create a loop so user can do multiple transactions
        print("Hello! Welcome to the Banking App")
        print("Press 1: To view your current balance.")
        print("Press 2: To deposit money into your account.")
        print("Press 3: To withdraw money from your account. ")
        print("Press 4: To exit the Banking App. ")

        u_num = input(print("Please select the number that coordinates with your desired selection."))

        if u_num == '1':
            print("Here is your current balance: %d$" % balance)
        elif u_num == '2':
            dep_num = int(input(print("How much would you like to deposit? ")))
            balance = balance + dep_num
        elif u_num == '3':
            withdraw_num = int(input(print("How much would you like to withdraw? ")))
            balance = balance - withdraw_num
            if balance < 0:
                print("Insufficient funds. Try again.")
                balance = balance + withdraw_num
        elif u_num == '4':
            print("Exiting Banking App. Have a great day!")
        else:
            print("Invalid Option. Try again")

#This will ask for starting balance
starting_amount = int(input(print("Enter starting amount")))
#Starts the banking app
menu(starting_amount)

![alt text](C:\Users\Reshi\OneDrive\Pictures\Screenshots)


#Chrisitan Rodas
#490-0003
#Question 2
#The objective is to take in a tuple and return it with a dictionary of lists
#First, the lists are and data is set up
#Then the tuple is iterated through. If the key(name) is found already inside the dictionary
#then it is added to a temp list along with default data. That temp list will then be set the key's(name) the new data(class info)
#finally, it will print the dictionary


#Sets up the problem with information
m_tuple = [('John', ('Physics', 80)), ('Daniel', ('Science', 90)), ('John', ('Science', 95)), ('Mark', ('Maths', 100)), ('Daniel', ('History', 75)), ('Mark', ('Social', 95))]
m_dict = {}
temp_list = ()

#Then it is iterated through
for info in m_tuple:
    #print("info: ",info)   #verifier
    key = info[0]
    class_info = info[1]
    #print("Name: ",key," Class Info: ",class_info) #verifier

    #creates list if key used more than once
    if key in m_dict:
        old_data = m_dict[key]
        #print("old data", old_data)    #verifier
        temp_list = (old_data, class_info)
        #print("Temp list", temp_list)  #verifier

        m_dict[key] = temp_list
    else:
        m_dict[key] = class_info

#outputs the final dictionary
print("The dictionary: ", m_dict)


![alt text](C:\Users\Reshi\OneDrive\Pictures\Screenshots)

#Chrisitan Rodas
#490-0003
#Question 3
#The objective is to be able to print to the user students who are both classes and those that are in only one
#First is set a basic lists of the classes
#Then if user wants, they can add more students to lists
#Finally the program will prints the 2 types of students


#Starting lists
python_students = ['Chris', 'Bob', 'John', 'Sally', 'Tom']

web_app_students = ['Chris', 'Billy', 'Joe', 'Sally', 'Amy', 'Ken']


#Add more students
add_student = 'y'
while add_student == 'y':
    add_student = str(input(print("Press 'y' to add a student to the Python students list and 'n' to not.")))
    if add_student == 'y':
        new_student_name = str(input(print("Enter the students name: ")))
        python_students.append(new_student_name)
    else:
        add_student = 'n'

print("Here are the Python Students: ")
for students in python_students:
    print(students)

add_student = 'y'
while add_student == 'y':
    add_student = str(input(print("Press 'y' to add a student to the Web App students list and 'n' to not.")))
    if add_student == 'y':
        new_student_name = str(input(print("Enter the students name: ")))
        web_app_students.append(new_student_name)
    else:
        add_student = 'n'

print("Here are the Web Applications Students: ")
for students in web_app_students:
    print(students)



#Find students who attend both class
students_in_both = set(python_students) & set(web_app_students)
print("These are the students in both classes: ", students_in_both)

#Students that aren't in both, just one
students_in_one = students_in_both
all_students = python_students + web_app_students
students_in_one = students_in_one.symmetric_difference(all_students)

print("These are the students that are in only one class: ", students_in_one)

![alt text](C:\Users\Reshi\OneDrive\Pictures\Screenshots)

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
    #print("x:",x,"y",y)

#if letters are repeated, then it adds to substring length
    if x == y:
        print("repeat")
        substring = substring + 1
        substring_letter = y
    i += 1

#outputs longest substring and the corresponding letter
print("Longest substring is:",substring," and the letter is: ",substring_letter)


C:\Users\Reshi\OneDrive\Pictures\Screenshots

