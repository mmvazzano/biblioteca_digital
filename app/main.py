import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from app.crud import get_books, create_book
from app.models import Book
from app.db import SessionLocal
import unicodedata
from rapidfuzz import fuzz

def normalizar(texto):
    if not texto:
        return ""
    texto = texto.lower()
    texto = unicodedata.normalize('NFKD', texto)
    texto = ''.join([c for c in texto if not unicodedata.combining(c)])
    return texto

def mostrar_libros(db):
    st.header("Listado de Libros")
    books = get_books(db)
    if not books:
        st.info("No hay libros registrados.")
    else:
        df = pd.DataFrame([{
            "Título": book.title,
            "Autor": book.author,
            "Año": book.year,
            "Género": book.genre
        } for book in books])
        st.dataframe(df, use_container_width=True)

def agregar_libro(db):
    st.header("Agregar Nuevo Libro")
    with st.form(key='add_book_form'):
        title = st.text_input("Título")
        author = st.text_input("Autor")
        year = st.number_input("Año", min_value=0, max_value=2025)
        genre = st.text_input("Género")
        submit_button = st.form_submit_button("Agregar Libro")
        if submit_button:
            create_book(db, title, author, int(year), genre)
            st.success("Libro agregado exitosamente!")

def buscar_libros(db):
    st.header("Buscar Libros")
    titulo = st.text_input("Buscar por título")
    autor = st.text_input("Buscar por autor")
    genero = st.text_input("Buscar por género")
    query = db.query(Book)
    resultados = query.all()

    # Normaliza los campos de búsqueda
    titulo_norm = normalizar(titulo)
    autor_norm = normalizar(autor)
    genero_norm = normalizar(genero)

    # Filtra resultados con búsqueda flexible
    libros_filtrados = []
    for book in resultados:
        coincide = True
        if titulo_norm:
            if fuzz.partial_ratio(normalizar(book.title), titulo_norm) < 80:
                coincide = False
        if autor_norm:
            if fuzz.partial_ratio(normalizar(book.author), autor_norm) < 80:
                coincide = False
        if genero_norm:
            if fuzz.partial_ratio(normalizar(book.genre), genero_norm) < 80:
                coincide = False
        if coincide:
            libros_filtrados.append(book)

    if libros_filtrados:
        df = pd.DataFrame([{
            "Título": book.title,
            "Autor": book.author,
            "Año": book.year,
            "Género": book.genre
        } for book in libros_filtrados])
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No se encontraron libros con esos criterios.")

def main():
    st.title("Biblioteca Digital")
    db = SessionLocal()

    menu = st.sidebar.selectbox("Menú", ["Ver libros", "Agregar libro", "Buscar libros"])
    if menu == "Ver libros":
        mostrar_libros(db)
    elif menu == "Agregar libro":
        agregar_libro(db)
    elif menu == "Buscar libros":
        buscar_libros(db)

if __name__ == "__main__":
    main()