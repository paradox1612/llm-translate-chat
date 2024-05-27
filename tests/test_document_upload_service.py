# tests/test_document_upload_service.py
# Write unit tests for the document upload service.
import unittest
from services.document_upload_service import upload_document

class TestDocumentUploadService(unittest.TestCase):
    def test_upload_document(self):
        with open('test_document.txt', 'rb') as file:
            document_id = upload_document(file)
            self.assertIsNotNone(document_id)

if __name__ == '__main__':
    unittest.main()
