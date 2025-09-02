# Programming Assignment : Assignment 4

---

## Program 1 : Write a Python program to create a dictionary of 5 students with their roll numbers as keys and names as values. Print the dictionary

```python
students = {}

num = int(input("Enter The Number Of Students : "))

for i in range(num):
    rollNo = int(input("Enter The Roll No : "))
    name = input("Enter The Name : ")

    students[rollNo] = name

print(students)
```

OUTPUT :

```bash
Enter The Number Of Students : 2

Enter The Roll No : 1
Enter The Name : Alice

Enter The Roll No : 2
Enter The Name : Bob

{1: 'Alice', 2: 'Bob'}
```

---

## Program 2 : Create a dictionary of fruits with their prices. Ask the user to input a fruit name and print its price. If the fruit is not available, display "Not Found"

```python
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
```

OUTPUT :

```bash
Enter A Fruit Name : apple
The Price Of apple Is 100
```

---

## Program 3 : Write a program to add a new key–value pair in a dictionary and update the value of an existing key

```python
fruits = {"apple": 100, "banana": 40, "mango": 120}

print("Original Dictionary :", fruits)

fruits["orange"] = 80
print("\nAfter Updating Dictionary ~\n", fruits)
```

OUTPUT :

```bash
Original Dictionary : {'apple': 100, 'banana': 40, 'mango': 120}

After Updating Dictionary ~
 {'apple': 100, 'banana': 40, 'mango': 120, 'orange': 80}
```

---

## Program 4 : Write a program to merge two dictionaries into one. If a key is present in both, sum their values

```python
d1 = {"a": 10, "b": 20}
d2 = {"b": 30, "c": 40}

merged = d1.copy()

for key, value in d2.items():
    if key in merged:
        merged[key] += value
    else:
        merged[key] = value

print("Merged Dictionary :", merged)
```

OUTPUT :

```bash
Merged Dictionary : {'a': 10, 'b': 50, 'c': 40}
```

---

## Program 5 : Sort a dictionary by keys and values

```python
items = {"pen": 10, "notebook": 50, "eraser": 5, "pencil": 7, "bag": 300}

print("Original Dictionary :", items)

sorted_by_keys = dict(sorted(items.items()))
print("\nSorted By Keys :", sorted_by_keys)

sorted_by_values = dict(sorted(items.items(), key=lambda x: x[1]))
print("\nSorted By Values:", sorted_by_values)
```

OUTPUT :

```bash
Original Dictionary : {'pen': 10, 'notebook': 50, 'eraser': 5, 'pencil': 7, 'bag': 300}

Sorted By Keys : {'bag': 300, 'eraser': 5, 'notebook': 50, 'pen': 10, 'pencil': 7}

Sorted By Values: {'eraser': 5, 'pencil': 7, 'pen': 10, 'notebook': 50, 'bag': 300}
```

---

## Program 6 : Book management system

```python
books = {101: "Python Programming", 102: "Data Structures", 103: "Algorithms"}


def add_book(book_id, book_name):
    if book_id in books:
        print(f"Book ID {book_id} Already Exists!")

    else:
        books[book_id] = book_name
        print(f"Book '{book_name}' Added With ID {book_id}")


def remove_book(book_id):
    if book_id in books:
        removed = books.pop(book_id)
        print(f"Book '{removed}' With ID {book_id} Removed")

    else:
        print("Book ID Not Found!")


def search_book(book_id):
    if book_id in books:
        print(f"Book Found → ID : {book_id}, Name : {books[book_id]}")

    else:
        print("Book Not Found!")


def display_books():
    if not books:
        print("No Books Available")

    else:
        print("\nList of Books : ")
        for id, name in books.items():
            print(f"ID : {id}, Name : {name}")


def main():
    while True:
        print("\nBook Management System\n")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Search Book")
        print("5. Exit")
        choice = input("Enter Your Choice (1-5) : ")

        if choice == "1":
            display_books()

        elif choice == "2":
            book_id = int(input("Enter Book ID : "))
            book_name = input("Enter Book Name : ")
            add_book(book_id, book_name)

        elif choice == "3":
            book_id = int(input("Enter Book ID To Remove : "))
            remove_book(book_id)

        elif choice == "4":
            book_id = int(input("Enter Book ID To Search : "))
            search_book(book_id)

        elif choice == "5":
            print("Exiting ...")
            break
        else:
            print("Invalid Choice. Please Try Again.")


if __name__ == "__main__":
    main()  # To Make It Run Only When File Is Ran
```

OUTPUT :

```bash
Book Management System

1. Display Books
2. Add Book
3. Remove Book
4. Search Book
5. Exit
Enter Your Choice (1-5) : 1

List of Books : 
ID : 101, Name : Python Programming
ID : 102, Name : Data Structures
ID : 103, Name : Algorithms

Book Management System

1. Display Books
2. Add Book
3. Remove Book
4. Search Book
5. Exit
Enter Your Choice (1-5) : 5
Exiting ...
```

---

## Program 7 : Employees dictionary operations

```python
employees = {
    101: {"name": "Alice", "department": "HR", "salary": 40000},
    102: {"name": "Bob", "department": "IT", "salary": 55000},
    103: {"name": "Charlie", "department": "Finance", "salary": 60000},
    104: {"name": "David", "department": "IT", "salary": 70000},
    105: {"name": "Eva", "department": "HR", "salary": 45000},
}


def print_department(dept):
    print(f"\nEmployees In {dept} Department :")

    found = False

    for emp_id, details in employees.items():
        if details["department"].lower() == dept.lower():
            print(
                f"ID : {emp_id}, Name : {details['name']}, Salary : {details['salary']}"
            )
            found = True

    if not found:
        print("No Employee Found!")


def max_salary_employee():
    max_emp = max(employees.items(), key=lambda x: x[1]["salary"])
    emp_id, details = max_emp

    print(
        f"\nEmployee With Maximum Salary :\nID : {emp_id}, Name : {details['name']}, "
        f"Department : {details['department']}, Salary : {details['salary']}"
    )


print_department("IT")
max_salary_employee()
```

OUTPUT :

```bash
Employees In IT Department :
ID : 102, Name : Bob, Salary : 55000
ID : 104, Name : David, Salary : 70000

Employee With Maximum Salary :
ID : 104, Name : David, Department : IT, Salary : 70000
```

---
