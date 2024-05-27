# utils/ocr.py
# Define a utility function to perform OCR on image files.
import pytesseract

def perform_ocr(image_content):
    return pytesseract.image_to_string(image_content)
