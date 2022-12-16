import json

from clients import Student

def login(name, password):
    with open("diary/students.json", "r", encoding="utf-8") as f:
        students = json.load(f)
        for key, value in students.items():
            if value["name"] == name and value["password"] == password:
                data = {key: value}
                return Student(key, data)
    return False

name = input() #"сергей"
password = input()# "1234"

user = login(name, password)



while user:
    user.print_commands()
    command = input("Введите команду: ")
    if command == "exit":
        break
    user.do_command(command)
else:
    print("Login failed")