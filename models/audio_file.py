import psycopg2
from utils import logging
from database import Database
# models/audio_file.py
# Define the AudioFile model with fields for translation ID, content, and format.
# Include methods to save and retrieve audio files.
class AudioFile:
    def __init__(self, translation_id, content, format):
        self.translation_id = translation_id
        self.content = content
        self.format = format
        self.logger = logging.configure_logging()
        self.databse= Database(host="192.168.1.10",
                port="5432",
                user="postgres",
                password="Kush_1997",
                db_name="LLM")

    def save(self):
        
        # Establish a connection to the PostgreSQL database
        try:
            connection = self.databse
            connection.connect()
            
            # Create a cursor object to interact with the database
            
            # Execute query to insert audio data into database table name audio_files
            # create a table if does not exist in your database with the following schema
            connection.create_table("audio_files", "audio_id SERIAL PRIMARY KEY, translation_id INTEGER, content text, format VARCHAR(255)")
            
            # CREATE TABLE audio_files ( 
            connection.insert_data("audio_files", "translation_id, content, format", (self.translation_id, self.content, self.format))
            
            logging.info(self.logger, "Audio file saved successfully: translation_id=%s, format=%s", self.translation_id, self.format)
            connection.disconnect()
        except psycopg2.Error as e:
            print("Error connecting to PostgreSQL database:", e)

    @staticmethod
    def get(audio_id):
        # Implement retrieval logic from a database or storage backend
        try:
            connection = psycopg2.connect(
                host="192.168.1.10",
                port="5432",
                user="postgres",
                password="Kush_1997",
                database="LLM"
            )
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM audio_files WHERE audio_id = %s", (audio_id,))
            audio_data = cursor.fetchone()
            connection.close()
            return audio_data
        except psycopg2.Error as e:
            print("Error connecting to PostgreSQL database:", e)
            return None
        
