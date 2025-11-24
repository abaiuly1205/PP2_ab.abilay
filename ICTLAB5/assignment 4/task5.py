contacts = {
    "Ayan": "87011234567",
    "Nursultan": "87012345678",
    "Aigerim": "87023456789",
    "Madina": "87034567890",
    "Yerlan": "87045678901",
}

while True:
    print("\ncontact manager")
    print("1. add contact")
    print("2. view contacts")   
    print("3. search for contact by name")
    print("4. delete contact")
    print("q. quit")
    choice = input("enter your choice: ")

    if choice == "1":
        name = input("enter name: ")
        phone = input("enter phone number: ")
        contacts[name] = phone
        print("contact added.")
    elif choice == "2":
        if not contacts:
            print("no contacts found.")
        else:
            print("contacts:")
            for name, phone in contacts.items():
                print("Name:", name, ", Phone:", phone)
    elif choice == "3":
        search_name = input("enter name to search: ")
        if search_name in contacts:
            print("found contact - Name:", search_name, ", Phone:", contacts[search_name])
        else:
            print("contact not found.")
    elif choice == "4":
        delete_name = input("enter name to delete: ")
        if delete_name in contacts:
            del contacts[delete_name]
            print("contact deleted.")
        else:
            print("contact not found.")
    elif choice == "q":
        print("goodbye!")
        break
    else:
        print("invalid choice.")