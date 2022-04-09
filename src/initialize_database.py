
from database_connection import get_db_connection

def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''drop table if exists users;''')
    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY,username TEXT,password TEXT);''')
    connection.commit()

def initialize_database():
    connection = get_db_connection()
    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()