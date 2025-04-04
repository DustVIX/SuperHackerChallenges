# Create a script that logs user input to a file (keystroke.log).

user_input = input("Entr some string: ")

file_path = open("assets\\keystroke.log", "a")
file_path.write(user_input)

file_path.close()