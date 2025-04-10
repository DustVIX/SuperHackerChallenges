# Write a function that finds the longest word in a list.

my_list = ["ls","nsso","ddddd","passwd","hi"]


def longest(a_input):
    long = 0
    for index in a_input:
        if long <= len(index):
            long = len(index)
    for index in a_input:
        if len(index) == long:
            print(f"The longest word is: {index}")

longest(my_list)