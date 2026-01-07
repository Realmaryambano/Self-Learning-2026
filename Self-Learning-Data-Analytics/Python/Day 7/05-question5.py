# Program 5: Student Performance Analysis
# Question: Analyze student marks and determine grade.

def calculate_total(marks):
    return sum(marks)

def calculate_average(total, subjects):
    return total / subjects

def assign_grade(avg):
    if avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    return "Fail"

def generate_report(name, grade):
    return f"Student: {name}, Grade: {grade}"

def student_result(name, marks):
    total = calculate_total(marks)
    avg = calculate_average(total, len(marks))
    grade = assign_grade(avg)
    return generate_report(name, grade)

# Main Program
report = student_result("Kiran", [78, 65, 72, 80, 60])
print(report)

# Output:
# Student: Kiran, Grade: B
