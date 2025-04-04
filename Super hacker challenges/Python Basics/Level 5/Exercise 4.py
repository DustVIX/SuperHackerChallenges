# Read a file and count how many times a given word appears.

import re


str_input = input("Enter the word you are looking for: ")

file_path = open("assets\\find_me.txt","r")
line_list = file_path.read();
count = line_list.count(str_input)
if count:
    print(f"There is {count} word in find_me.txt")
else:
    print("There is no such word in find_me.txt")

file_path.close()



# match = re.search(str_input, line_list)

# if match:
#     print(f"We find it: {match.group()}") 
# else:
#     print("Sorry, the word is not here ):")