import json
import os

from clients import Student


def login(name, password):
    with open("data/students.json", "r", encoding="utf-8") as f:
        students = json.load(f)
        for key, value in students.items():
            if value["name"] == name and value["password"] == password:
                data = {key: value}
                return Student(key, data)
    return False

name = "сергей"
password = "1234"

user = login(name, password)



while user:
    os.system('clear')
    user.print_commands()
    command = input("Введите команду: ")
    user.do_command(command)
    is_continue = input("Продлжить - press Enter,  Завершить работу - exit: ")
    if is_continue == "exit":
        break
else:
    print("Login failed")