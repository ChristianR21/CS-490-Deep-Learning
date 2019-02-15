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
