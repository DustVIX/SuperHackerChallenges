# Check if a given year is a leap year.


# my code
year = int(input("Enter the year: "))
leap_year = False

if not year%4:
    leap_year = True 
    if not year%100:
        leap_year = False
        if not year%400:
            leap_year = True 
    
    
if leap_year:
    print(f"The {year} is a leap year")
else:
    print(f"The {year} is not a leap year")


# Ai code

# year = int(input("Enter the year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"The {year} is a leap year")
# else:
#     print(f"The {year} is not a leap year")
