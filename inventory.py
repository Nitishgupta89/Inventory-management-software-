import pandas as pd
import warnings
warnings.filterwarnings("ignore")

class IMS:
    def __init__(self):
        self.data = pd.DataFrame(columns=["ID", "Product_name", "seller", "customer", "Address", "status", "Quantity"])
    
    def add(self, ID, Product_name, seller, customer, Address, status, Quantity):
        new_product = {
            "ID": ID,
            "Product_name": Product_name,
            "seller": seller,
            "customer": customer,
            "Address": Address,
            "status": status,
            "Quantity": Quantity
        }
        self.data = self.data.append(new_product, ignore_index=True)
        return f"Product '{Product_name}' added successfully."

    def edit(self, ID, Product_name=None, seller=None, customer=None, Address=None, status=None, Quantity=None):
        index = self.data[self.data["ID"] == ID].index
        if not index.empty:
            if Product_name is not None:
                self.data.at[index[0], "Product_name"] = Product_name
            if seller is not None:
                self.data.at[index[0], "seller"] = seller
            if customer is not None:
                self.data.at[index[0], "customer"] = customer
            if Address is not None:
                self.data.at[index[0], "Address"] = Address
            if status is not None:
                self.data.at[index[0], "status"] = status
            if Quantity is not None:
                self.data.at[index[0], "Quantity"] = Quantity 
            return f"Product with ID {ID} updated."
        else:
            return "Product not found."
    
    def delete(self, ID):
        index = self.data[self.data["ID"] == ID].index
        if not index.empty:
            self.data = self.data.drop(index)
            return f"Product with ID {ID} deleted."
        else:
            return "Product not found."
    
    def track(self):
        print("Current Inventory:")
        print(self.data)

    def generate_report(self):
        low_stock = self.data[self.data["Quantity"] < 5]
        if not low_stock.empty:
            print("Low Stock Products:")
            print(low_stock)
        else:
            print("No low stock products.")

    def show_data(self):
        if self.data.empty:
            print("No products in inventory.")
        else:
            print(self.data)

# Testing the IMS system
ims = IMS()

# Adding products
print(ims.add(1, "Product A", "seller A", "customer A", "Address A", "In stock", 10))
print(ims.add(2, "Product B", "seller B", "customer B", "Address B", "In stock", 3))
print(ims.add(3, "Product C", "seller C", "customer C", "Address C", "Out of stock", 0))

# Viewing the current inventory
ims.track()

# Edit product with ID 2 (change quantity and status)
print(ims.edit(2, Quantity=1, status="Out of stock"))

# Delete product with ID 1
print(ims.delete(1))

# Viewing the updated inventory
ims.track()

# Generate low-stock report
ims.generate_report()

# Show full data (this will print the entire DataFrame)
ims.show_data()
