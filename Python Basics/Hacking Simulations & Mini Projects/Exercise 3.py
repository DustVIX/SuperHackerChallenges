# Build a script that scrapes all links from a webpage using BeautifulSoup.

import requests
from bs4 import BeautifulSoup

req = requests.get("https://pypi.org/project/beautifulsoup4/")
soup = BeautifulSoup(req.text, 'html.parser')

links = soup.find_all('a')
for a_href in soup.find_all("a", href=True):
    print(a_href["href"])