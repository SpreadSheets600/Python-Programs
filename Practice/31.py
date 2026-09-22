for number in range(1, 1001):
    digits = str(number)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    if total == number:
        print(number)
