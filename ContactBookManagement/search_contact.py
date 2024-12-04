def search_contacts(contacts):
    query = input("\nSearch by name, phone, or email: ").lower()
    results = [c for c in contacts if 
                query in c["name"].lower() or
                query in c["phone"] or
                query in c["email"]]
    if results:
        print("\nSearch Results:")
        print("{:<20} {:<30} {:<15} {:<30}".format("Name", "Email", "Phone", "Address"))
        print("-" * 100)
        for contact in results:
            print("{:<20} {:<30} {:<15} {:<30}".format(contact['name'], contact['email'], contact['phone'], contact['address']))
    else:
        print("No matching contacts found.")