from fastapi import FastAPI, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import re
from collections import defaultdict
import math

app = FastAPI()
templates = Jinja2Templates(directory="templates")


def analyze_text(content: str) -> list[dict]:
    """Анализирует текст и возвращает список слов с TF и IDF"""
    words = re.findall(r'\w+', content.lower())  # Все слова в нижнем регистре

    # Считаем TF (количество вхождений каждого слова)
    tf_dict = defaultdict(int)
    for word in words:
        tf_dict[word] += 1

    # Считаем IDF (1/TF)
    stats = []
    for word, tf in tf_dict.items():
        stats.append({
            "word": word,
            "tf": tf,
            "idf": 1 / tf  # Ваша формула IDF
        })

    # Сортируем по убыванию IDF
    stats.sort(key=lambda x: x["idf"], reverse=True)

    # Ограничиваем 50 словами
    return stats[:50]


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "results": None
    })


@app.post("/upload")
async def handle_upload(request: Request, file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")

    results = analyze_text(text)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "results": results,
        "filename": file.filename
    })