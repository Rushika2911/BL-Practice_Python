# school_friends = ['John', 'Alice', 'Bob', 'David']
# college_friends = ['Alice', 'Charlie', 'David', 'Eve']

# common_friends = []

# for friend in school_friends:
#     if friend in college_friends:
#         common_friends.append(friend)

# print("Common friends (Iterative method):", common_friends)

# school_friends = {'John', 'Alice', 'Bob', 'David'}
# college_friends = {'Alice', 'Charlie', 'David', 'Eve'}

# common_friends = school_friends & college_friends

# print("Common friends (Set & operator):", list(common_friends))

school_friends = {'John', 'Alice', 'Bob', 'David'}
college_friends = {'Alice', 'Charlie', 'David', 'Eve'}

common_friends = school_friends.intersection(college_friends)

print("Common friends (Set intersection method):", list(common_friends))