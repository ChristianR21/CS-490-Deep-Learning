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