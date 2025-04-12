# Simulate a login attempt system that locks after 3 failed attempts.

from getpass import getpass

password = ""
attempts = 3
while attempts:
    input_password = getpass()
    if input_password != password:
        print("Incorrect password, please try again.")
        attempts = attempts - 1
    else:
        print("Hello Hacker")
        break 