import csv
def load_contacts():
    contacts = []
    try:
        with open('data.csv', "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        with open('data.csv', "w") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "email", "phone", "address"])
            writer.writeheader()
    return contacts