# Program 4 : Take a tuple and unpack its elements into variables and print them.

tup = (1, 2, 3, 4, 5)
a, b, c, d, e = tup

print("Unpacked Variables : ")
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
print("e =", e)

# Other Method ~
print("Upack Operator : ", *tup)
