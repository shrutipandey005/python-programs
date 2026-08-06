contacts = {}

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Search\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone

    elif choice == 2:
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == 3:
        search = input("Enter name to search: ")
        print(contacts.get(search, "Not found"))

    elif choice == 4:
        break
