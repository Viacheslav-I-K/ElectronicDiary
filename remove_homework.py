
import json


def write_homeworks_to_json(homeworks): 
    with open("data/homeworks1.json", "w", encoding="utf-8") as f:
        json.dump(homeworks, f, indent=4, ensure_ascii=False)


def get_homeworks_from_json():
    with open("data/homeworks.json", "r", encoding="utf-8") as f:
        homeworks = json.load(f)
    return homeworks


def remove_homeworks(id_group, homework_id):
    all_homeworks = get_homeworks_from_json()
    for key, value in all_homeworks.items():
        if value["to_group"] == id_group and key  == homework_id:
            del all_homeworks[key]
            break
    return all_homeworks


write_homeworks_to_json(remove_homeworks('0', '0'))
