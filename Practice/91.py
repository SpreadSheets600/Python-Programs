import random


items = input("Enter List Items : ").split()

if items:
    print(random.choice(items))
else:
    print("List Is Empty")
