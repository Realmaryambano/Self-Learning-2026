# Program 4: Inventory Management System
# Question: Manage product stock in a warehouse.

def add_stock(stock, qty):
    return stock + qty

def remove_stock(stock, qty):
    return stock - qty if qty <= stock else stock

def check_stock(stock):
    return stock

def reorder_required(stock):
    return stock < 20

def inventory_process(stock, action, qty=0):
    if action == "add":
        return add_stock(stock, qty)
    elif action == "remove":
        return remove_stock(stock, qty)
    return check_stock(stock)

# Main Program
stock = 50
stock = inventory_process(stock, "remove", 40)
print("Current Stock:", stock)
print("Reorder Needed:", reorder_required(stock))

# Output:
# Current Stock: 10
# Reorder Needed: True
