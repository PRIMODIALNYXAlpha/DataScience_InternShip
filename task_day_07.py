# Inventory Management System

inventory = {}

def add_product():
    name = input("Enter product name: ").strip()
    if name in inventory:
        print("Product already exists!")
        return
    
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    
    inventory[name] = {
        "price": price,
        "quantity": quantity
    }
    print("Product added successfully!")

def remove_product():
    name = input("Enter product name to remove: ").strip()
    if name in inventory:
        del inventory[name]
        print("Product removed successfully!")
    else:
        print("Product not found!")

def search_product():
    name = input("Enter product name to search: ").strip()
    if name in inventory:
        product = inventory[name]
        print(f"Product Found!")
        print(f"Price: ₹{product['price']}")
        print(f"Quantity: {product['quantity']}")
    else:
        print("Product not found!")

def update_stock():
    name = input("Enter product name to update: ").strip()
    if name in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[name]["quantity"] = quantity
        print("Stock updated successfully!")
    else:
        print("Product not found!")

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    
    print("\n--- Inventory List ---")
    for name, details in inventory.items():
        print(f"Product: {name}")
        print(f"Price: ₹{details['price']}")
        print(f"Quantity: {details['quantity']}")
        print("----------------------")

def total_inventory_value():
    total = 0
    for product in inventory.values():
        total += product["price"] * product["quantity"]
    print(f"Total Inventory Value: ₹{total}")

def menu():
    while True:
        print("\n===== Inventory Management System =====")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Search Product")
        print("4. Update Stock")
        print("5. View Inventory")
        print("6. Total Inventory Value")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_product()
        elif choice == "2":
            remove_product()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_stock()
        elif choice == "5":
            view_inventory()
        elif choice == "6":
            total_inventory_value()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
