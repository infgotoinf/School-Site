from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse

import requests
import json
import os

from tkinter import filedialog

from encrypt import xor_encrypt_decrypt

root = os.path.dirname(os.path.abspath(__file__))
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


app = FastAPI()

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

@app.get("/materials", response_class=HTMLResponse)
def root():
    data = "<h1>Материалы</h1>"
    data = data + f'<button action="login" class="add" method="post">Отправить</button><br>'
    for i in material_data:
        file = i["filename"]
        data = data + f'<a href="https://github.com/infgotoinf/School-Site/raw/refs/heads/main/files/materials/{file}">{file}</a>'
        data = data + f'<button id="{file}" class="delete">Удалить</button><br>'
    return data

@app.post("/materials/add")
def add():
    File = filedialog.askopenfilename()
    # print(File)

    if (File != ''):
        i = len(File) - 1
        Filename = ''
        while (File[i] != '/'):
            Filename = File[i] + Filename
            i -= 1
        # print(Filename)
    return data

# for js in user_data:
#     for j in js:
#         js[j] = xor_encrypt_decrypt(js[j], key)
#     print()

# with open('data.json', 'w', encoding='utf-8') as file:
#     json.dump(user_data, file, ensure_ascii=False, indent=4)