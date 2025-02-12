from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse

import requests
import json
import os
import shutil

from tkinter import filedialog

from encrypt import xor_encrypt_decrypt

key = "69"

# Загрузка jsona с гитхаба в переменную
response = requests.get("https://raw.githubusercontent.com/infgotoinf/School-Site/refs/heads/main/files/jsons/data.json")
data = response.content.decode('utf-8') # Декодируем данные
user_data = json.loads(data) # Получаем JSON. 😎
# Расшифровываем
for js in user_data:
    for j in js:
        js[j] = xor_encrypt_decrypt(js[j], key)
    print()

response = requests.get("https://raw.githubusercontent.com/infgotoinf/School-Site/refs/heads/main/files/jsons/materials.json")
data = response.content.decode('utf-8')
material_data = json.loads(data)


# Функция обновления физической таблицы с материалами
def update_material(new_material_data):
    with open('files/jsons/materials.json', 'w', encoding='utf-8') as file:
        json.dump(new_material_data, file, ensure_ascii=False, indent=4)

# Функция сохранения данных на гитхаб
def commit(savename):
    os.system("git add .")
    os.system(f'git commit -m "{savename}"')
    os.system("git push")


app = FastAPI()

# Говорим АПИ где находятся статик файлы
app.mount('/static', StaticFiles(directory='static'), 'static')


@app.get("/")
def root():
    return FileResponse("site/index.html")

@app.post("/login")
def postdata(login = Form(), password = Form()):
    for i in user_data:
        if ((i["login"] == login) & (i["password"] == password)):
            return FileResponse("site/menu.html")
    return FileResponse("site/index.html")

@app.get("/tables")
def root():
    return FileResponse("site/tables.html")

@app.get("/materials", response_class=HTMLResponse)
def root():
    data = "<title>Материалы</title>"
    data = data + "<h1>Материалы</h1>"
    data = data + f'<form action="materials/add" method="get">'
    data = data + f'<button class="add">Добавить</button><br></form>'
    for i in material_data:
        file = i["filename"]
        data = data + f'<a href="https://github.com/infgotoinf/School-Site/raw/refs/heads/main/files/materials/{file}">{file}</a>'
        data = data + f'<form id="{file}" action="materials/delete/{file}" method="get">'
        data = data + f'<button id="{file}" class="delete">Удалить</button><br></form>'
    return data

@app.get("/materials/add")
def add():
    path = filedialog.askopenfilename()

    if (path != ''):
        i = len(path) - 1
        filename = ''
        while (path[i] != '/'):
            filename = path[i] + filename
            i -= 1

        new = {"filename": filename}
        material_data.append(new)

        update_material(material_data)

        shutil.copy2(path, f'files/materials/{filename}')

        commit("added " + filename)
    return FileResponse("site/menu.html")

@app.get("/materials/delete/{id}")
def delete(id: str):
    i = 0
    for material in material_data:
        if (material["filename"] == id):
            material_data.pop(i)
        i += 1
    os.remove(f"files/materials/{id}")

    update_material(material_data)

    commit("deleted " + id)
    return FileResponse("site/menu.html")


# for js in user_data:
#     for j in js:
#         js[j] = xor_encrypt_decrypt(js[j], key)
#     print()

# with open('data.json', 'w', encoding='utf-8') as file:
#     json.dump(user_data, file, ensure_ascii=False, indent=4)