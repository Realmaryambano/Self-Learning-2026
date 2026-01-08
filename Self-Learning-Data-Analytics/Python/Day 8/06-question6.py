# ------------------------------------------------------------
# QUESTION:
# Write a Python program to manage inventory stock.
# The system should alert when stock is low.
# ------------------------------------------------------------

class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def check_stock(self):
        if self.quantity < 10:
            return "Low Stock Alert"
        return "Stock Sufficient"


def main():
    item = InventoryItem("Printer Ink", 6)

    print(f"Item: {item.name}")
    print(f"Quantity: {item.quantity}")
    print(item.check_stock())


if __name__ == "__main__":
    main()


# OUTPUT DISPLAYED:
# Item: Printer Ink
# Quantity: 6
# Low Stock Alert
