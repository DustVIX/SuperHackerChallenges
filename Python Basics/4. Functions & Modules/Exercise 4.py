# Use the hashlib module to create an MD5 hash of a user-entered string.

import hashlib

text = input("Enter a text: ")
m = hashlib.md5(text.encode())
print(m.hexdigest())