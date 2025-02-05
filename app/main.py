from fastapi import FastAPI
from utils import json_to_dict_list
import os
from typing import Optional

import requests
import json
from urllib.request import urlopen


response = requests.get("https://raw.githubusercontent.com/infgotoinf/School-Site/refs/heads/main/jason.json")
data = response.content.decode('utf-8') # Декодируем данные
json_data = json.loads(data) # Получаем JSON. 😎

print(json_data)


# Получаем путь к директории текущего скрипта
# script_dir = os.path.dirname(os.path.abspath(__file__))

# # Переходим на уровень выше
# parent_dir = os.path.dirname(script_dir)

# Получаем путь к JSON
# path_to_json = os.path.join(script_dir, 'jason.json')


app = FastAPI()

@app.get("/")
def root():
   return "API is working!"#FileResponse("public/index.html")

@app.get("/users")
def get_all_data(login: Optional[str] = None):
    users = json_data
    if login is None:
        return users
    else:
        return_list = []
        for user in users:
            if user["login"] == login:
                return_list.append(user)
        return return_list

@app.get("/login")
def login(login, password):
    users = json_data
    for user in users:
            if (user["login"] == login) & (user["password"] == password):
                return "Wellcome!"
    return "Wrong login or password!"