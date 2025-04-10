# Create a function that generates random MAC addresses.

import random
import string

def mac_generatre():
    letters = string.ascii_letters + string.digits
    temp2 = ""
    for _ in range(12):
        temp = "".join(random.choices(letters, k=2))
        temp2 += temp + ":"
    
    print(temp2[:-1])

mac_generatre()