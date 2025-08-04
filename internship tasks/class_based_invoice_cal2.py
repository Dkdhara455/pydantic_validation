class LineItem:
    def __init__(self, name, quantity, unit_price):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def total_price(self):
        return self.quantity * self.unit_price


class Invoice:
    def __init__(self, tax_rate=0.18):
        self.items = []
        self.tax_rate = tax_rate

    def add_item(self, item):
        self.items.append(item)

    def subtotal(self):
        return sum(item.total_price() for item in self.items)

    def tax_amount(self):
        return self.subtotal() * self.tax_rate

    def total(self):
        return self.subtotal() + self.tax_amount()

    def print_invoice(self):
        print("\n----- INVOICE -----")
        for item in self.items:
            print(f"{item.name}: {item.quantity} x {item.unit_price} = ₹{item.total_price()}")
        print(f"\nSubtotal: ₹{self.subtotal():.2f}")
        print(f"Tax: ₹{self.tax_amount():.2f}")
        print(f"Total: ₹{self.total():.2f}")
        print("-------------------")


# ---------- USER INPUT PART ----------

invoice = Invoice()

while True:
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    unit_price = float(input("Enter unit price: "))

    invoice.add_item(LineItem(name, quantity, unit_price))

    more = input("Do you want to add another item? (yes/no): ").strip().lower()
    if more != "yes":
        break

invoice.print_invoice()
