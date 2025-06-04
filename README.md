# Proyecto: Biblioteca Digital - Aplicación de Ciencia de Datos

## Descripción
Este proyecto consiste en una aplicación de biblioteca digital desarrollada en Python. La aplicación permite a los usuarios buscar libros, agregar nuevos libros manualmente o mediante el escaneo de portadas, y almacenar toda la información en una base de datos SQLite utilizando SQLAlchemy como ORM. La interfaz de usuario está construida con Streamlit, y se utiliza Pytesseract junto con TensorFlow para extraer texto de las imágenes de las portadas de los libros.

## Estructura del Proyecto
La estructura del proyecto es la siguiente:

```
biblioteca_digital/
├── app/
│   ├── __init__.py           # Inicializa el paquete de la aplicación
│   ├── main.py                # Interfaz principal en Streamlit
│   ├── db.py                  # Configuración de la base de datos con SQLAlchemy
│   ├── crud.py                # Funciones para manejar libros (CRUD)
│   ├── models.py              # Modelos de datos con SQLAlchemy
│   └── ocr.py                 # Lógica para reconocimiento de texto desde imagen
├── data/
│   └── sample_cover.jpg       # Imagen de ejemplo para pruebas
├── tests/
│   └── test_crud.py           # Pruebas unitarias para funciones de base de datos
├── requirements.txt           # Lista de dependencias
├── README.md                  # Documentación del proyecto
└── .streamlit/
    └── config.toml            # Configuraciones opcionales para Streamlit
```

## Instalación
Para instalar y ejecutar el proyecto, sigue estos pasos:

1. Clona el repositorio o descarga los archivos del proyecto.
2. Crea un entorno virtual:
   ```
   python -m venv venv
   ```
3. Activa el entorno virtual:
   - En Windows:
     ```
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```
     source venv/bin/activate
     ```
4. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Uso
Para ejecutar la aplicación, utiliza el siguiente comando en la terminal:
```
streamlit run app/main.py
```

## Funcionalidades
- Listado de libros con opciones de filtrado.
- Formulario para agregar nuevos libros.
- Subida de imágenes de portadas para extracción de texto mediante OCR.
- CRUD básico para gestionar libros en la base de datos.
- Pruebas unitarias para asegurar el correcto funcionamiento de las funciones.

## Extensiones Futuras
- Clasificación automática del género usando TensorFlow.
- Exportación de la base de datos a CSV o PDF.
- Sistema de login para usuarios.
- Estadísticas y gráficos sobre libros (por año, autor, género, etc.).

## Contribuciones
Las contribuciones son bienvenidas. Si deseas colaborar, por favor abre un issue o envía un pull request.