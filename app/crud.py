from sqlalchemy.orm import Session
from models import Book

def create_book(db: Session, title: str, author: str, year: int, genre: str):
    db_book = Book(title=title, author=author, year=year, genre=genre)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Book).offset(skip).limit(limit).all()

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def delete_book(db: Session, book_id: int):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book

def update_book(db: Session, book_id: int, title: str = None, author: str = None, year: int = None, genre: str = None):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        if title is not None:
            db_book.title = title
        if author is not None:
            db_book.author = author
        if year is not None:
            db_book.year = year
        if genre is not None:
            db_book.genre = genre
        db.commit()
        db.refresh(db_book)
    return db_book