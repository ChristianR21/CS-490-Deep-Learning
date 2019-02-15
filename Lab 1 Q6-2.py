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
print(My_table)

#Since the the data(countries) are in links, find the links using 'a'
links = My_table.findAll('a')
print(links)

#Then create a list to store the countries
countries = []

#Then iterate through the links, grabbing the titles which holds the countries
for link in links:
    countries.append(link.get('title'))

#Then print the countries
print(countries)