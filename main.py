from fastapi import FastAPI, Request, Response, Form, Depends
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

# @app.get("/materials")
#     return FileResponse("site/materials.html")
# async def get_files_html(request: Request, files=Depends(material_data)):
#     return templates.TemplateResponse(request=Request, name='materials.html', context={'files': files})

# link_template = "/materials/{file}"
# @app.post(link_template.format(file=material_data[0]["filename"]))
# def download():
#     download_template = "files/materials/{file}"
#     return FileResponse(download_template.format(file=material_data[0]["filename"]))

@app.get("/materials", response_class=HTMLResponse)
def root():
    data = "<h1>Материалы</h1>"
    for i in material_data:
        data = data + f"<p>{i["filename"]}</p>"
    return data

link_template = "/materials/{file}"
#print(link_template.format(file=material_data[0]["filename"]))