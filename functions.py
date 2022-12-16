import json


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


if __name__ == "__main__":
    print(get_homework("2"))
    print(get_teacher_by_id("0"))

'''
def homeworks_from_json(action="read", data={}):
    if action == "read":
        with open("data/homeworks.json", "r", encoding="utf-8") as f:
            homeworks = json.load(f)
        return homeworks
    elif action == "write":
        with open("data/homeworks.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
'''