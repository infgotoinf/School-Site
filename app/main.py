from fastapi import FastAPI
from utils import json_to_dict_list
import os
from typing import Optional

import requests
import json

def get_result():
    r = requests.get("https://raw.githubusercontent.com/infgotoinf/School-Site/refs/heads/main/jason.json")
    return r

f = get_result()

for i in f:
    for j in i:
        print(j)
    print()

# Получаем путь к директории текущего скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))

# # Переходим на уровень выше
# parent_dir = os.path.dirname(script_dir)

# Получаем путь к JSON
path_to_json = os.path.join(script_dir, 'jason.json')


app = FastAPI()

@app.get("/")
def root():
   return "API is working!"#FileResponse("public/index.html")


@app.get("/users")
def get_all_data(access_level: Optional[int] = None):
    students = json_to_dict_list(path_to_json)
    if access_level is None:
        return students
    else:
        return_list = []
        for student in students:
            if student["access_level"] == access_level:
                return_list.append(student)
        return return_list

