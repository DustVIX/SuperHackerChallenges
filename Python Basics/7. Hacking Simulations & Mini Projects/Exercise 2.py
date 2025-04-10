# Simulate a Caesar cipher encryption/decryption tool.

import string

letters = string.ascii_letters + string.digits 

def encryption():
    encrypted = []
    text = input("Enter an unencrypted text: ")
    key =  int(input("Enter the key (1-25): "))
    for i in range(len(text)):
        for j in range(len(letters)):
            if text[i] == letters[j]:
                encrypted.append(letters[(j + key) % len(letters)])
    return "".join(encrypted)

def decryption():
    decrypted = []
    ciphertext = input("Enter an encrypted text: ")
    key =  int(input("Enter the key (1-25): "))
    for i in range(len(ciphertext)):
        for j in range(len(letters)):
            if ciphertext[i] == letters[j]:
                decrypted.append(letters[(j - key) % len(letters)])
    return "".join(decrypted)

try:
    while True:
        mod = input("Enter the mod[encryption/decryption]: ").lower()
        if mod == "encryption":
            print(encryption())
        elif mod == "decryption":
            print(decryption())
        else:
            print("Sorry just type encryption or decryption")
except KeyboardInterrupt:
    print("\nCTRL + C: Bye Bye")