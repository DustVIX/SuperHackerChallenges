# Write a function that extracts all vowels “aeiouAEIOU” from a string.

import re

str_input = input("Enter a string that contains a vowel: ")

def Vowel_Extractor(string):
    no_vowel = []
    for index in string:
        if not re.search("[aeiouAEIOU]",index):
            no_vowel.append(index)
    print(f"Your string without vowels is {''.join(no_vowel)}")
Vowel_Extractor(str_input)