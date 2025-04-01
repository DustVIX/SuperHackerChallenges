# Write a program that checks if a number is even or odd.

num1 = int(input("Enter a number: "))
num2 = num1 % 2

if num2 == 1:
    print("odd")
else:
    print("even")