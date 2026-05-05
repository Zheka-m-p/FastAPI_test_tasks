from fastapi import FastAPI, Depends, Response, HTTPException
from typing import Annotated
from models import Base, UrlModel
from utils import get_short_url
from database import engine, get_session, AsyncSession, host, port
from sqlalchemy import select
import uvicorn

app = FastAPI()
SessionDep = Annotated[AsyncSession, Depends(get_session)]


@app.post('/create_tables', summary='Создает все таблицы(пустыми)')
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    return {'ok': 'Талбицы созданы'}


@app.post('/drop_tables', summary='Удаляет все таблицы')
async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    return {'ok': 'Таблицы удалены'}



@app.post('/', status_code=201, summary='Добавляет новый url в таблицу urls')
async def add_url(url: str, session: SessionDep):
    query = select(UrlModel).where(UrlModel.url == url)  # Ищем url, есть ли такой уже в базе
    result = await session.execute(query)
    existing_url = result.scalars().first()

    if existing_url:
        raise HTTPException(
            status_code=409,
            detail={
                "message": "URL уже существует",
                "short_url": existing_url.short_url
            }
        )

    short_url = get_short_url(url)
    new_url = UrlModel(
        url=url,
        short_url=short_url,
    )
    session.add(new_url)
    await session.commit()
    return {'success': 'Новый url успешно добавлен в таблицу urls', 'short_url': new_url.short_url}


@app.get('/{short_url}', status_code=307, summary='Перенаправляет на исходный URL по короткому URL')
async def redirect_url(short_url: str, session: SessionDep):
    query = select(UrlModel).where(UrlModel.short_url == short_url)  # Ищем запись по полю short_url
    result = await session.execute(query)
    url_data = result.scalars().first()

    if not url_data:
        raise HTTPException(status_code=404, detail="URL not found")  # если нет такого сокращения, ошибку выдаем

    original_url = url_data.url
    return Response(headers={"Location": original_url}, status_code=307)  # Возвращаем редирект на оригинальный URL


@app.get('/', summary='Показывает список всех эндпоинтов')
async def get_list_all_end_points():
    list_end_ponts = ['/create_tables', '/drop_tables', '/', '/{url_id}']
    # надо как-то получить список или записать вручную пока что
    return {'details': list_end_ponts}


if __name__ == "__main__":
    uvicorn.run("main:app", host=host, port=port, reload=True)