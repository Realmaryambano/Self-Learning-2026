# ------------------------------------------------------------
# QUESTION:
# Write a Python program to track online order delivery status.
# The program should update and display order status.
# ------------------------------------------------------------

class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.status = "Order Placed"

    def update_status(self, new_status):
        self.status = new_status

    def display(self):
        print(f"Order ID: {self.order_id}")
        print(f"Customer: {self.customer}")
        print(f"Status: {self.status}")


def main():
    order = Order(5001, "Neha")
    order.update_status("Out for Delivery")
    order.display()


if __name__ == "__main__":
    main()


# OUTPUT DISPLAYED:
# Order ID: 5001
# Customer: Neha
# Status: Out for Delivery
