# implement your own data structures
# create an inventory
inventory = {}

# print menu
print("Welcome to Inventory Manager!")
print("Current inventory:")
print(inventory)
# add item
def add_item(item_name, quantity, price):
    inventory[item_name] = (quantity, price)
# test add
add_item("apple", 10, 2.5)
print(inventory)
# remove item
def remove_item(item_name):
    if item_name in inventory:
        del inventory[item_name]
    else:
        print(f"{item_name} not found in inventory.")
# test remove and not found
remove_item("apple")
print(inventory)
remove_item("apple")

#update item
def update_item(item_name, new_quantity=None, new_price=None):
    if item_name in inventory:
        quantity, price = inventory[item_name]
        if new_quantity is not None:
            quantity = new_quantity
        if new_price is not None:
            price = new_price
        inventory[item_name] = (quantity, price)  # Update the tuple
    else:
        print(f"{item_name} not found in inventory.")
# test update item
add_item("apple", 10, 2.5)
print(inventory)
update_item("apple", new_quantity=5)
print(inventory)
update_item("apple", new_price=1.5)
print(inventory)
# show inventory
def print_inventory():
    print("Inventory:")
    if not inventory:
        print("Inventory is empty.")
    else:
        for item_name, (quantity, price) in inventory.items():
            print(f"Item: {item_name}, Quantity: {quantity}, Price: ${price:.2f}")
# test printing
print_inventory()

# calculate value of inventory
def calculate_value():
    total = 0
    for item_name, (quantity, price) in inventory.items():
        total += quantity * price
    print(f"Total value of inventory: $ {total:.2f}")
# test calculate total
calculate_value()

# create menu
def display_menu():
    print("Welcome to Inventory Manager!")
    print_inventory()
    print("1. Add item")
    print("2. Remove item")
    print("3. Update quantity")
    print("4. Update price")
    print("5. Calculate total value of inventory.")
    print("6. Exit")

while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter item name: ")
        quantity = int(input("Enter item quantity: "))
        price = float(input("Enter item price: "))
        add_item(name, quantity, price)
    elif choice == "2":
        name = input("Enter item name: ")
        remove_item(name)
    elif choice == "3":
        name = input("Enter item name: ")
        quantity = int(input("Enter item quantity: "))
        update_item(name, new_quantity=quantity)
    elif choice == "4":
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        update_item(name, new_price=price)
    elif choice == "5":
        calculate_value()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
