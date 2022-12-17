import json

from clients import Student, Teacher

def login(name, password):
    with open("data/students.json", "r", encoding="utf-8") as f:
        students = json.load(f)
    for key, value in students.items():
        if value["name"] == name and value["password"] == password:
            return Student(key, {key: value})
    
    with open("data/teachers.json", "r", encoding="utf-8") as f:
        teachers = json.load(f)
    for key, value in teachers.items():
        if value["name"] == name and value["password"] == password:
            return Teacher(key, {key: value})
