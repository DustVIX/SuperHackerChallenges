# Write a script that checks if a website is online or down.

import requests

url = input("Enter a url: ")
try:
    req = requests.get(url)
    if req.status_code < 400:
        print(f"[+] {url} is ONLINE! ✅ (Status Code: {req.status_code})")
    else:
        print(f"[-] {url} might be DOWN ❌ (Status Code: {req.status_code})")
except requests.exceptions.RequestException as e:
    print(f"[-] {url} is DOWN ❌ ({type(e).__name__})")