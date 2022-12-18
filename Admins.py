from Base import Base
from functions import get_teachers_from_json, write_teachers_to_json, table, get_homeworks_from_json, get_teacher_by_id, write_homeworks_to_json

class Admins(Base):
    commannds = {
            0: "Изменить студентов",
            1: "Изменить группы",
            2: "Изменить учителей",
            3: "Изменить Д/З"
        }
    
    def change_students(self):
        '''
        Вечеслав
        добавление измение и удаление
        '''
        pass

    def change_groups(self):
        '''
        Николая
        добавление измение и удаление
        '''
        pass

    def change_teachers(self):
        teachers = get_teachers_from_json()
        local_commannds = {
            0: "Добавить учителя",
            1: "Изменить учителя",
            2: "Удалить учителя",
            3: "Посмотреть всех учителей"
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
                    "groups": [item for item in input("Введите групы учителя через запитую без пробелов: ").split(",")],
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
