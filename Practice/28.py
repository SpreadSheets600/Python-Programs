num = int(input("Enter A Number : "))
sign = -1 if num < 0 else 1
num = abs(num)
reversed_num = 0

while num > 0:
    reversed_num = (reversed_num * 10) + (num % 10)
    num //= 10

print(f"Reversed Number : {reversed_num * sign}")
