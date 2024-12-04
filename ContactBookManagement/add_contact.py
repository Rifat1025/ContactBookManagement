import csv
data_file="data.csv"

def add_contacts(contacts):
    print("\n Add a New Contact:")
    name = input("Name: ")
    email = input("Email: ")

    while True:
        phone_input = input("Phone Number: ").strip()
        if phone_input.isdigit():
            phone = int(phone_input)
            break
        else:
            print("Invalid input. Phone number must contain integer value .Please try again.")
    if any(str(contact["phone"]) == str(phone) for contact in contacts):
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
