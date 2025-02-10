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
user_data = json.loads(data) # Получаем JSON. 😎

response = requests.get("https://raw.githubusercontent.com/infgotoinf/School-Site/refs/heads/main/files/jsons/materials.json")
data = response.content.decode('utf-8')
material_data = json.loads(data)


app = FastAPI()

templates = Jinja2Templates(directory="site")

# Говорим АПИ где находятся статик файлы
app.mount('/static', StaticFiles(directory='static'), 'static')

@app.get("/")
def root():
    return FileResponse("site/index.html")

@app.post("/login")
def postdata(login = Form(), password=Form()):
    for i in user_data:
        if ((i["login"] == login) & (i["password"] == password)):
            return FileResponse("site/menu.html")
    return FileResponse("site/index.html")

@app.get("/tables")
def root():
    return FileResponse("site/tables.html")

@app.get("/materials")
def root():
    return FileResponse("site/materials.html")