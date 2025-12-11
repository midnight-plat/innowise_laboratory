from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional


import models
import schemas
from database import engine, get_db


# Сreate tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book Collection API")


# Endpoints

#  POST /books/
@app.post("/books/", response_model=schemas.BookResponse, status_code=201, summary="Add book")
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):



    db_book = models.Book(title=book.title, author=book.author, year=book.year)

    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book


#  GET /books/
@app.get("/books/", response_model=List[schemas.BookResponse], summary="All books")
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = db.query(models.Book).offset(skip).limit(limit).all()
    return books


# 3. DELETE /books/{book_id}
@app.delete("/books/{book_id}", status_code=204, summary="Remove book via ID")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")

    db.delete(book)
    db.commit()
    return


# 4. PUT /books/{book_id}
@app.put("/books/{book_id}", response_model=schemas.BookResponse, summary="Update book via ID")
def update_book(book_id: int, updated_data: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if db_book is None:
        raise HTTPException(status_code=404, detail="Not found")


    db_book.title = updated_data.title
    db_book.author = updated_data.author
    db_book.year = updated_data.year

    db.commit()
    db.refresh(db_book)

    return db_book


# 5. GET /books/search/
@app.get("/books/search/", response_model=List[schemas.BookResponse], summary="Find global books")
def search_books(
        q: Optional[str] = Query(None, description="Via author or name "),
        year: Optional[int] = Query(None, description="Via yaer"),
        db: Session = Depends(get_db)
):

    query = db.query(models.Book)

    if q:

        query = query.filter(
            (models.Book.title.ilike(f"%{q}%")) |
            (models.Book.author.ilike(f"%{q}%"))
        )

    if year is not None:
        query = query.filter(models.Book.year == year)

    books = query.all()

    if not books:

        raise HTTPException(status_code=404, detail="Not found")

    return books