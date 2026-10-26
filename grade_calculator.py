
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def main():
    print("=" * 40)
    print("   STUDENT MARKS & GRADE CALCULATOR")
    print("=" * 40)

    name = input("Enter student name: ").strip()

    if not name:
        print("Error: Student name cannot be empty.")
        return

    subjects = ["English", "Mathematics", "Computer Science",
                "Artificial Intelligence", "Environmental Studies"]

    marks = []

    for subject in subjects:
        while True:
            try:
                score = float(input(f"Enter marks in {subject} (0-100): "))

                if 0 <= score <= 100:
                    marks.append(score)
                    break
                else:
                    print("Please enter marks between 0 and 100.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    total = sum(marks)
    maximum = len(subjects) * 100
    percentage = (total / maximum) * 100
    grade = calculate_grade(percentage)

    # Student must score at least 40 in every subject to pass.
    passed = all(score >= 40 for score in marks)

    print("\n" + "=" * 40)
    print("           STUDENT REPORT")
    print("=" * 40)
    print(f"Student Name : {name}")
    print("-" * 40)

    for subject, score in zip(subjects, marks):
        print(f"{subject:<28} {score:>6.1f}/100")

    print("-" * 40)
    print(f"Total Marks  : {total:.1f}/{maximum}")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Grade        : {grade}")
    print(f"Result       : {'PASS' if passed else 'FAIL'}")
    print("=" * 40)


if __name__ == "__main__":
    main()
