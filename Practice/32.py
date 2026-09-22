num = int(input("Enter A Number : "))

if num < 2:
    print("Not Prime")
else:
    is_prime = True

    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")
