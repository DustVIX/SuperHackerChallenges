# Write a script that generates fake credit card numbers for testing.

import random
import string

names = [
    "James", "Emily", "Michael", "Olivia", "John",
    "Sophia", "David", "Isabella", "Robert", "Mia",
    "Daniel", "Charlotte", "William", "Amelia", "Joseph",
    "Ava", "Thomas", "Grace", "Andrew", "Lily"
];
number = string.digits

name_card = " ".join(random.choices(names,k=2))
card_number = []
CVV = "".join(random.choices(number,k=3))

for i in range(0,4):
    card_number.append("".join(random.choices(number,k=4)))


while True:
    expiry_year = int("".join(random.choices(number,k=2)))
    if expiry_year > 24 and expiry_year < 40:
        break

while True:
    expiry_month = int("".join(random.choices(number,k=2)))
    if expiry_month < 13 and expiry_month != 0:
        break


print(f"Name: {name_card}")
print(f"Card Number: {" ".join(card_number)}")
print(f"Expiration Date: {expiry_month}/{expiry_year}")
print(f"CVV: {CVV}")