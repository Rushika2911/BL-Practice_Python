current_subscribers = input("Enter the current subscribers' emails (comma-separated): ").split(",")
new_signups = input("Enter the new sign-ups' emails (comma-separated): ").split(",")

current_set = set(email.strip().lower() for email in current_subscribers)
new_set = set(email.strip().lower() for email in new_signups)

if current_set.isdisjoint(new_set):
    print("\nThere are no common email addresses between current subscribers and new sign-ups.")
else:
    common_emails = current_set.intersection(new_set)
    print("\nThe following email addresses are present in both lists:")
    for email in common_emails:
        print(email)