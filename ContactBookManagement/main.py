import add_contact
import show_contact
import search_contact
import load_contact
import save_contact
import remove_contact

while True:

    contacts=load_contact.load_contacts()
    print("Book Contact Management menu::")
    print("1.Add_contact")
    print("2.Show the Contact")
    print("3.Search Contact")
    print("4.Remove_contact")
    print("5.Exit")

    opt=input("Chosse the option 1 to 5 ::")
    if opt=="1":
        add_contact.add_contacts(contacts)
    if opt=="2":
        show_contact.show_contacts(contacts)
    if opt=="3":
        search_contact.search_contacts(contacts)
    if opt=="4":
        remove_contact.remove_contacts(contacts)
    if opt=="5":
        save_contact.save_contacts(contacts)
        break
    else:
        print("you choose invalid option")
    
