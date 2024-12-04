import csv
data_file="data.csv"

def add_contacts(contacts):
    print("\n Add a New Contact:")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone Number: ")

    # Check for duplicate phone number
    if any(contact['phone'] == phone for contact in contacts):
        print("Error: This phone number is already assigned to another contact.")
        return

    address = input("Address: ")

    new_contact = {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address,
    }
    contacts.append(new_contact)

    # Save the new contact to the file
    with open(data_file, "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "email", "phone", "address"])
        writer.writerow(new_contact)
    print("Contact added successfully!")
