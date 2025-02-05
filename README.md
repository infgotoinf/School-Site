## The School Site
# Как работать с сайтом?
1. Скопировать директорию
2. В консоли ```cmd``` используя ```cd``` перейти в папку проекта
3. Создать виртуальное окружение ```python -m venv env```
4. Активировать его ```cd env\Scripts``` и ```activate```
5. ```cd..``` 2 раза и ```pip install uvicorn fastapi[all] requests```
6. Для запуска сайта нужно в директории проекта в консоли прописать ```uvicorn main:app --reload```
