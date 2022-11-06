def locker():
    code1 = input("Set your password: ")
    print(code1)
    code2 = input("Repeat your password: ")
    print(code2)
    if code1 == code2:
        print("The password is correct")
    else:
        print("The password is incorrect")