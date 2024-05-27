# services/document_upload_service.py
# Define a service to handle document uploads. Save the uploaded document and return its ID.
import uuid
from models.document import Document

def upload_document(file):
    document_id = str(uuid.uuid4())
    document = Document(id=document_id, content=file.read())
    document.save()
    return document_id
