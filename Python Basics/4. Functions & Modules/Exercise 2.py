# Create a function that checks if a password is strong (at least 8 characters, includes a number, and a special character).

import re

passwd = input("Enter the password: ")
rate_of_passed = ["Weak","Medium","Strong","Very Strong"]
counter = 0

def Verification(check):
    global counter
    if len(check) > 8:
        print("The password is more the 8 characters:✅")
        counter += 1
    if re.search("[@#$.%^&*]",check):
        print("There is a special character:✅")
        counter += 1
    if re.search("[1-9]",check):
        print("It includes a number:✅")
        counter += 1
    print(f"Your password is {rate_of_passed[counter]}")

Verification(passwd)