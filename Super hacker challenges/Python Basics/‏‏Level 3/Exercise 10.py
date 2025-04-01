# Given a dictionary of usernames and passwords, write a script that asks for a username and prints the stored password.

dictionary = [{"username":"DustVIX","passwd":"p@sswd"},{"username":"Ahmed","passwd":"re_ahmed"},{"username":"admin","passwd":"admin"}]
num = 0

str_username = input("Enter your username: ")

for i in dictionary:
    num = 1 + num
    if i["username"] == str_username:
        print(f"Welcome {str_username}, your password is {i["passwd"]}")
    elif num == 3:
        print(f"Sorry, {str_username} not found")