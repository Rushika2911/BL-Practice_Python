import re


def search_digits(input_str):
    pattern = r'\d'
    digits= re.findall(pattern, input_str)

    return digits


input_str= input("enter the string: ")

digits_found= search_digits(input_str)
if digits_found:
    print(f"digits found in string: {digits_found}")
else:
    print("no digit is found")