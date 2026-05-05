# URL Shortener API (AVBINVEST / 5D HUB Test Task)


Асинхронный HTTP-сервис на FastAPI для сокращения длинных URL-ссылок с хранением данных в SQLite.

## 🚀 Основной функционал
- **Сокращение URL:** Генерация коротких уникальных идентификаторов.
- **Редирект:** Мгновенное перенаправление с короткого кода на оригинальный адрес.
- **Асинхронность:** Полностью асинхронная работа с базой данных (SQLAlchemy + aiosqlite).
- **Валидация:** Строгая проверка входящих ссылок через Pydantic-схемы.

---

## 📦 Установка и запуск

1. **Клонирование ветки проекта (avbinvest) **:
   ```bash
   https://github.com/Zheka-m-p/FastAPI_test_tasks.git
   ```

2. **Настройка окружения**:
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # Linux/MacOS:
   source venv/bin/activate
   ```

3. **Установка зависимостей**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Запуск сервера**:
   ```bash
   uvicorn main:app --host 127.0.0.1 --port 8080 --reload
   ```
   *Swagger UI будет доступен по адресу: [http://127.0.0](http://127.0.0)*

---

## 📬 API Эндпоинты


| Метод | Путь | Описание |
|:--- |:--- |:--- |
| **POST** | `/create_tables` | Инициализация таблиц базы данных. |
| **POST** | `/` | Создать короткую ссылку (передать `{"url": "..."}`). |
| **GET** | `/{short_url}` | Перейти по короткой ссылке (редирект). |
| **GET** | `/async-request` | Асинхронный запрос (тестовый эндпоинт). |

---

## 📂 Структура проекта
```text
├── main.py          # Инициализация FastAPI и роуты
├── models.py        # Описание таблиц базы данных (SQLAlchemy)
├── schemas.py       # Схемы данных Pydantic (вход/выход)
├── database.py      # Конфигурация подключения к БД и сессий
├── utils.py         # Вспомогательные функции (генерация кодов)
├── requirements.txt # Зависимости проекта
└── README.md
```

---

## 🛠 Технологии
- **Backend:** FastAPI, Uvicorn
- **ORM:** SQLAlchemy 2.0 (Async)
- **DB:** SQLite + aiosqlite
- **Logic:** Pydantic, HTTPX (для асинхронных запросов)
