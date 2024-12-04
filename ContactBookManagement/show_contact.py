
def show_contacts(contacts):
    print("\nAll Contacts:")
    if not contacts:
        print("No contacts available.")
        return
    print("{:<20} {:<30} {:<15} {:<30}".format("Name", "Email", "Phone", "Address"))
    print("-" * 100)
    for contact in contacts:
        print("{:<20} {:<30} {:<15} {:<30}".format(contact['name'], contact['email'], contact['phone'], contact['address']))

