import requests
from bs4 import BeautifulSoup
import urllib.request
import os

#This parses the pg
html = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
parsedObj = BeautifulSoup(html.content, "html.parser")
print(parsedObj)

#this prints the title of the pg
print("Printing the title: ")
print(parsedObj.title)

#This finds all the links in the wiki pg with the 'a' tag and
#then iterates each tag, returning the link using the 'href' attribute
for link in parsedObj.find_all('a'):
    print(link.get('href'))
