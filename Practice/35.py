num_1 = int(input("Enter Number 1 : "))
num_2 = int(input("Enter Number 2 : "))

greater = max(abs(num_1), abs(num_2))
lcm = greater

while True:
    if lcm % num_1 == 0 and lcm % num_2 == 0:
        print(f"LCM : {lcm}")
        break
    lcm += greater
