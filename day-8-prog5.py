school_friends = {'John', 'Alice', 'Bob', 'David'}
college_friends = {'Alice', 'Charlie', 'David', 'Eve'}

all_friends = school_friends | college_friends

print("All friends (Set | operator):", list(all_friends))


school_friends = {'John', 'Alice', 'Bob', 'David'}
college_friends = {'Alice', 'Charlie', 'David', 'Eve'}

all_friends = school_friends.union(college_friends)

print("All friends (Set union method):", list(all_friends))



school_friends = input("Enter school friends (comma separated): ").split(",")
college_friends = input("Enter college friends (comma separated): ").split(",")

school_set = set(friend.strip() for friend in school_friends)
college_set = set(friend.strip() for friend in college_friends)

print("Using | operator:", list(school_set | college_set))
print("Using union():", list(school_set.union(college_set)))