# Build a script that scrapes all links from a webpage using BeautifulSoup.

import requests
from bs4 import BeautifulSoup

url = input("Enter a url: ")
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

links = soup.find_all('a')
for a_href in soup.find_all("a", href=True):
    print(a_href["href"])