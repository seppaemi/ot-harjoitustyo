
from entities.user import User
from database_connection import get_db_connection

def get_user_by_row(row):
    return User(row['username'], row['password']) if row else None

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute('INSERT INTO Users (username, password) values (?, ?)',[user.username, user.password])
        self._connection.commit()
        cursor.close()

        return user

    def find_by_username(self, username):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM Users WHERE username = ?', [username])
        row = cursor.fetchone()
        cursor.close()

        return get_user_by_row(row)

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM Users')
        self._connection.commit()
        cursor.close()

user_repository = UserRepository(get_db_connection())
