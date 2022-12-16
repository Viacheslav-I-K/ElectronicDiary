'''
Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы.
'''

class Student:
    commannds = ["view_homework"]

    def __init__(self, id, student):
        self.id = id
        self.student = student
    
    def view_homework(self):
        if self.is_login:
            return "data"

    def view(self):
        if self.is_login:
            pass
    
    def print_data(self, data):
        print(data)


    def print_commands(self):
        print(f"Доступные коменды{self.commannds}")

    def do_command(self, command):
        if command in self.commannds:
            if command == "view_homework":
                self.print_data(f"Ваша домашняя работа {self.student[self.id]['homework']}")
        else:
            print("Invalid command")

class Teacher(Student):
    pass

class Admin(Teacher):
    pass

a = Student("max", 1234)