larger = lambda first, second: first if first > second else second

num_1 = float(input("Enter Number 1 : "))
num_2 = float(input("Enter Number 2 : "))

print(f"Larger Number : {larger(num_1, num_2)}")
