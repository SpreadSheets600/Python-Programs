def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


count = int(input("Enter How Many Numbers : "))
numbers = []

for index in range(1, count + 1):
    numbers.append(int(input(f"Enter Number {index} : ")))

for number in numbers:
    if is_prime(number):
        print(number)
