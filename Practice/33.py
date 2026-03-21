start = int(input("Enter Start Number : "))
end = int(input("Enter End Number : "))

for number in range(start, end + 1):
    if number < 2:
        continue

    is_prime = True

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(number)
