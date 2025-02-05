## The School Site
# Как работать с сайтом?
1. Скопировать директорию
2. В консоли ```cmd``` используя ```cd``` перейти в папку проекта
3. Создать виртуальное окружение ```python -m venv env```
4. Активировать его ```cd env\Scripts``` и ```activate```
5. ```cd..``` 2 раза и ```pip install uvicorn fastapi[all] requests```
6. Для запуска сайта нужно в директории проекта в консоли прописать ```uvicorn main:app --reload```
# Что нужно для того, чтобы консольное админа заработала в VS Code?
1. Для этого нужно воспользоваться официальным гайдом по установке C++ для VS Code: https://code.visualstudio.com/docs/cpp/config-mingw или следующим гайдом на ютубе: https://www.youtube.com/watch?v=DMWD7wfhgNY&ab_channel=KennyYipCoding
2. Далее воспользоваться гайдом по установке библиотеки из нашего предыдущего проекта https://github.com/infgotoinf/Console-Manager
