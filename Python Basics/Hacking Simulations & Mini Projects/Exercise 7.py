# Simulate a basic phishing email generator.

import random

names = ["User", "Customer", "Client"]
subjects = ["Account Alert", "Urgent Notice", "Login Required"]
senders = ["support@bank.com", "admin@paypal.com", "security@netflix.com"]
links = ["http://verify-login.com", "http://secure-check.net", "http://reset-now.org"]

message = f"""
From: {random.choice(senders)}
Subject: {random.choice(subjects)}

Dear {random.choice(names)},

We noticed suspicious activity in your account. Please verify your login details immediately to avoid suspension.

Click here: {random.choice(links)}

Best regards,
Bank Security Team
"""



print(message)