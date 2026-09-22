items = []

while True:
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        value = input("Enter Value : ")
        items.append(value)
    elif choice == "2":
        value = input("Enter Value To Delete : ")
        if value in items:
            items.remove(value)
        else:
            print("Value Not Found")
    elif choice == "3":
        value = input("Enter Value To Search : ")
        if value in items:
            print(f"Found At Position : {items.index(value)}")
        else:
            print("Value Not Found")
    elif choice == "4":
        print(items)
    elif choice == "5":
        break
    else:
        print("Invalid Choice")
