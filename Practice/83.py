def simple_interest(principal, rate=5, time=1):
    return (principal * rate * time) / 100


principal = float(input("Enter Principal : "))
rate_text = input("Enter Rate Or Press Enter : ")
time_text = input("Enter Time Or Press Enter : ")

rate = float(rate_text) if rate_text else 5
time = float(time_text) if time_text else 1

print(f"Simple Interest : {simple_interest(principal, rate, time)}")
