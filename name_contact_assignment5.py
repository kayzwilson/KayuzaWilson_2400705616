contacts = []


# Validation Functions

def validate_phone(phone):
    allowed = "0123456789-+"

    for char in phone:
        if char not in allowed:
            return False

    return True


def validate_email(email):

    if email == "":
        return True

    return "@" in email and "." in email


# CRUD Functions

def add_contact():

    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    if not validate_phone(phone):
        print("Error: Invalid phone number.")
        return

    if not validate_email(email):
        print("Error: Invalid email address.")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)

    print("Contact added successfully.")


def view_contact():

    name = input("Enter contact name: ")

    found = False

    for contact in contacts:

        if contact["name"].lower() == name.lower():

            print("\nContact Details")
            print("-------------------")
            print(f"Name : {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")

            found = True
            break

    if not found:
        print("Contact not found.")


def update_contact():

    name = input("Enter contact name to update: ")

    for contact in contacts:

        if contact["name"].lower() == name.lower():

            new_phone = input("Enter new phone: ")
            new_email = input("Enter new email: ")

            if not validate_phone(new_phone):
                print("Error: Invalid phone number.")
                return

            if not validate_email(new_email):
                print("Error: Invalid email.")
                return

            contact["phone"] = new_phone
            contact["email"] = new_email

            print("Contact updated successfully.")
            return

    print("Contact not found.")


def delete_contact():

    name = input("Enter contact name to delete: ")

    for contact in contacts:

        if contact["name"].lower() == name.lower():

            contacts.remove(contact)

            print("Contact deleted successfully.")
            return

    print("Contact not found.")


# Search Functions

def search_contacts():

    keyword = input(
        "Search by name, phone or email: "
    ).lower()

    results = []

    for contact in contacts:

        if (keyword in contact["name"].lower()
                or keyword in contact["phone"].lower()
                or keyword in contact["email"].lower()):

            results.append(contact)

    if len(results) == 0:
        print("No contacts found.")
        return

    print("\nSearch Results")
    print("------------------------")

    for contact in results:

        print(f"Name : {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print("------------------------")


def list_contacts():

    if len(contacts) == 0:
        print("No contacts available.")
        return

    print("\nAll Contacts")
    print("========================")

    for contact in contacts:

        print(f"Name : {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print("------------------------")


# Main Menu

def main():

    while True:

        print("\n=== Contact Manager Menu ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")

        choice = input(
            "Choose an option (1-7): "
        )

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contact()

        elif choice == "3":
            update_contact()

        elif choice == "4":
            delete_contact()

        elif choice == "5":
            search_contacts()

        elif choice == "6":
            list_contacts()

        elif choice == "7":
            print("Exiting program...")
            break

        else:
            print("Invalid option.")


main()