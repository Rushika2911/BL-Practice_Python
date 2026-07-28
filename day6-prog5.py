import re


def is_valid_email(mail):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern,mail):
        return True
    else:
        return False
    


mail= input("enter email address: ")
if is_valid_email(mail):
    print("its valid email address")
else:
    print("its invalid email address")