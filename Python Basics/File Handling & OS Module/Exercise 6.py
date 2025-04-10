#  Write a script that creates a new text file, writes a message to it, and then reads it.

import os
import re


files = str(os.listdir("assets"))
file_name = input("Enter a file name: ")

def Create_a_file():
    file_path = open(f"assets\\{file_name}", "w+")
    user_input = input("Entr some string: ")
    file_path.write(user_input)
    file_path.seek(0)
    print(file_path.read())


if not re.search (file_name,files):
    Create_a_file()
else:
    user_input = input("The file already exists, would you like to rewrite it[Y/N]? ")
    if user_input == "Y" or user_input  == "y" :
        Create_a_file()