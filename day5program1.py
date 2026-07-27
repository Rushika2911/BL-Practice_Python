# PROG 1: Sum A List

# Write a custom function (custom_sum()) which takes a list of numbers as an input argument and returns the sum of all elements of the list
# Check the answer received with the inbuilt function sum function.
# Print True or False

# Input => numbers = [29, 45, 32, 49, 37]

# Output =>

# ```
# The Original List is [29, 45, 32, 49, 37]
# The Sum of the list using Custom function is 192
# The Sum of the list using Builtin function is 192
# Comparing the results of Custom function and Builtin function: True
# ```
# PROG1-SumAList-Part1


# PROG 1.1: By Using Hard-Coded List
def custom_sum(original_list):
    total =0
    for n in original_list:
        total+=n
    
    return total

original_list =[29,45,32,49,37]
print(f"The original list is {original_list}")

custom_result= custom_sum(original_list)
built_in_result= sum(original_list)
print(f"the sum of list using custom function is {custom_result}")
print(f"the sum of list using builtin function is {built_in_result}")
print(f"comparing the result of custom and builtin function: {custom_result== built_in_result}")


# PROG 1.2: Taking List From The User

def custom_sum(original_list):
    total =0
    for n in original_list:
        total+=n
    
    return total

n = int(input("Enter the number of elements in the list: "))
original_list=[]
for i in range(n):
    num= int(input("enter a number: "))
    original_list.append(num)

print(f"The original list is {original_list}")

custom_result= custom_sum(original_list)
built_in_result= sum(original_list)
print(f"the sum of list using custom function is {custom_result}")
print(f"the sum of list using builtin function is {built_in_result}")
print(f"comparing the result of custom and builtin function: {custom_result== built_in_result}")
# Write The Code Here