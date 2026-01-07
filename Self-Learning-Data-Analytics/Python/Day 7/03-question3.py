# Program 3: E-commerce Order Processing
# Question: Process customer orders and calculate final bill with discount.

def calculate_total(price, quantity):
    return price * quantity

def apply_discount(total):
    return total * 0.9 if total > 5000 else total

def add_tax(amount):
    return amount * 1.18

def generate_invoice(customer, amount):
    return f"Customer: {customer}, Final Bill: {amount}"

def order_process(customer, price, quantity):
    total = calculate_total(price, quantity)
    discounted = apply_discount(total)
    final = add_tax(discounted)
    return generate_invoice(customer, final)

# Main Program
bill = order_process("Anita", 2000, 3)
print(bill)

# Output:
# Customer: Anita, Final Bill: 6372.0
