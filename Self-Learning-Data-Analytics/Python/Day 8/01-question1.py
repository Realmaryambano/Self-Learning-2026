# ------------------------------------------------------------
# QUESTION:
# Write a Python program to manage a company's product sales.
# The program should:
# 1. Store product details (ID, name, price).
# 2. Record sales transactions.
# 3. Calculate total revenue.
# 4. Display a sales summary.
# This program should follow industry-level coding practices.
# ------------------------------------------------------------


class Product:
    def __init__(self, product_id, name, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.product_id = product_id
        self.name = name
        self.price = price


class SalesManager:
    def __init__(self):
        self.products = {}
        self.sales = []

    def add_product(self, product):
        self.products[product.product_id] = product

    def record_sale(self, product_id, quantity):
        if product_id not in self.products:
            raise KeyError("Product not found")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        product = self.products[product_id]
        total_price = product.price * quantity
        self.sales.append((product.name, quantity, total_price))

    def calculate_total_revenue(self):
        return sum(sale[2] for sale in self.sales)

    def display_sales_summary(self):
        print("\n--- Sales Summary ---")
        for name, quantity, total in self.sales:
            print(f"Product: {name}, Quantity Sold: {quantity}, Revenue: ${total:.2f}")
        print(f"\nTotal Revenue: ${self.calculate_total_revenue():.2f}")


def main():
    manager = SalesManager()

    # Adding products
    manager.add_product(Product(101, "Laptop", 75000))
    manager.add_product(Product(102, "Mouse", 500))
    manager.add_product(Product(103, "Keyboard", 1200))

    # Recording sales
    manager.record_sale(101, 2)
    manager.record_sale(102, 5)
    manager.record_sale(103, 3)

    # Display summary
    manager.display_sales_summary()


if __name__ == "__main__":
    main()

