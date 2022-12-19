import json

from Base import Base
from functions import get_teachers_from_json, write_teachers_to_json, table, get_homeworks_from_json, get_teacher_by_id, write_homeworks_to_json, get_groups_from_json, get_students_from_json, write_students_to_json


class Admins(Base):
    commannds = {
            0: "Изменить студентов",
            1: "Изменить группы",
            2: "Изменить учителей",
            3: "Изменить Д/З"
        }
    
    def change_students(self):
        students = get_students_from_json()
        local_commannds = {
            0: "Добавить учителя",
            1: "Изменить учителя",
            2: "Удалить учителя",
            3: "Посмотреть всех учителей"
        }
        for key, command in local_commannds.items():
            print(f"{command} - {key}")
        id = input("Введите id студента: ")
        command = input("Введите команду: ")
        if command == "1":
            all_students = get_students_from_json()
            data = list(input("Введите через пробел новые данные в формате: id name password group; через пробел: ").lower().split())
            for key in all_students.keys():
                if key == data[0]:
                    all_students[data[0]] = {"name": data[1], "pasword": data[2], "group": data[3]}
                    break
            write_students_to_json(all_students)
        
        if command == "0":
            if id not in list(students.keys()):
                students[id] = {
                    "name": input("Введите имя студента: "),
                    "password": input("Введите пароль студента: "),
                    "group": input("Введите группу студента: ")
                }
                write_students_to_json(students)
            else:
                print("Такой id уже занят")
        
        if command == "2":
            if id in list(students.keys()):
                del students[id]
                write_students_to_json(students)
            else:
                print("Такого id не сужествует")

        if command == "3":
            headers = {"id": "ID", "name": "Имя", "password": "Пароль", "group": "Группы"}
            temp = []
            for key, value in students.items():
                temp.append({
                    "id": key,
                    "name": value["name"],
                    "password": value["password"],
                    "group": value["group"]
                })
            print(table(headers, temp))

    def change_groups(self):
        f = input('''Введите 1 если хотите поменять группы
Введите 2 если хотите добавить группу
Введите 3 если хотите удалить группы
Введите 4, что бы посмотреть группы:  ''')
        gc = get_groups_from_json()
        id = input('Введите ключ группы c которой будем работать: ')
        if f == '1':
            if id in list(gc.keys()):
                gc[id] = {
                    "name": input("Введите наименование новой группы: "),
                    "students": [item for item in input("Введите студентов в новой группе через запитую без пробелов: ").split(",")]}
                with open("data/groups.json", "w", encoding="utf-8") as x:
                    json.dump(gc, x, indent=4, ensure_ascii=False)
            else:
                print('Такого id еще нет')

        elif f == '2':
            if id not in list(gc.keys()):
                gc[id] = {
                    "name": input("Введите наименование новой группы: "),
                    "students": [item for item in input("Введите студентов в новой группе через запитую без пробелов: ").split(",")]}
                with open("data/groups.json", "w", encoding="utf-8") as x:
                    json.dump(gc, x, indent=4, ensure_ascii=False)
            else:
                print('Такой id уже занят')

        elif f == '3':
            all_groups = get_groups_from_json()
            del all_groups[id]
            with open("data/groups.json", "w", encoding="utf-8") as x:
                json.dump(all_groups, x, indent=4, ensure_ascii=False)
        elif f == '4':
            all_groups = get_groups_from_json()
            headers = {"id": "ID", "name": "Имя группы", "students": "students"}
            temp = []
            for key, value in all_groups.items():
                temp.append({
                    "id": key,
                    "name": value["name"],
                    "students": str(value["students"])
                    })
            print(table(headers, temp))

    def change_teachers(self):
        teachers = get_teachers_from_json()
        local_commannds = {
            0: "Добавить студента",
            1: "Изменить студента",
            2: "Удалить студента",
            3: "Посмотреть всех студентов"
        }
        for key, command in local_commannds.items():
            print(f"{command} - {key}")
        id = input("Введите id учителя: ")
        command = input("Введите команду: ")
        if command == "0":
            if id not in list(teachers.keys()):
                teachers[id] = {
                    "name": input("Введите имя учителя: "),
                    "password": input("Введите пароль учителя: "),
                    "groups": [item for item in input("Введите группы учителя через запитую без пробелов: ").split(",")],
                    "subject": input("Введите предмет учителя: ")
                }
                write_teachers_to_json(teachers)
            else:
                print("Такой id уже занят")
        if command == "1":
            if id in list(teachers.keys()):
                teachers[id] = {
                    "name": input("Введите имя учителя: "),
                    "password": input("Введите пароль учителя: "),
                    "groups": [item for item in input("Введите групы учителя через запитую без пробелов: ").split(",")],
                    "subject": input("Введите предмет учителя: ")
                }
                write_teachers_to_json(teachers)
            else:
                print("Такого id не сужествует")
        if command == "2":
            if id in list(teachers.keys()):
                del teachers[id]
                write_teachers_to_json(teachers)
            else:
                print("Такого id не сужествует")
        if command == "3":
            headers = {"id": "ID", "name": "Имя", "password": "Пароль", "groups": "Группы", "subject": "Предмет"}
            temp = []
            for key, value in teachers.items():
                temp.append({
                    "id": key,
                    "name": value["name"],
                    "password": value["password"],
                    "groups": str(value["groups"]),
                    "subject": value["subject"]
                })
            print(table(headers, temp))
                
        

    def change_homeworkers(self):
        homeworks = get_homeworks_from_json()
        local_commannds = {
            0: "Добавить Д/З",
            1: "Изменить Д/З",
            2: "Удалить Д/З",
            3: "Посмотреть Д/З"
        }
        for key, command in local_commannds.items():
            print(f"{command} - {key}")
        id = input("Введите id Д/З: ")
        command = input("Введите команду: ")
        if command == "0":
            if id not in list(homeworks.keys()):
                homeworks[id] = {
                        "from": input("Введите кто задал Д/З его id: "),
                        "to_group": input("Введите какой группе задали Д/З её id: "),
                        "homework": input("Введите текст Д/З: "),
                        "deadline": input("Введите срок задичи Д/З: "),
                        "students_completed": []
                    }
                write_homeworks_to_json(homeworks)
            else:
                print("Такой id уже занят")
        if command == "1":
            if id in list(homeworks.keys()):
                homeworks[id] = {
                        "from": input("Введите кто задал Д/З его id: "),
                        "to_group": input("Введите какой группе задали Д/З её id: "),
                        "homework": input("Введите текст Д/З: "),
                        "deadline": input("Введите срок задичи Д/З: "),
                        "students_completed": []
                    }
                write_homeworks_to_json(homeworks)
            else:
                print("Такого id не сужествует")
        if command == "2":
            if id in list(homeworks.keys()):
                del homeworks[id]
                write_homeworks_to_json(homeworks)
            else:
                print("Такого id не сужествует")

        if command == "3":
            headers = {"id": "ID", "from": "Учитель", "subject": "Предмет", "homework": "Задание", "deadline": "Срок выполнения", "student_completed": "Кто сдал"}
            temp = []
            for key, value in homeworks.items():
                teacher = get_teacher_by_id(value["from"])
                temp.append({
                    "id": key,
                    "from": teacher["name"],
                    "subject": teacher["subject"],
                    "homework": value["homework"],
                    "deadline": value["deadline"],
                    "student_completed": str(value["students_completed"])
                })
            print(table(headers, temp))

    def do_command(self, command):
        if command in [str(item) for item in self.commannds.keys()]:
            print("----------------------------------------------------------------")
            if command == "0":
                self.change_students()
            elif command == "1":
                self.change_groups()
            elif command == "2":
                self.change_teachers()
            elif command == "3":
                self.change_homeworkers()
        else:
            print("Invalid command")