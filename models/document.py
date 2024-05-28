# models/document.py
# Define the Document model with fields for ID and content. Include methods to save and retrieve documents.
from database import Database
from utils import logging
import psycopg2
class Document:
    def __init__(self, id, content):
        self.id = id
        self.content = content
        self.databse= Database(host="192.168.1.10",
                port="5432",
                user="postgres",
                password="Kush_1997",
                db_name="LLM")
        self.logger = logging.configure_logging()

    def save(self):
        
        try:
            connection = self.databse
            connection.connect()
            
            connection.create_table("documents", "id SERIAL PRIMARY KEY, content TEXT, document_id INTEGER")
            
            connection.insert_data("documents", "content, translation_id", (self.content,self.id))
            
            self.logger.info(self.logger, "Document saved successfully: document_id=%s", self.id)
            connection.disconnect()
        except psycopg2.Error as e:
            print("Error connecting to PostgreSQL database:", e)
            self.logger.error(self.logger, "Error saving document: document_id=%s Error =%s", self.id,e)

    @staticmethod
    def get(document_id):
        # Implement retrieval logic from a database or storage backend
        pass
