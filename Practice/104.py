def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    if second == 0:
        return "Division By Zero Is Not Allowed"
    return first / second


while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "5":
        break

    num_1 = float(input("Enter Number 1 : "))
    num_2 = float(input("Enter Number 2 : "))

    if choice == "1":
        print(add(num_1, num_2))
    elif choice == "2":
        print(subtract(num_1, num_2))
    elif choice == "3":
        print(multiply(num_1, num_2))
    elif choice == "4":
        print(divide(num_1, num_2))
    else:
        print("Invalid Choice")
