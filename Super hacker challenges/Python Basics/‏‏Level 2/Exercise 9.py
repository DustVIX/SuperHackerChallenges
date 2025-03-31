#  Use a while loop to continuously ask for a password until the correct one is entered.
from getpass import getpass

passwd = "p@ssw0red"

while True:
    user_passwd = getpass()
    if passwd == user_passwd:
        print("your passwoed is correct")
        break
    else:
        print("Incorrect password, please try again.")