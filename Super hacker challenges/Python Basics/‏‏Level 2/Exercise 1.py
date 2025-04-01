# Write a script that asks for a password and only allows access if it matches "s3cr3t".
password = "s3cr3t"

user_pass = input("Enter your password: ")
if user_pass == password:
    print("Welcome back")
else:
    print("Error, Please try again.")