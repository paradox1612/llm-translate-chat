# services/output_service.py
# Define a service to handle the output of translated documents and generated audio files.
# It should provide functionality to download these files.
from models.document import Document
from models.audio_file import AudioFile

def get_translated_document(document_id):
    document = Document.get(document_id)
    return document.translated_content

def get_audio_file(audio_id):
    audio_file = AudioFile.get(audio_id)
    return audio_file.content
