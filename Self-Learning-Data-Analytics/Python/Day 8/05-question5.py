# ------------------------------------------------------------
# QUESTION:
# Write a Python program to manage employee attendance.
# The program should:
# 1. Store employee details.
# 2. Mark attendance (Present/Absent).
# 3. Display attendance report.
# ------------------------------------------------------------

class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name
        self.attendance = None


class AttendanceManager:
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee):
        self.employees[employee.emp_id] = employee

    def mark_attendance(self, emp_id, status):
        if emp_id not in self.employees:
            raise KeyError("Employee not found")
        self.employees[emp_id].attendance = status

    def display_report(self):
        print("\n--- Attendance Report ---")
        for emp in self.employees.values():
            print(f"ID: {emp.emp_id}, Name: {emp.name}, Status: {emp.attendance}")


def main():
    manager = AttendanceManager()

    manager.add_employee(Employee(1, "Alice"))
    manager.add_employee(Employee(2, "Bob"))

    manager.mark_attendance(1, "Present")
    manager.mark_attendance(2, "Absent")

    manager.display_report()


if __name__ == "__main__":
    main()


# OUTPUT DISPLAYED:
# --- Attendance Report ---
# ID: 1, Name: Alice, Status: Present
# ID: 2, Name: Bob, Status: Absent
