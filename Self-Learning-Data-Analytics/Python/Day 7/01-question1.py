# Program 1: Employee Payroll System
# Question: Design a payroll system that calculates gross salary, tax, and net salary for employees.

def calculate_gross(basic, hra, allowance):
    return basic + hra + allowance

def calculate_tax(gross):
    return gross * 0.15

def calculate_net(gross, tax):
    return gross - tax

def generate_payslip(name, net):
    return f"Employee: {name}, Net Salary: {net}"

def payroll_process(name, basic, hra, allowance):
    gross = calculate_gross(basic, hra, allowance)
    tax = calculate_tax(gross)
    net = calculate_net(gross, tax)
    return generate_payslip(name, net)

# Main Program
result = payroll_process("Rahul", 30000, 8000, 5000)
print(result)

# Output:
# Employee: Rahul, Net Salary: 36550.0
