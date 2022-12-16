import json

from clients import Student, Teacher

def login(name, password):
    with open("diary/students.json", "r", encoding="utf-8") as f:
        students = json.load(f)
    with open("diary/students.json", "r", encoding="utf-8") as f:
        students = json.load(f)
    return Student(id)
    return Teacher(id)
    return False