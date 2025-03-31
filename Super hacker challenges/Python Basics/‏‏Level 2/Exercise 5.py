# Find prime numbers between 1 and 100.

index = 1
while index <= 100:
    if (index%2 and index%3 and index%5 and index%7):
        print(index)
    
    index += 1