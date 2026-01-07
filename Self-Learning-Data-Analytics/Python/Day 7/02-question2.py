# Program 2: Banking Transaction System
# Question: Create a banking system to deposit, withdraw, and check balance.

def create_account(balance):
    return balance

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        return balance
    return balance - amount

def check_balance(balance):
    return balance

def bank_process(balance, action, amount=0):
    if action == "deposit":
        return deposit(balance, amount)
    elif action == "withdraw":
        return withdraw(balance, amount)
    return check_balance(balance)

# Main Program
balance = create_account(10000)
balance = bank_process(balance, "deposit", 5000)
balance = bank_process(balance, "withdraw", 3000)
print("Final Balance:", balance)

# Output:
# Final Balance: 12000
