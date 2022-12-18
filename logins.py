import json

from Students import Student
from Teachers import Teacher
from Admins import Admins
from functions import get_students_from_json, get_teachers_from_json, get_admins_from_json

def login(name, password):
    students = get_students_from_json()
    for key, value in students.items():
        if value["name"] == name and value["password"] == password:
            return Student(key, {key: value})
    
    teachers = get_teachers_from_json()
    for key, value in teachers.items():
        if value["name"] == name and value["password"] == password:
            return Teacher(key, {key: value})
    
    admins = get_admins_from_json()
    for key, value in admins.items():
        if value["name"] == name and value["password"] == password:
            return Admins(key, {key: value})
