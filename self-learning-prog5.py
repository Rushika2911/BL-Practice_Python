import re


# Function to check password
def check_password(password):

    # At least 8 characters
    if len(password) < 8:
        return False

    # Cannot start with digit or special character
    if not re.match(r'^[A-Za-z]', password):
        return False

    # At least one digit
    if not re.search(r'\d', password):
        return False

    # At least one special symbol
    if not re.search(r'[@#$%^&*]', password):
        return False

    # At least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # At least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    return True


# Input
password = input("Enter your password: ")

# Output
if check_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")