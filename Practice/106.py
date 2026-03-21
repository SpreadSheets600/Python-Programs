students = {}

while True:
    print("1. Add")
    print("2. Update")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        name = input("Enter Student Name : ")
        marks = float(input("Enter Marks : "))
        students[name] = marks
    elif choice == "2":
        name = input("Enter Student Name : ")
        if name in students:
            students[name] = float(input("Enter New Marks : "))
        else:
            print("Student Not Found")
    elif choice == "3":
        name = input("Enter Student Name : ")
        if name in students:
            del students[name]
        else:
            print("Student Not Found")
    elif choice == "4":
        print(students)
    elif choice == "5":
        break
    else:
        print("Invalid Choice")
