## The School Site
# Как работать с сайтом?
1. В консоли ```cmd``` используя ```cd``` перейти в папку проекта
2. Создать виртуальное окружение ```python -m venv env```
3. Активировать его ```cd env\Scripts``` и ```activate```
4. ```cd..``` 2 раза и ```pip install uvicorn fastapi[all] requests jinja2```
5. Для запуска сайта нужно в директории с python файлом в консоли прописать ```uvicorn main:app --reload```
