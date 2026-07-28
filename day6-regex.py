import re

# sentence="i scream , you scream , we all scream"
# print(re.search("scream", sentence))

# print(re.search("scream", sentence).group())

# print(re.findall("scream", sentence))

# print(re.split("scream", sentence))


text1="i have 2 apples and 10 oranges"
matches= re.findall(r'\d', text1)           #splits 10 also in 1,0 as it checks frm 0-9 only 
print(matches)