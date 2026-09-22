import random


def calculate_tip(bill, tip_percent):
    tip = bill * (tip_percent / 100)
    total = bill + tip
    return tip, total


def main():
    try:
        bill = float(input("Enter The Bill Amount : $"))

        tip_percent = random.randint(10, 20)
        tip, total = calculate_tip(bill, tip_percent)

        print(f"Tip : {tip:.2f}")
        print(f"Total : {total:.2f}")

    except ValueError:
        print("Please Enter Valid Amount")


if __name__ == "__main__":
    main()
