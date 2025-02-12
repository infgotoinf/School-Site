## The School Site
# Как работать с сайтом?
1. В консоли ```cmd``` используя ```cd``` перейти в папку проекта
2. Создать виртуальное окружение ```python -m venv env```
3. Активировать его ```cd env\Scripts``` и ```activate```
4. ```cd..``` 2 раза и ```pip install uvicorn fastapi[all] requests jinja2```
5. Перейти в ```C:\Users\<user>\AppData\Local\Programs\Python\Python313\``` и копировать папку tcl, чтобы вставить её в корневой папке виртуального окружения (env)
6. Для запуска сайта нужно в директории с python файлом в консоли прописать ```uvicorn main:app --reload```
# Как запустить консоль админа?
1. Скачать node.js ```https://nodejs.org/en/download```
2. Добавить расширение Code Runner в VS Code
3. Скачиваем штуку npm ```install simple-git```
   - Если нам это не дают сделать, то в powershell от имени администратора ```Set-ExecutionPolicy RemoteSigned```
