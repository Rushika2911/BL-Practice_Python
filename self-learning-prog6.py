import random

TOTAL_SUBJECT_MARKS = 50

students = [
    "Olivia", "Liam", "Emma", "Noah", "Sophia",
    "James", "Ava", "William", "Mia", "Benjamin"
]
subjects = ["Physics", "Chemistry", "Mathematics"]

for student in students:
    marks = []
    for i in range(3):
        marks.append(random.randint(0, TOTAL_SUBJECT_MARKS))

    total_obtained = sum(marks)
    total_marks = TOTAL_SUBJECT_MARKS * len(subjects)
    overall_percentage = (total_obtained / total_marks) * 100

    print("\nNew School Of Learning - Class XI -", student)
    print("-" * 71)
    print(f"{'Subject':15}{'Total Marks':>15}{'Marks Obtained':>18}{'Percentage':>15}")
    print("-" * 71)

    for i in range(len(subjects)):
        percentage = (marks[i] / TOTAL_SUBJECT_MARKS) * 100
        print(f"{subjects[i]:15}{TOTAL_SUBJECT_MARKS:>15}{marks[i]:>18}{percentage:>15.2f}")

    print("-" * 71)
    print(f"{'Total':15}{total_marks:>15}{total_obtained:>18}{overall_percentage:>15.2f}")
    print("-" * 71)