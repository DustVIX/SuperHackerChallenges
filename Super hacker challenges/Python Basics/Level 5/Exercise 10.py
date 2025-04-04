# Scan a directory for files containing a specific keyword.

import os
import re

user_input= input("Enter a word: ")
find = False
path_find = []

for filename in os.listdir("assets"):
    file_path = open(f"assets\\{filename}","r")
    word = re.search(user_input, file_path.read())
    if word:
        find = True
        path_find.append(file_path.name)        
if find:
    print(f"The word {user_input} is find in: \n")
    print("\n".join(path_find))
else:
    print(f"Sorry we couldn't find the word '{user_input}'")