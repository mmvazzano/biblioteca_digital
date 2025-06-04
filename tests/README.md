# Pruebas unitarias de la Biblioteca Digital

Este directorio contiene los tests automáticos para la aplicación de Biblioteca Digital.

## ¿Qué se prueba?

El archivo `test_crud.py` verifica el correcto funcionamiento de las operaciones básicas sobre la base de datos (CRUD):

- **Crear libro:** Se prueba que se puede crear un libro y que los datos guardados coinciden con los proporcionados.
- **Obtener libros:** Se comprueba que la función para obtener libros devuelve resultados (al menos el libro creado).
- **Eliminar libro:** Se verifica que se puede eliminar un libro y que, tras la eliminación, ya no aparece en la base de datos.

Estas pruebas ayudan a asegurar que la lógica principal de la aplicación funciona correctamente y que no hay errores en las operaciones básicas sobre los libros.

## ¿Cómo ejecutar los tests?

Desde la raíz del proyecto (`biblioteca_digital`), ejecuta:

```bash
PYTHONPATH=. pytest tests/test_crud.py
```

Esto garantiza que los imports funcionen correctamente y que las pruebas se ejecuten sobre el código de la aplicación.
