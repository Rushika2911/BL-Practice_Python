def format_full_name(first_name, middle_name, last_name):
    full_name= first_name.title()
    if middle_name !="":
        full_name+=" "+ middle_name.title()
    
    full_name+= " "+last_name.title()
    return full_name

first_name= input("enter first name: ")
middle_name= input("enter middles name: ")
last_name= input("enter last name: ")

fullname= format_full_name(first_name,middle_name, last_name)
print(f"formatted full name is : {fullname}")