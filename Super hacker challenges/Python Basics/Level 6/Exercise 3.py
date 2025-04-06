# Write a script that sends an HTTP request to example.com and prints the response headers.

import requests

user_input = input("Enter a url: ")

req = requests.get(user_input)

for header in req.headers:
    print(header)