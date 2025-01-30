from fastapi import FastAPI
# from utils import object_detection
from utils import json_to_dict_list
import os
from typing import Optional
import json


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

@app.get("/get_all/{id}")
def get_all_data(id : int):
   users = json_to_dict_list(path_to_json)
   return_list = []
   for user in users:
      if user["id"] == id:
         return_list.append(users)
   return return_list