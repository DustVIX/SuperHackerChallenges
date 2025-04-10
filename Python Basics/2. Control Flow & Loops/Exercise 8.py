# Print numbers 1-100, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", and both with "FizzBuzz".

index = 1
while index <= 100:
    if not index%3 and not index%5:
        print("FizzBuzz")
    elif not index%3:
        print("Fizz")
    elif not index%5:
        print("Buzz")
    else: 
        print(index)

    index += 1