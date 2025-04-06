# Create a program that sends fake HTTP headers to mimic different browsers.

import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

user_input = input("Enter a url to fake a http header to mimic different browsers: ")
req = requests.get(user_input, headers=headers)

# Note: if u want to intercept the request in burp, u must set verify=False at requests.get() and proxies=proxies
# proxies = { 
#               "http"  : "http://127.0.0.1:8080", 
#               "https" : "http://127.0.0.1:8080"
# }