# services/storage_service.py
# Define a service for storing and retrieving documents and audio files from a storage backend.
from models.document import Document
from models.audio_file import AudioFile

def save_document(document):
    document.save()

def retrieve_document(document_id):
    return Document.get(document_id)

def save_audio_file(audio_file):
    audio_file.save()

def retrieve_audio_file(audio_id):
    return AudioFile.get(audio_id)
