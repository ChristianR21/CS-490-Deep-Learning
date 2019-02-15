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

