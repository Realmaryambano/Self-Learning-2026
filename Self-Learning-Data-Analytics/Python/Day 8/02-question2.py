# ------------------------------------------------------------
# QUESTION:
# Write a Python program to calculate student grades
# based on average marks.
# ------------------------------------------------------------

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        avg = sum(self.marks) / len(self.marks)
        if avg >= 80:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 40:
            return "C"
        else:
            return "Fail"


def main():
    student = Student("Ankit", [75, 82, 78])
    grade = student.calculate_grade()

    print(f"Student Name: {student.name}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()


# OUTPUT DISPLAYED:
# Student Name: Ankit
# Grade: A
