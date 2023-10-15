# To-Do

## Структура проекта

При разворачивании локально можно посмотреть используя скрипт [tree.sh](tree.sh)

```
app
├── controllers
│   ├── auth.py
│   └── user.py
├── internal
│   └── responses.py
├── main.py
├── models
│   ├── database.py
│   └── user.py
├── routers
│   ├── auth.py
│   └── users.py
└── schemas
    ├── auth.py
    └── user.py

```

## Установка модулей

Для работы сервера необходимо установить модули находящиеся в [requirements.txt](requirements.txt).

```shell
pip install -r requirements.txt
```

## Переменные среды

Также для работы проекта необходимо установить _переменные среды_:

+ FASTAPI_DB_URL - ссылка на базу данных;
+ SECRET_KEY - секретный ключ для алгоритма, генерации подписи `HS256`

## Запуск сервера

```shell
uvicorn main:app
```