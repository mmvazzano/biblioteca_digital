import sqlite3
from sqlalchemy.orm import sessionmaker
from db import engine
from crud import create_book

"""
Script para poblar la base de datos local desde metadata.db.
Este script está pensado para agregar libros desde la biblioteca de Calibre.
Extrae títulos y autores de metadata.db y los inserta en la base de datos de la app.
"""

# Conexión a metadata.db (ajusta la ruta si es necesario)
conn = sqlite3.connect("../metadata.db")
cur = conn.cursor()

# Obtiene todos los libros y sus autores
cur.execute('''
    SELECT b.title, a.name
    FROM books b
    JOIN books_authors_link bal ON b.id = bal.book
    JOIN authors a ON bal.author = a.id
''')
libros = cur.fetchall()
conn.close()

# Inserta en la base de datos de la app usando SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()
for titulo, autor in libros:
    create_book(session, titulo, autor, year=None, genre=None)
session.close()
print(f"Se importaron {len(libros)} libros desde metadata.db.")
