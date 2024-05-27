import psycopg2
import logging
from utils import logging

class Database:
    def __init__(self, db_name, user, password, host, port):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        self.connection = psycopg2.connect(
            dbname=self.db_name,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        logging.info("Connected to the database.")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            logging.info("Disconnected from the database.")

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            self.connection.commit()
        logging.info(f"Table '{table_name}' created.")

    def insert_data(self, table_name, columns, values):
        placeholders = ', '.join(['%s'] * len(values))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
            self.connection.commit()
        logging.info(f"Data inserted into '{table_name}'.")

    def select_data(self, table_name, condition=None):
        query = f"SELECT * FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
        logging.info(f"Selected data from '{table_name}'.")
        return rows

    def update_data(self, table_name, set_values, condition=None):
        query = f"UPDATE {table_name} SET {set_values}"
        if condition:
            query += f" WHERE {condition}"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            self.connection.commit()
        logging.info(f"Data updated in '{table_name}'.")

    def delete_data(self, table_name, condition=None):
        query = f"DELETE FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            self.connection.commit()
        logging.info(f"Data deleted from '{table_name}'.")

# Example usage:
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    db = Database(db_name="LLM", user="postgres", password="Kush_1997", host="192.168.1.10", port="5432")
    db.connect()
    
    # Example table creation
    db.create_table("test_table", "id SERIAL PRIMARY KEY, name VARCHAR(100), age INT")
    
    # Example data insertion
    db.insert_data("test_table", "name, age", ("John Doe", 30))
    
    # Example data selection
    rows = db.select_data("test_table")
    print(rows)
    
    # Example data update
    db.update_data("test_table", "age = 31", "name = 'John Doe'")
    
    # Example data deletion
    db.delete_data("test_table", "name = 'John Doe'")
    
    db.disconnect()
