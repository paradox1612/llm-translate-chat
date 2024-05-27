# services/document_processing_service.py
# Define a service for pre-processing documents, including OCR for images and formatting for text documents.
from utils.ocr import perform_ocr

def preprocess_document(file_content, file_type):
    if file_type == 'image':
        text_content = perform_ocr(file_content)
    else:
        text_content = file_content.decode('utf-8')
    return text_content
