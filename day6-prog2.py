def create_new_string(input_string):
    first_char= input_string[0]
    middle_idx= len(input_string)//2
    middle_char= input_string[middle_idx]
    last_char= input_string[-1]
    new_str= first_char+middle_char+last_char
    return new_str

input_string= 'Knowledge'
result= create_new_string(input_string)
print(f"new string is: {result}")