current_members = input("Enter the names of current members (comma-separated): ").split(",")
renewed_members = input("Enter the names of renewed members (comma-separated): ").split(",")

current_set = set(name.strip().lower() for name in current_members)
renewed_set = set(name.strip().lower() for name in renewed_members)

current_set.symmetric_difference_update(renewed_set)

print("\nUpdated club members list:")

for member in current_set:
    print(member.title())