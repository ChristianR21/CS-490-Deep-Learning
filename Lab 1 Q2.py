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

