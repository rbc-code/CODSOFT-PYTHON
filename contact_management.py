import json
data_file = "contacts.json"
def load_contacts():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_contacts(contacts):
    with open(data_file, "w") as file:
        json.dump(contacts, file, indent=4)
def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully!")
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    print("\nContact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
def search_contacts(contacts):
    search_term = input("Enter name or phone number to search: ").strip().lower()
    results = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]
    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No matching contacts found.")

def update_contact(contacts):
    search_contacts(contacts)
    try:
        contact_index = int(input("Enter the contact number to update: ")) - 1
        if 0 <= contact_index < len(contacts):
            contact = contacts[contact_index]
            print("Leave fields empty to keep existing values.")
            contact['name'] = input(f"Name ({contact['name']}): ").strip() or contact['name']
            contact['phone'] = input(f"Phone ({contact['phone']}): ").strip() or contact['phone']
            contact['email'] = input(f"Email ({contact['email']}): ").strip() or contact['email']
            contact['address'] = input(f"Address ({contact['address']}): ").strip() or contact['address']
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input.")

def delete_contact(contacts):
    search_contacts(contacts)
    try:
        contact_index = int(input("Enter the contact number to delete: ")) - 1
        if 0 <= contact_index < len(contacts):
            contacts.pop(contact_index)
            print("Contact deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input.")

def main():
    contacts = load_contacts()

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
