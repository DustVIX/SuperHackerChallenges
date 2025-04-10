# Write a script that reads a file and prints its contents.

file_path = open("assets\\hi.txt", "r") # Double back slash to tell the interpreter the path
line_list = file_path.readlines();
for line in line_list:
    print(line)
file_path.close()

# Note: if you are in windows use \ special character not / special character
# and if you are in linux you can use / special character normally