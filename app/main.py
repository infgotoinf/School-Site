from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Optional

import requests
import json
import os
from urllib.request import urlopen

root = os.path.dirname(os.path.abspath(__file__))

# Загрузка jsona с гитхаба в переменную
response = requests.get("https://raw.githubusercontent.com/infgotoinf/School-Site/refs/heads/main/jason.json")
data = response.content.decode('utf-8') # Декодируем данные
json_data = json.loads(data) # Получаем JSON. 😎

print(json_data)



app = FastAPI()

templates = Jinja2Templates(directory="Site")

# Говорим АПИ где находятся статик файлы
app.mount('/static', StaticFiles(directory='static'), 'static')

@app.get("/")
# async def main():
#     with open(os.path.join(root, 'index.html')) as fh:
#         data = fh.read()
#     return Response(content=data, media_type="html")
async def authorization(request: Request):
    return templates.TemplateResponse(name='index.html', context={'request': request})

@app.get("/menu")
async def menu(request: Request):
    return templates.TemplateResponse(name='menu.html', context={'request': request})

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