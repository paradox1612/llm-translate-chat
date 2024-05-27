# tests/test_document_processing_service.py
# Write unit tests for the document processing service.
import unittest
from services.document_processing_service import preprocess_document

class TestDocumentProcessingService(unittest.TestCase):
    def test_preprocess_text_document(self):
        file_content = b"Hello, world!"
        file_type = 'text'
        result = preprocess_document(file_content, file_type)
        self.assertEqual(result, "Hello, world!")

    def test_preprocess_image_document(self):
        file_content = b""  # Add sample image bytes here
        file_type = 'image'
        result = preprocess_document(file_content, file_type)
        self.assertIsNotNone(result)  # Assuming OCR will extract some text

if __name__ == '__main__':
    unittest.main()
