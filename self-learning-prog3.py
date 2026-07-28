import re


def remove_digits(text):
    return re.sub(r'\d', '', text)

input_string = input("Input String: ")

output_string = remove_digits(input_string)
print("Output String without numbers:", output_string)