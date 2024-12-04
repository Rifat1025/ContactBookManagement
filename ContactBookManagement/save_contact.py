import csv

def save_contacts(contacts):
    with open('data.csv', "w") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "email", "phone", "address"])
        writer.writeheader()
        writer.writerows(contacts)