# Fetch and print your public IP address using an API.

import requests
req = requests.get("https://api.ipify.org")

print(f"Your ip adderss: {req.text}")