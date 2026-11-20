contacts = {}

while True:
    print("\n1.Add 2.View 3.Search 4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone

    elif choice == "2":
        print(contacts)

    elif choice == "3":
        name = input("Enter name: ")
        print(contacts.get(name, "Contact not found"))

    elif choice == "4":
        break

    else:
        print("Invalid choice")