# 10. Check if a string is a palindrome (same forward and backward).

str_input = input("Enter a string to check if it is a palindrome: ")

re_txt = str_input[::-1]
if re_txt == str_input:
    print("It is a palindrome")
else:
    print("It is not a palindrome")