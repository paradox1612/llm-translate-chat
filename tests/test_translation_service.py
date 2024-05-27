# tests/test_translation_service.py
# Write unit tests for the translation service.
import unittest
from services.translation_service import translate_document

class TestTranslationService(unittest.TestCase):
    def test_translate_document(self):
        document_id = "sample_document_id"
       
