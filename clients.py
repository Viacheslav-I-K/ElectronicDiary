'''
Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы.
'''
from functions import get_homeworks, get_teacher_by_id, table, get_homeworks_from_json, write_homeworks_to_json

class Student:
    commannds = {
            0: "Посмотреть Д/З",
            1: "Сдать Д/З"
        }

    def __init__(self, id, student):
        self.id = id
        self.student = student
    
    def print_data(self, data):
        print(data)

    def view_homework(self):
        homeworks = get_homeworks(self.student[self.id]['group'])
        headers = {"id": "ID", "from": "Учитель", "subject": "Предмет", "homework": "Задание", "deadline": "Срок выполнения", "student_completed": "Статус"}
        temp = []
        for item in homeworks:
            for key, value in item.items():
                teacher = get_teacher_by_id(value["from"])
                temp.append({
                    "id": key,
                    "from": teacher["name"],
                    "subject": teacher["subject"],
                    "homework": value["homework"],
                    "deadline": value["deadline"],
                    "student_completed": "Сдано" if self.id in value["students_completed"] else "Не сдано"
                })
        print(table(headers, temp))
    
    def make_homework(self, homework_id):
        '''
        self.id - id студента
        '''
        pass

    def make_homework(self, homework_id):
        temp_hw = get_homeworks_from_json()
        if temp_hw.get(homework_id) is None:
            print('Такой работы нет')
        elif self.id not in temp_hw[homework_id]["students_completed"] and temp_hw[homework_id]["to_group"] == self.student[self.id]["group"] :
            temp_hw[homework_id]["students_completed"].append(self.id)
        else:
            print('Ошибка при сдаче ДЗ')
        
        write_homeworks_to_json(temp_hw)


    
    def print_commands(self):
        for key, command in self.commannds.items():
            print(f"{command} - {key}")

    def do_command(self, command):
        if command in [str(item) for item in self.commannds.keys()]:
            if command == "0":
                self.view_homework()
            elif command == "1":
                self.make_homework(input("Введите id работы: "))
        else:
            print("Invalid command")

class Teacher(Student):
    def view_homeworks(self, group_id):
        headers = {"id": "ID", "homework": "Домашняя Работа", "subject": "Предмет"}

    def add_homeworks(self, group_id):
        pass
    def remove_homeworks(self, id_group, homework_id):
        all_homeworks = get_homeworks_from_json()
        for key, value in all_homeworks.items():
            if value["to_group"] == id_group and key  == homework_id:
                if self.id == value["from"]:
                    del all_homeworks[key]
                    break
                else: print("Вы не задавали эту домашнюю работу и поэтому не можете её удалить.")
        write_homeworks_to_json(all_homeworks)

class Admin(Teacher):
    pass
