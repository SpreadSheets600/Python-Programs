num = int(input("Enter A Number : "))
original_num = abs(num)
temp = original_num
reversed_num = 0

while temp > 0:
    reversed_num = (reversed_num * 10) + (temp % 10)
    temp //= 10

if original_num == reversed_num:
    print("Palindrome")
else:
    print("Not Palindrome")
