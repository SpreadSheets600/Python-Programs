correct_password = "python123"

while True:
    password = input("Enter Password : ")
    if password == correct_password:
        print("Correct Password")
        break
    print("Wrong Password")
