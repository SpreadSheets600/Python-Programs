class NegativeNumberError(Exception):
    pass


num = int(input("Enter A Positive Number : "))

if num < 0:
    raise NegativeNumberError("Negative Numbers Are Not Allowed")

print("Valid Number")
