import json
import os
os.chdir(os.path.dirname(__file__))


def get_students_from_json():
    with open("data/students.json", "r", encoding="utf-8") as f:
        students = json.load(f)
    return students

def get_teachers_from_json():
    with open("data/teachers.json", "r", encoding="utf-8") as f:
        teachers = json.load(f)
    return teachers

def get_groups_from_json():
    with open("data/groups.json", "r", encoding="utf-8") as f:
        groups = json.load(f)
    return groups

def get_homeworks_from_json():
    with open("data/homeworks.json", "r", encoding="utf-8") as f:
        homeworks = json.load(f)
    return homeworks

def get_admins_from_json():
    with open("data/admins.json", "r", encoding="utf-8") as f:
        admins = json.load(f)
    return admins

def write_homeworks_to_json(homeworks):
    with open("data/homeworks.json", "w", encoding="utf-8") as f:
        json.dump(homeworks, f, indent=4, ensure_ascii=False)

def write_teachers_to_json(teachers):
    with open("data/teachers.json", "w", encoding="utf-8") as f:
        json.dump(teachers, f, indent=4, ensure_ascii=False) 

def get_teacher_by_id(id):
    teachers = get_teachers_from_json()
    return teachers.get(id)

def get_homeworks(id_group):
    res = []
    all_homeworks = get_homeworks_from_json()
    for key, value in all_homeworks.items():
        if value["to_group"] == id_group:
            res.append({key: value})
    return res

def table(headers, data):
    lens = {}
    for key, value in headers.items():
        lens[key] = 0
    for item in data:
        for key, value in headers.items():
            if len(item[key]) > lens[key]:
                lens[key] = len(item[key])
    res = "+"
    for key, value in headers.items():
        if lens[key] < len(value):
            lens[key] = len(value) + 1
        res += f"{' ' * (lens[key] - len(value) - 1)}{value} +"
    res += "\n|"
    for key, value in headers.items():
        res += f"{'-' * lens[key]}|"
    res += "\n"
    for item in data:
        temp = "|"
        for key, value in headers.items():
            temp += f"{' ' * (lens[key] - len(item[key]))}{item[key]}|"
        res += temp
        res += "\n"
    res += "+"
    for key, value in headers.items():
        res += f"{'-' * lens[key]}+"
    return res

def write_students_to_json(students):
    with open("data/students.json", "w", encoding="utf-8") as f:
        json.dump(students, f, indent=4, ensure_ascii=False)
