# PROG 4: To Remove Elements From The List

# Removing Elements at particular position/index:
# Given a list colors, plan removing 0th, 2nd and 5th element from the list.

# colors = [“Red”,”Green”, “Pink”, “Blue”, “Black”, ”Purple”, “Yellow”, “Magenta”, “Brown”]

# revised_colors = [“Green”, “Blue”, ”Purple”, “Yellow”, “Magenta”, “Brown”]

# Input =>
# Colors List : ['Red', 'Green', 'Pink', 'Blue', 'Black', 'Purple', 'Yellow', 'Magenta', 'Brown']

# Output =>
# ```
# Colors List : ['Red', 'Green', 'Pink', 'Blue', 'Black', 'Purple', 'Yellow', 'Magenta', 'Brown']

# List After Removing Particular Elements : ['Green', 'Blue', 'Black', 'Yellow', 'Magenta', 'Brown']

# ```


# PROG 4: To Remove Elements From The List
colors =['red','green','pink','blue','purple','yellow','magenta','brown']
index_to_remove=[0,2,5]
result=[]
for index, num in enumerate(colors):
    if index not in index_to_remove:
        result.append(num)

print(f"list after removing: {result}")

# Write The Code Here