
def hello():
    print("Hello World")

def personalInfo():
    name = input("Give me your name: ")
    surname = input("Give me your surname: ")
    birth = input("Give me your year of birth: ")
    print("Name: " + name + ", surname: " + surname + ", year of birth: " + birth)

def locker():
    code1 = input("Set your password: ")
    print(code1)
    code2 = input("Repeat your password: ")
    print(code2)
    if code1 == code2:
        print("The password is correct")
    else:
        print("The password is incorrect")

import os
def counter():
    directoryPath = r'/Users/macbook/desktop/studia_all'
    count = 0
    for path in os.listdir(directoryPath):
        if os.path.isfile(os.path.join(directoryPath, path)):
            count += 1
    print("The number of file is: ", count)
