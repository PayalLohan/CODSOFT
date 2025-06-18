

class Contact:
    """Represents a single contact with name, phone, email, and address."""
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Phone: {self.phone}\n"
                f"Email: {self.email}\n"
                f"Address: {self.address}\n")

class ContactBook:
    """Manages a collection of contacts."""
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        """Allows user to add a new contact."""
        print("\n--- Add New Contact ---")
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email Address: ")
        address = input("Enter Address: ")
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added successfully!")

    def view_contact_list(self):
        """Displays a list of all saved contacts (name and phone)."""
        print("\n--- Contact List ---")
        if not self.contacts:
            print("No contacts available.")
            return

        for i, contact in enumerate(self.contacts):
            print(f"{i+1}. Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self):
        """Allows user to search for a contact by name or phone number."""
        print("\n--- Search Contact ---")
        if not self.contacts:
            print("No contacts to search.")
            return

        search_term = input("Enter Name or Phone Number to search: ").lower()
        found_contacts = []
        for contact in self.contacts:
            if search_term in contact.name.lower() or search_term in contact.phone:
                found_contacts.append(contact)

        if found_contacts:
            print("\n--- Found Contacts ---")
            for contact in found_contacts:
                print(contact)
        else:
            print(f"No contacts found matching '{search_term}'.")

    def update_contact(self):
        """Enables users to update contact details."""
        print("\n--- Update Contact ---")
        self.view_contact_list()
        if not self.contacts:
            return

        try:
            choice = int(input("Enter the number of the contact to update: ")) - 1
            if 0 <= choice < len(self.contacts):
                contact = self.contacts[choice]
                print(f"Updating contact: {contact.name}")
                contact.name = input(f"Enter new Name (current: {contact.name}): ") or contact.name
                contact.phone = input(f"Enter new Phone (current: {contact.phone}): ") or contact.phone
                contact.email = input(f"Enter new Email (current: {contact.email}): ") or contact.email
                contact.address = input(f"Enter new Address (current: {contact.address}): ") or contact.address
                print(f"Contact '{contact.name}' updated successfully!")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def delete_contact(self):
        """Provides an option to delete a contact."""
        print("\n--- Delete Contact ---")
        self.view_contact_list()
        if not self.contacts:
            return

        try:
            choice = int(input("Enter the number of the contact to delete: ")) - 1
            if 0 <= choice < len(self.contacts):
                deleted_contact = self.contacts.pop(choice)
                print(f"Contact '{deleted_contact.name}' deleted successfully!")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def display_menu():
    """Displays the main menu options to the user."""
    print("\n===== Contact Book Menu =====")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("=============================")

def main():
    """Main function to run the Contact Book application."""
    contact_book = ContactBook()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            contact_book.add_contact()
        elif choice == '2':
            contact_book.view_contact_list()
        elif choice == '3':
            contact_book.search_contact()
        elif choice == '4':
            contact_book.update_contact()
        elif choice == '5':
            contact_book.delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()