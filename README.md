# Proyecto: Biblioteca Digital - Aplicación de Ciencia de Datos

## Herramientas y tecnologías utilizadas

- **SQLite**: Motor de base de datos ligero y embebido. Se utiliza para almacenar la información de los libros de forma local y eficiente.
- **SQLAlchemy**: ORM (Object Relational Mapper) de Python que permite interactuar con la base de datos SQLite usando objetos y clases en lugar de SQL directo.
- **Streamlit**: Framework para construir interfaces web interactivas de manera sencilla y rápida en Python. Permite visualizar, buscar y agregar libros desde el navegador.
- **Pytesseract**: Wrapper de Python para Tesseract OCR. Se usa para extraer texto de imágenes de portadas de libros.
- **TensorFlow**: Biblioteca de machine learning utilizada para posibles extensiones de clasificación automática de género literario y procesamiento de imágenes.
- **Pillow** y **OpenCV**: Bibliotecas para procesamiento y manipulación de imágenes.
- **Pandas**: Para manipulación y visualización de datos tabulares en la interfaz.
- **RapidFuzz**: Biblioteca para realizar búsquedas aproximadas (fuzzy search), permitiendo encontrar libros aunque haya errores de tipeo o diferencias en tildes y mayúsculas/minúsculas.
- **unicodedata** (estándar de Python): Se usa para normalizar texto y facilitar búsquedas insensibles a tildes y mayúsculas.
- **pytest**: Herramienta para ejecutar pruebas unitarias y asegurar la calidad del código.

Estas herramientas permiten que la aplicación sea robusta, flexible y fácil de usar tanto para usuarios finales como para desarrolladores.

## Descripción

Este proyecto consiste en una aplicación de biblioteca digital desarrollada en Python. La aplicación permite a los usuarios buscar libros, agregar nuevos libros manualmente o mediante el escaneo de portadas, y almacenar toda la información en una base de datos SQLite utilizando SQLAlchemy como ORM. La interfaz de usuario está construida con Streamlit, y se utiliza Pytesseract junto con TensorFlow para extraer texto de las imágenes de las portadas de los libros.

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

```
biblioteca_digital/
├── app/
│   ├── __init__.py                # Inicializa el paquete de la aplicación
│   ├── main.py                    # Interfaz principal en Streamlit
│   ├── db.py                      # Configuración de la base de datos con SQLAlchemy
│   ├── crud.py                    # Funciones para manejar libros (CRUD)
│   ├── models.py                  # Modelos de datos con SQLAlchemy
│   ├── ocr.py                     # Lógica para reconocimiento de texto desde imagen
│   ├── create_tables.py           # Script para crear las tablas de la base de datos
│   ├── importar_desde_metadata.py # Script para importar libros desde Calibre (metadata.db)
│   ├── check_tables.py            # Script utilitario para inspeccionar tablas en la base de datos
├── data/
│   └── sample_cover.jpg           # Imagen de ejemplo para pruebas
├── tests/
│   ├── test_crud.py               # Pruebas unitarias para funciones de base de datos
│   ├── README.md                  # Documentación sobre los tests
├── .streamlit/
│   └── config.toml                # Configuraciones opcionales para Streamlit
├── biblioteca.db                  # Base de datos principal de la app
├── metadata.db                    # Base de datos de Calibre (opcional, para importar)
├── requirements.txt               # Lista de dependencias
├── README.md                      # Documentación principal del proyecto
```

## Instalación

Para instalar y ejecutar el proyecto, sigue estos pasos:

1. Clona el repositorio o descarga los archivos del proyecto:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd biblioteca_digital
   ```

2. Crea un entorno virtual:

   ```bash
   python -m venv venv
   ```

3. Activa el entorno virtual:

   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

5. Crea la base de datos y las tablas necesarias (solo la primera vez):

   ```bash
   cd app
   python create_tables.py
   cd ..
   ```

   Esto generará el archivo `biblioteca.db` en la raíz del proyecto con la estructura de tablas necesaria.

   Si ya tienes una base de datos existente y no quieres sobrescribirla, asegúrate de que el archivo `biblioteca.db` esté presente en la raíz antes de este paso.

6. (Opcional) Importa libros desde una biblioteca de Calibre:
   - Copia el archivo `metadata.db` de tu biblioteca de Calibre a la raíz del proyecto (`biblioteca_digital/metadata.db`).
   - Ejecuta:
     ```bash
     cd app
     python importar_desde_metadata.py
     cd ..
     ```
     Esto agregará los títulos y autores de Calibre a tu base de datos local.

## Uso

### Ejecutar la aplicación

Para ejecutar la aplicación, asegúrate de estar en la raíz del proyecto (`biblioteca_digital`) y utiliza el siguiente comando en la terminal:

```bash
streamlit run app/main.py
```

Esto abrirá la interfaz web de la biblioteca digital en tu navegador predeterminado.

## Funcionalidades

- Listado de libros con opciones de filtrado.
- Formulario para agregar nuevos libros.
- Subida de imágenes de portadas para extracción de texto mediante OCR.
- CRUD básico para gestionar libros en la base de datos.
- Pruebas unitarias para asegurar el correcto funcionamiento de las funciones.

## Pruebas

Para ejecutar los tests unitarios correctamente, asegúrate de estar en la raíz del proyecto (`biblioteca_digital`) y ejecuta:

```bash
PYTHONPATH=. pytest tests/test_crud.py
```

Esto garantiza que los imports funcionen correctamente y que las pruebas se ejecuten sobre el código de la aplicación.

## Extensiones Futuras

- Clasificación automática del género usando TensorFlow.
- Exportación de la base de datos a CSV o PDF.
- Sistema de login para usuarios.
- Estadísticas y gráficos sobre libros (por año, autor, género, etc.).

## Contribuciones

Las contribuciones son bienvenidas. Si deseas colaborar, por favor abre un issue o envía un pull request.
