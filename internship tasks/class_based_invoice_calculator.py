# Define a class for each item in the invoice
class LineItem:
    def __init__(self, name, quantity, unit_price):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def total_price(self):
        return self.quantity * self.unit_price

# Define a class for the invoice
class Invoice:
    def __init__(self, tax_rate=0.18):  # 18% tax by default
        self.items = []
        self.tax_rate = tax_rate

    def add_item(self, item):
        self.items.append(item)

    def subtotal(self):
        total = 0
        for item in self.items:
            total += item.total_price()
        return total

    def tax_amount(self):
        return self.subtotal() * self.tax_rate

    def total(self):
        return self.subtotal() + self.tax_amount()

    def print_invoice(self):
        print("\n----- INVOICE -----")
        for item in self.items:
            print(f"{item.name}: {item.quantity} x {item.unit_price} = ₹{item.total_price()}")
        print(f"\nSubtotal: ₹{self.subtotal()}")
        print(f"Tax: ₹{self.tax_amount()}")
        print(f"Total: ₹{self.total()}")
        print("-------------------")

# ---------- USE IT BELOW ----------

invoice = Invoice()  # Create an invoice

# Add some items to the invoice
invoice.add_item(LineItem("Laptop", 1, 60000))
invoice.add_item(LineItem("Mouse", 2, 500))
invoice.add_item(LineItem("Keyboard", 1, 1500))

# Print the final invoice
invoice.print_invoice()
