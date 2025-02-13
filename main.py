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

response = requests.get("https://raw.githubusercontent.com/infgotoinf/School-Site/refs/heads/main/admin/AllDataDatabase.json")
data = response.content.decode('utf-8')
table_data = json.loads(data)


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

@app.get("/tables", response_class=HTMLResponse)
def tables():
    data = \
'<!DOCTYPE html> \
<html lang="ru"> \
    <head> \
        <meta charset="UTF-8"> \
        <meta name="viewport" content="width=device-width, initial-scale=1.0"> \
        <title>Таблицы</title> \
        <link rel="stylesheet" type="text/css" href="/static/base.css"> \
    </head> \
    <body> \
        <p class="words">Таблицы</p>'
    for table in table_data:
        response = requests.get(f"https://raw.githubusercontent.com/infgotoinf/School-Site/refs/heads/main/files/tables/{table["name"]}")
        dat = response.content.decode('utf-8')
        cur_table = json.loads(dat)
        data = data + '<a class="link">' + table["name"] + '<br>'
        print(table)
        for elem in cur_table:
            data = data + str(elem) + '<br>'
        data = data + '</a><br>'
    data = data + \
    '</body> \
</html>'
    return data

@app.get("/materials", response_class=HTMLResponse)
def materials():
    data = \
'<!DOCTYPE html> \
<html lang="ru"> \
    <head> \
        <meta charset="UTF-8"> \
        <meta name="viewport" content="width=device-width, initial-scale=1.0"> \
        <title>School Site</title> \
        <link rel="stylesheet" type="text/css" href="/static/base.css"> \
    </head> \
    <body> \
        <p class="words">Материалы</p> \
        <form action="materials/add" method="get"> \
            <button class="button">Добавить</button> \
        </form>'
    for i in material_data:
        file = i["filename"]
        data = data + \
        f'<form id="{file}" action="materials/delete/{file}" method="get"> \
            <a class="link" href="https://github.com/infgotoinf/School-Site/raw/refs/heads/main/files/materials/{file}">{file}</a> \
            <button id="{file}" class="button">Удалить</button> \
        </form>'
    data = data + \
    '</body> \
</html>'
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