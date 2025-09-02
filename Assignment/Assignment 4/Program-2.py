# Create a dictionary of fruits with their prices. Ask the user to input a fruit name and print its price. If the fruit is not available, display "Not Found".

fruits = {
    "apple": 100,
    "banana": 40,
    "mango": 120,
    "orange": 80,
    "grapes": 60
}

fruit_name = input("Enter A Fruit Name : ").lower()

if fruit_name in fruits:
    print(f"The Price Of {fruit_name} Is {fruits[fruit_name]}")
else:
    print("Not Found!")
