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
employee_1.set_hr_wg()
employee_1.set_job_postion()

#Chrisitan Rodas
#490-0003
#Question 6
#First import libraries needed to parse a webpage and extract specific data from it
#Then get the URL using requests and parse it using BS4
#Next, find the where the data is on the webpage and extract that
#So in this case,it would be in the class wikitable
#Then iterate through the table, extracting the countries' info and appending them to a list
#Finally, export the list of countries onto a file

#Errors: I keep getting Response [404] everytime I run the program and I couldn't figure out
#wny so I was unable to produce any ouput. I did try parsing on another file (Lab 1 Q6-2) and was able
#to get output but not on this file.

import requests
import urllib.request
from bs4 import BeautifulSoup
import os

#This function gets the url and parses.
#it also write to another file
def get_data(url):
    source_code = urllib.request.urlopen(url)
    plain_text = source_code
    soup = BeautifulSoup(plain_text, "html.parser")
    body = soup.find('table', class_= 'wikitable')
    file2.write(str(body.text))
    print(body.text)

#This function searches the webpage using user's search and limit
def search_spider(sch,lim):
    url = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"+lim+"&offset=0&search="+sch
    source_code = requests.get(url)
    print(source_code)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    result_list = soup.findAll('table', class_= "wikitable")
    for tr in result_list:
        print(tr)
        link = tr.find('a')
        href = "https://en.wikipedia.org"+link.get('href')
        get_data(href)



search = input('What state do you want to search in the wiki? ')
limit = input('How many results do you wish to receive? ')

if not os.path.exists(search):
    print("Creating file " + search)
    file2 = open(search+'.txt','a+',encoding='utf-8')

search_spider(search, limit)


#Chrisitan Rodas
#490-0003
#Question 6
#First import libraries needed to parse a webpage and extract specific data from it
#Then get the URL using requests and parse it using BS4
#Next, find the where the data is on the webpage and extract that
#So in this case,
#Then iterate through the table, extracting the countries and appending them to a list
#Finally, export the list of countries onto a file

#This library is for connecting to url's
import requests
import urllib.request

#This library will parse the webpage for easier manipulation
from bs4 import BeautifulSoup

#Gets the desired url
web_url = requests.get("https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States").text

#This essentially is the webpage's data parsed
#and I used since lxml since that's what I read is good for processing xml and html in python
soup = BeautifulSoup(web_url,'lxml')
#print(soup.prettify())


#My_table = soup.find('table',{'class':'wikitable_sortable'})
#So looking at the html code on the wikia pg, find where the data is under
#and put those tags into the find() method
My_table = soup.find('table', class_="wikitable")
#print(My_table)

#Since the the data(countries) are in links, find the links using 'a'
links = My_table.findAll('a')
#print(links)

#Then create a list to store the countries
countries = []

#Then iterate through the links, grabbing the titles which holds the countries
for link in links:
    countries.append(link.get('title'))

#Then print the countries
print(countries)
