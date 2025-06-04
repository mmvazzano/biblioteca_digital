from PIL import Image
import pytesseract
import cv2
import numpy as np

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Aplicar un umbral para binarizar la imagen
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    return thresh

def extract_text_from_image(image_path):
    processed_image = preprocess_image(image_path)
    text = pytesseract.image_to_string(processed_image, lang='eng')
    return text

def extract_book_info(image_path):
    text = extract_text_from_image(image_path)
    # Aquí se pueden agregar más lógica para extraer título, autor, etc. del texto
    return text.strip()  # Retornar el texto extraído limpio