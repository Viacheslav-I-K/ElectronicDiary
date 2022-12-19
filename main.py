import json
import os

from clients import Student
from functions import get_homeworks, get_teacher_by_id, table, get_homeworks_from_json
from logins import login

# name = "сергей"
# password = "1234"
# name = "Константин Юрьевич"
# password = "1234"
name = "admin"
password = "1234"
user = login(name, password)
# user.change_teachers()
# user.change_homeworkers()

while user:
    os.system('cls||clear')
    user.print_commands()
    command = input("Введите команду: ")
    user.do_command(command)
    is_continue = input("Продлжить - press Enter,  Завершить работу - exit: ")
    if is_continue == "exit":
        break
else:
    print("Login failed")