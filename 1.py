# Use: Dictionary (store contacts), functions (add, search, delete), loops (menu)
# ○ Add contact (name, phone)
# ○ Search contact by name
# ○ Delete contact
# ○ Show all contact
contacts = {}


def add_contact(name, phone):
    contacts[name] = phone
    print(f"{name} added to contact list successfully ✅.")


def search_contact(name):
    if name in contacts:
        return f"Contact name: {name}\nPhone number: {contacts[name]}"
    else:
        return "Contact not found ❌"


def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"{name} Deleted from contact list successfully ✅.")
    else:
        print("Contact not found ❌")


def show_contacts():
    if contacts:
        print("------ Contact List ------")
        for name, phone in contacts.items():
            print(f"{name} : {phone}")
    else:
        print("No contacts found ❌")


# Loop menu to call these functions


while True:
    print("====================")
    print("1. Add Contact")
    print("2. Search contact")
    print("3. Delete Contact")
    print("4. Show Contact")
    print("5. Exit")
    print("====================")

    choice = input("Enter your choice: ")

    if choice == "1":
        contact_name = input("Enter contact name: ")
        phone_no = input("Enter contact number: ")
        add_contact(contact_name, phone_no)

    elif choice == "2":
        contact_name = input("Enter contact name: ")
        print(search_contact(contact_name))

    elif choice == "3":
        contact_name = input("Enter contact name: ")
        delete_contact(contact_name)
    elif choice == "4":
        show_contacts()

    elif choice == "5":
        print("Exiting....")
        break
    else:
        print("Invalid input Try again..")
