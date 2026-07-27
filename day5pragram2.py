# PROG 2: Reverse A List

# Reverse a list of numbers using slicing and also with reverse function.


# Input => numbers = [29, 45, 32, 49, 37]

# Output =>
# ```
# The Original List is [29, 45, 32, 49, 37]
# The Reversed List using slicing is [37, 49, 32, 45, 29]
# The Reversed List using reverse() method is [37, 49, 32, 45, 29]
# ```


# PROG 2.1: By Using Slicing

# Write The Code

n= int(input())
original_list=[]
for i in range(n):
    num= int(input())
    original_list.append(num)

print(f"the original list is {original_list}")
reverse_list= original_list[::-1]
print(reverse_list)



# PROG 2.2: By Using reverse() method
def reverse_list(original_list):
    original_list.reverse()
    return original_list
n= int(input())
original_list=[]
for i in range(n):
    num= int(input())
    original_list.append(num)

print(f"the original list is {original_list}")
reverse_order= reverse_list(original_list)
print(f"reversed list is {reverse_order}")