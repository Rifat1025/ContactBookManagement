
def show_contacts(contacts):
    print("\nAll Contacts:")
    if not contacts:
        print("No contacts available.")
        return
    print("{:<15} {:<20} {:<20} {:<20}".format("Name", "Email", "Phone", "Address"))
    print("-" * 100)
    for contact in contacts:
        print("{:<20} {:<25} {:<25} {:<25}".format(contact['name'], contact['email'], contact['phone'], contact['address']))

