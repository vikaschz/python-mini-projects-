"""3. Shopping List with Categories
● Use: Dictionary (category: list of items), functions, loops
● Features:
○ Add item to category
○ Show items by category
○ Remove item
○ Show full shopping list
"""

shopping_list = {}


def add_item(category, size):
    items = []
    for i in range(size):
        item = input(f"Enter item {i+1}: ")
        items.append(item)

    if category in shopping_list:
        shopping_list[category].extend(items)
        print('Item added successfully.')
    else:
        shopping_list[category] = items


def show_category(category):
    if category in shopping_list:
        print(f"Category: {category}")
        print(f"Items: {shopping_list[category]}")
    else:
        print("Not found")


def remove_item(category, item):
    if category in shopping_list:
        if item in shopping_list[category]:
            shopping_list[category].remove(item)
            print(f"{item} removed from {category} ✅")
            if not shopping_list[category]:  # if empty, remove category
                del shopping_list[category]
        else:
            print(f"{item} not found in {category} ❌")
    else:
        print("Category not found ❌")


def Show_full_shopping_list():
    if not shopping_list:
        print("Shopping list is empty ❌")
    else:
        print("\n---- Shopping List ----")
        for category, items in shopping_list.items():
            print(f"{category}: {', '.join(items)}")

while True:
    print(
        """\n1. Add item
2. Show items by category
3. Remove item
4. Show full shopping list
5. Exit
"""
    )

    choice = input("Enter choice: ")

    match choice:
        case "1":
            name_of_category = input("Enter the name of category: ").lower()
            size_of_item = int(input("Enter the size of items: "))
            add_item(name_of_category, size_of_item)

        case "2":
            name_of_category = input("Enter the name of category to show: ").lower()
            show_category(name_of_category)

        case "3":
            name_of_category = input("Enter the name of category: ").lower()
            name_of_item = input("Enter the name of item: ").lower()
            remove_item(name_of_category, name_of_item)
        case "4":
            Show_full_shopping_list()
        case "5":
            print("Exiting...")
            break
        case _:
            print("Invalid choice, try again.")
