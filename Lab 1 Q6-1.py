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
    result_list = soup.findAll('table', class_= "wikitable"}
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