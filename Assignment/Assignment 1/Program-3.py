# Write program to implement id(), type(),sep,end, | , &&, ^ , << ,>>

# User Input
a = int(input("Enter A Number : "))
b = float(input("Enter A Float :"))
c = str(input("Enter A String : "))

print("ID Of a :", id(a), "Type Of a :", type(a))
print("ID Of b :", id(b), "Type Of b :", type(b))
print("ID Of c :", id(c), "Type Of c :", type(c))

# Sep And End Parameters
print("Python", "is", "fun", sep="-", end="!\n")

# Bitwise Operator
x = 5  # 0b0101
y = 3  # 0b0011

print("x | y =", x | y)  # Bitwise OR
print("x & y =", x & y)  # Bitwise AND
print("x ^ y =", x ^ y)  # Bitwise XOR

print("x << 1 =", x << 1)  # Left shift
print("x >> 1 =", x >> 1)  # Right shift
