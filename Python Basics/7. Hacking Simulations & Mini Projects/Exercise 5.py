# Write a script that detects if a website is up or down.

import requests

url = input("Enter a url: ").strip()
if not url.startswith("http"):
    url = "http://" + url



try:
    req = requests.head(url, timeout=5, allow_redirects=True)
    if req.status_code < 400:
        print(f"[+] {url} is ONLINE! ✅ (Status Code: {req.status_code})")
    else:
        print(f"[-] {url} might be DOWN ❌ (Status Code: {req.status_code})")
except requests.exceptions.RequestException as e:
    print(f"[-] {url} is DOWN ❌ ({type(e).__name__})")
except KeyboardInterrupt:
    print("CTRL + C: Bye Bye")