# services/translation_service.py
# Define a service to handle document translation using a Large Language Model (LLM).
# It should detect the source language, translate the text, and save the translation metadata.
from utils.language_detection import detect_language
from models.document import Document
from models.translation_metadata import TranslationMetadata
from some_llm_library import LargeLanguageModel

llm = LargeLanguageModel()

def translate_document(document_id, target_language):
    document = Document.get(document_id)
    source_language = detect_language(document.content)
    translated_text = llm.translate(document.content, source_language, target_language)
    
    translation_metadata = TranslationMetadata(
        document_id=document_id,
        source_language=source_language,
        target_language=target_language,
        translated_text=translated_text
    )
    translation_metadata.save()

    return translation_metadata.id
