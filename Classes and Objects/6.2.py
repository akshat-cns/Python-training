class Inventory:

    def __init__(self):
        self.stock = {}

    def add_item(self, item_name, quantity):
        if quantity <= 0:
            print("Quantity must be positive.")
        
        if item_name in self.stock:
            self.stock[item_name] += quantity
        else:
            self.stock[item_name] = quantity
        
        print(f"Added {quantity} of {item_name}")

    def remove_item(self, item_name, quantity):
        if quantity <= 0:
            print("Quantity must be positive.")
        
        if item_name not in self.stock:
            raise KeyError(f"Item '{item_name}' not found")
        
        if self.stock[item_name] < quantity:
            print(f"Insufficient stock")
        
        self.stock[item_name] -= quantity
        print(f"Removed {quantity} of {item_name}")

        if self.stock[item_name] == 0:
            del self.stock[item_name]

    def query_item(self, item_name):
        if item_name in self.stock:
            print(f"{item_name}: {self.stock[item_name]} in stock.")
            return self.stock[item_name]
        else:
            print(f"{item_name} is not in stock.")
            return 0

    def display_inventory(self):
        if not self.stock:
            print("Inventory is empty.")
        else:
            print("\nCurrent Inventory:")
            for item, quantity in self.stock.items():
                print(f"{item}: {quantity}")
