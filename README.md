🌐 FastAPI AVBINVEST(разделение 5D HUB Test Task) 
URL-сокращатель с асинхронной обработкой

HTTP-сервис на FastAPI для сокращения URL и асинхронных запросов.
Сервер запускается по умолчанию: http://127.0.0.1:8080 (порт/хост можно изменить).

🚀 Основные функции<br>
Сокращение длинных URL в уникальные идентификаторы. <br>
Перенаправление на оригинальный URL по короткой ссылке.<br>
Асинхронная обработка базы данных (используется SQLAlchemy + aiosqlite).<br>
RESTful API с автоматической документацией (Swagger доступен по /docs).<br>
Управление таблицами БД через эндпоинты /create_tables и /drop_tables.<br>

🛠 Установка и запуск

1. Клонируйте репозиторий :
      ```
    git clone https://github.com/Zheka-m-p/FastAPI_5D_HUB_test_task.git
   ```
2. Установите зависимости :
      ```
   pip install -r requirements.txt
   ```
   
3. Запустите сервер :
      ```
   uvicorn main:app --host 127.0.0.1 --port 8080
   ```
   
📦 Структура проекта

```
FastAPI_5D_HUB_test_task/
├── main.py              # Основной файл FastAPI-приложения
├── models.py            # Модели SQLAlchemy (UrlModel)
├── utils.py             # Утилиты для генерации коротких URL
├── schemas.py           # Схемы Pydantic для валидации данных
├── database.py          # Настройка асинхронной БД (SQLite)
├── requirements.txt     # Зависимости
├── .gitignore           # Игнорируемые файлы
└── README.md            # Документация
   ``` 
📬 API Endpoints
1. Создать таблицы БД: 
POST / /create_tables <br>
2. Удалить таблицы БД: 
POST / /drop_tables
3. Сократить URL: 
POST /
4. Получить оригинальный URL: 
GET / <short_url>
5. Список всех эндпоинтов: 
GET /
6. Асинхронный запрос (в разработке):
POST / /async-request

🧪 Пример использования<br>
   ```
# Создать таблицы
curl -X POST http://127.0.0.1:8080/create_tables

# Сократить URL
curl -X POST http://127.0.0.1:8080/ -H "Content-Type: application/json" -d '{"url": "https://example.com"}' 

# Перейти по короткой ссылке
curl -I http://127.0.0.1:8080/abc123
```

🛠 Настройки <br>
Хост/порт : Измените параметры --host и --port при запуске Uvicorn. <br>
База данных : Используется асинхронный SQLite (urls.db). Хранилище находится в текущей директории. <br>

📄 Зависимости<br>

```
aiosqlite==0.21.0
fastapi==0.115.12
sqlalchemy==2.0.41
pydantic==2.11.5
uvicorn==0.34.2
```


📝 Примечания <br>
Короткие URL генерируются случайным образом (буквы + цифры). <br>
Асинхронный запрос (пункт 3 ТЗ) пока не реализован. <br>

📄 Лицензия <br>
MIT License 
