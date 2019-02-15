#Chrisitan Rodas
#490-0003
#Question 5
#This is a management program that utililizes class
#The base class is the AMS and that sets basic information that can be inherited by other classes
#The Employee class sets the hourly wage and job position of an employee.
#The Passenger class uses the information from the AMS class and uses that to determince the seat size for passengers
#The Plane class uses the super call and is for the type of plane
#The Destination class calculates the cost for flight to the USA or Europe

#AMS = Airline Management System
class AMS:
    def __init__(self):
        self.name = ""
        self.age = 0
    def set_name(self):
        self.name = input("Please enter your name: ")
    def get_name(self):
        return self.name
    def set_age(self):
        self.age = int(input("Please enter your age: "))
    def get_age(self):
        return self.age

class Employee:
    def __init__(self):
        self.hr_wg = 0.00
        self.job_position = ""
    def set_hr_wg(self):
        self.hr_wg = float(input("Enter employee's salary hourly wage: "))
    def get_hr_wg(self):
        return self.hr_wg

    def set_job_postion(self):
        self.job_position = str(input("Enter employee's job position: "))
    def get_hr_wg(self):
        return self.hr_wg

class Passenger(AMS):
    def __init__(self):
        self.seat_size = ""

    def get_seat_size(self, age):
        if self.age < 12 :
            self.seat_class = "Small Seat"
            return self.seat_size
        elif self.age >= 12 and self.age < 18:
            self.seat_class = "Medium Seat"
            return self.seat_size
        elif self.age >= 18:
            self.seat_class = "Large Seat"
            return self.seat_size
        else:
            print("Invalid age. No seat assigned")
            return self.seat_size


class Plane:
    def __init__(self):
        super(Plane, self).__init__()
        self.plane_type = "Jet"


class Destination_Cost:
    def __init__(self):
        #Private Member
        self._location = ""

    def fly_cost(self):
        location = str(input("Press 1 for USA and 2 for Europe"))
        if location == "1":
            return 500
        elif location == "2":
            return 1000





passenger_1 = Passenger()
passenger_1.set_name()
passenger_1.set_age()

#This utilizes the Passenger class, which inherites the AMS class
#This will ouput the age, name and seat size for the passenger
print("Passenger Information: ")
print("Name:", passenger_1.get_name(), "Age:", passenger_1.get_age(),)
print("Seat Size: ", passenger_1.get_seat_size(99))

#This is the Plane class and has the super call
Plane_1 = Plane()

#This utilizes the Desination Cost class and determines flight cost
destinations_1 = Destination_Cost
print("Travel Cost: ", destinations_1.fly_cost(1),"$")

#This utilizes the Employee Class and some basic functions
employee_1 = Employee()
employee_1.set_hr_wg(20.0)
employee_1.set_job_postion()