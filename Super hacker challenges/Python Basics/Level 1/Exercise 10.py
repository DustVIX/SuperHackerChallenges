password = "ahmed"
vowels = ["a","A","i","I","e","E","o","O","u","U"]

for v in vowels:
    password = password.replace(v, "*")
print(password)