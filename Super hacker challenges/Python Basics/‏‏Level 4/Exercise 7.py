# Build a function that performs a simple XOR encryption on text.

def xor_encrypt(text, key):
    encrypted_text = ""
    
    for char in text:
        encrypted_char = chr(ord(char) ^ key)
        encrypted_text += encrypted_char 
    
    return encrypted_text

text = "Hello World"
key = 123  
encrypted = xor_encrypt(text, key)
print("Encrypted:", encrypted)