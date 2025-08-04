import tkinter as tk
from tkinter import messagebox

# ---------------- Logic Classes ---------------- #

class LineItem:
    def __init__(self, name, quantity, unit_price, category="General"):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price
        self.category = category

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

    def save_to_file(self, filename="invoice.txt"):
        with open(filename, "w") as f:
            f.write("----- INVOICE -----\n")
            for item in self.items:
                f.write(f"{item.name} ({item.category}): {item.quantity} x {item.unit_price} = ₹{item.total_price()}\n")
            f.write(f"\nSubtotal: ₹{self.subtotal():.2f}\n")
            f.write(f"Tax: ₹{self.tax_amount():.2f}\n")
            f.write(f"Total: ₹{self.total():.2f}\n")
        messagebox.showinfo("Saved", f"Invoice saved to '{filename}'")

# ---------------- GUI Application ---------------- #

class InvoiceApp:
    def __init__(self, root):
        self.invoice = Invoice()
        self.root = root
        self.root.title("Invoice Calculator")

        # Input fields
        tk.Label(root, text="Item Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(root, text="Quantity").grid(row=1, column=0)
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.grid(row=1, column=1)

        tk.Label(root, text="Unit Price").grid(row=2, column=0)
        self.price_entry = tk.Entry(root)
        self.price_entry.grid(row=2, column=1)

        tk.Label(root, text="Category").grid(row=3, column=0)
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=3, column=1)

        # Buttons
        tk.Button(root, text="Add Item", command=self.add_item).grid(row=4, column=0, columnspan=2, pady=10)
        # tk.Button(root, text="Save Invoice", command=self.save_invoice).grid(row=5, column=0, columnspan=2, pady=5)

        # Display
        self.output = tk.Text(root, height=10, width=50)
        self.output.grid(row=6, column=0, columnspan=2)

    def add_item(self):
        try:
            name = self.name_entry.get()
            quantity = int(self.quantity_entry.get())
            price = float(self.price_entry.get())
            category = self.category_entry.get() or "General"

            item = LineItem(name, quantity, price, category)
            self.invoice.add_item(item)

            self.output.insert(tk.END, f"✔ Added: {name} ({category}) - {quantity} x ₹{price}\n")
            self.display_totals()

            # Clear inputs
            self.name_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid quantity and price.")

    def display_totals(self):
        subtotal = self.invoice.subtotal()
        tax = self.invoice.tax_amount()
        total = self.invoice.total()
        self.output.insert(tk.END, f"Subtotal: ₹{subtotal:.2f}, Tax: ₹{tax:.2f}, Total: ₹{total:.2f}\n\n")

    def save_invoice(self):
        self.invoice.save_to_file()


# ---------------- Main Application Run ---------------- #

if __name__ == "__main__":
    root = tk.Tk()
    app = InvoiceApp(root)
    root.mainloop()
