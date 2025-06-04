import pytest
from app.db import SessionLocal, engine
from app.models import Base, Book
from app.crud import create_book, get_books, delete_book

@pytest.fixture(scope='module')
def db_session():
    # Crear una nueva base de datos en memoria para pruebas
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

def test_create_book(db_session):
    book_data = {
        'title': 'Test Book',
        'author': 'Test Author',
        'year': 2023,
        'genre': 'Fiction'
    }
    book = create_book(db_session, **book_data)
    assert book.title == book_data['title']
    assert book.author == book_data['author']
    assert book.year == book_data['year']
    assert book.genre == book_data['genre']

def test_get_books(db_session):
    books = get_books(db_session)
    assert len(books) > 0  # Asegurarse de que hay libros en la base de datos

def test_delete_book(db_session):
    book = get_books(db_session)[0]  # Obtener el primer libro
    delete_book(db_session, book.id)
    books = get_books(db_session)
    assert book not in books  # Verificar que el libro ha sido eliminado