import save_contact

def remove_contacts(contacts):
    query = input("\nEnter the name or phone number of the contact to remove: ").strip().lower()
    for contact in contacts:
        if query in contact["name"].lower() or query in contact["phone"]:
            contacts.remove(contact)
            save_contact.save_contacts(contacts)
            print(f"Contact '{contact['name']}' has been removed.")
            return
    print("No matching contact found.")
    