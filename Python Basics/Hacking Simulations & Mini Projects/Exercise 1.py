# Generate 10 fake email addresses.

import random
import string

for i in range(0,10):
    letters = string.ascii_letters + string.digits 
    result_str = ''.join(random.choice(letters) for i in range(7))
    print(result_str + "@gmail.com")