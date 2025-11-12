# 6. Simple Inventory System
# ● Use: Dictionary (item: quantity), functions, loops
# ● Features:
# ○ Add new item or update quantity
# ○ Remove item
# ○ Show inventory list

def add_item(inventory, item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    else:
        print(f"{item} not found in inventory.")

def show_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Inventory List:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")

def main():
    inventory = {}
    while True:
        print("\n1. Add/Update Item")
        print("2. Remove Item")
        print("3. Show Inventory")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            item = input("Enter item name: ")
            try:
                quantity = int(input("Enter quantity: "))
                add_item(inventory, item, quantity)
            except ValueError:
                print("Invalid quantity.")
        elif choice == '2':
            item = input("Enter item name to remove: ")
            remove_item(inventory, item)
        elif choice == '3':
            show_inventory(inventory)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

