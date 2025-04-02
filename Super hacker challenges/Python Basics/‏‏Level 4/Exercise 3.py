# Write a function that generates a random password of 12 characters.

import random
import string

def get_random_string(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)

get_random_string(12)