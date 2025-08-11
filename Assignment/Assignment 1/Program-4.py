"""
Write a program for net amount payable on purchasing Electronic goods
If Cost >= 50000 discount : 15%
If Cost in between 30000 to 50000 discount: 10%
If Cost in between 20000 to 30000 discount : 5%
"""

cost = int(input("Enter The Cost Of Electronic Goods : "))

if cost >= 50000:
    discount = cost * 0.15
    print("The Discounted Price Is : ", cost - discount)

elif 30000 <= cost <= 50000:
    discount = cost * 0.10
    print("The Discounted Price Is : ", cost - discount)

elif 20000 >= cost <= 30000:
    discount = cost * 0.5
    print("The Discounted Price Is : ", cost - discount)

else:
    print("No Discount Available!")
