markdown
# TF-IDF Analyzer for Text Files

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

Анализатор текстовых файлов с расчетом TF-IDF метрик. Простое FastAPI-приложение для обработки `.txt` документов.

## 📦 Установка и запуск

1. **Клонирование репозитория**:
   ```bash
   git clone https://github.com/Zheka-m-p/FAST_API_Lesta_Games_test.git
   cd FAST_API_Lesta_Games_test
Настройка окружения:

bash
python -m venv venv
# Для Windows:
.\venv\Scripts\activate
# Для Linux/MacOS:
source venv/bin/activate
Установка зависимостей:

```bash
    pip install -r requirements.txt
```
Запуск приложения:

```bash
    uvicorn main:app --reload
```
Приложение доступно по адресу: http://localhost:8000

🛠️ Функционал <br>
* Загрузка текстовых файлов (.txt)
* Расчет метрик:
* TF (Term Frequency) - частота слова
* IDF (Inverse Document Frequency) - 1/TF (упрощенная формула)
* Сортировка по убыванию IDF
* Вывод топ-50 слов в таблице


## Структура проекта
FAST_API_Lesta_Games_test/

├── main.py   
├── requirements.txt    
├── templates/          
│   └── index.html      
├── README.md         
└── .gitignore         



📜 Лицензия
MIT License