terms = int(input("Enter Number Of Terms : "))
first = 0
second = 1

for _ in range(terms):
    print(first)
    first, second = second, first + second
