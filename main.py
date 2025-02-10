from fastapi import FastAPI, Request, Response, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from django.shortcuts import render
from typing import Optional

import requests
import json
import os
from urllib.request import urlopen

root = os.path.dirname(os.path.abspath(__file__))

# Загрузка jsona с гитхаба в переменную
response = requests.get("https://raw.githubusercontent.com/infgotoinf/School-Site/refs/heads/main/files/jsons/jason.json")
data = response.content.decode('utf-8') # Декодируем данные
json_data = json.loads(data) # Получаем JSON. 😎

response = requests.get("https://raw.githubusercontent.com/infgotoinf/School-Site/refs/heads/main/files/jsons/jason.json")
data = response.content.decode('utf-8') # Декодируем данные
json_data = json.loads(data) # Получаем JSON. 😎

https://github.com/infgotoinf/School-Site/raw/refs/heads/main/files/materials/


app = FastAPI()

templates = Jinja2Templates(directory="site")

# Говорим АПИ где находятся статик файлы
app.mount('/static', StaticFiles(directory='static'), 'static')

@app.get("/")
# async def authorization(request: Request):
#     return templates.TemplateResponse(name='index.html', context={'request': request})
# def my_view(request):
#     return render(request, 'site/index.html', json_data)
def root():
    return FileResponse("site/index.html")

@app.post("/login")
def postdata(login = Form(), password=Form()):
    for i in json_data:
        if ((i["login"] == login) & (i["password"] == password)):
            return FileResponse("site/menu.html")
    return FileResponse("site/index.html")

@app.get("/tables")
def root():
    return FileResponse("site/tables.html")

@app.get("/materials")
def root():
    return FileResponse("site/materials.html")

@app.get("/login")
def login(login, password):
    users = json_data
    for user in users:
            if (user["login"] == login) & (user["password"] == password):
                return "Wellcome!"
    return "Wrong login or password!"