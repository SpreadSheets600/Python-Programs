try:
    num_1 = float(input("Enter Number 1 : "))
    num_2 = float(input("Enter Number 2 : "))
    print(f"Result : {num_1 / num_2}")
except ZeroDivisionError:
    print("Division By Zero Is Not Allowed")
