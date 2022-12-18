from functions import get_homeworks, table, get_homeworks_from_json, write_homeworks_to_json, get_students_from_json, get_groups_from_json
from Base import Base


class Teacher(Base):
    commannds = {
            0: "Посмотреть Д/З группе",
            1: "Задать Д/З",
            2: "Удалить Д/З",
            3: "Посмотреть группы"
        }

    def view_homeworks(self):
        headers = {"id": "ID", "homework": "Домашняя Работа", "students": "Ученики сдавшие Д/З"}
        group_id = input("Д/З какой группы выхотите посмотреть(напишие её id)?: ")
        if group_id not in self.user[self.id]["groups"]:
            print("Вы не припадаёте в ётой группе")
            return
        homeworks = get_homeworks(group_id)
        temp = []
        for item in homeworks:
            temp_id = list(item.keys())[0]
            students_res = ""
            all_students = get_students_from_json()
            i = 0
            for it in item[temp_id]["students_completed"]:
                student = all_students[it]["name"]
                students_res += f", {student}" if i > 0 else f"{student}"
                i += 1
            temp.append({
                "id": temp_id,
                "homework": item[temp_id]["homework"],
                "students": students_res
            })
        print(table(headers, temp))

    def add_homework(self):
        hw = get_homeworks_from_json()
        hw[int(list(hw.keys())[-1]) + 1] = {
            "from": self.id,
            "to_group": input("Введите ключ группы, которой адресовано Д/З: "),
            "homework": input("Текст Д/З: "),
            "deadline": input("Дата сдачи Д/З: "),
            "students_completed": []
        }
        write_homeworks_to_json(hw)
        
    
    def remove_homeworks(self, id_group, homework_id):
        all_homeworks = get_homeworks_from_json()
        for key, value in all_homeworks.items():
            if value["to_group"] == id_group and key  == homework_id:
                if self.id == value["from"]:
                    del all_homeworks[key]
                    break
                else:
                    print("Вы не задавали эту домашнюю работу и поэтому не можете её удалить.")
        write_homeworks_to_json(all_homeworks)
    
    def view_goups(self):
        headers = {"id": "ID", "name": "Имя группы"}
        groups = get_groups_from_json()
        temp = []
        for key, value in groups.items():
            if key in self.user[self.id]["groups"]:
                temp.append({
                    "id": key,
                    "name": value["name"]
                })
        print(table(headers, temp))
    
    def do_command(self, command):
        if command in [str(item) for item in self.commannds.keys()]:
            if command == "0":
                self.view_homeworks()
            elif command == "1":
                self.add_homework()
            elif command == "2":
                self.remove_homeworks(input("Введите id группы: "), input("Введите id работы: "))
            elif command == "3":
                self.view_goups()
        else:
            print("Invalid command")