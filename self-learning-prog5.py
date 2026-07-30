access_rights = input("Enter the employees with access rights (comma-separated): ").split(",")
current_employees = input("Enter the current employees (comma-separated): ").split(",")

access_set = set(name.strip().lower() for name in access_rights)
current_set = set(name.strip().lower() for name in current_employees)

access_set.intersection_update(current_set)

print("\nUpdated Access Rights List:")

for employee in access_set:
    print(employee.title())