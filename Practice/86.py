def fibonacci(terms, first=0, second=1):
    if terms <= 0:
        return

    print(first)
    fibonacci(terms - 1, second, first + second)


terms = int(input("Enter Number Of Terms : "))
fibonacci(terms)
