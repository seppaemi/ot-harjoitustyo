"""repo käyttäjille
"""
from entities.user import User
from database_connection import get_db_connection

def get_user_by_row(row):
    """palauttaa käyttäjän
    """
    return User(row['username'], row['password']) if row else None


class UserRepository:
    """Käyttäjiin liittyvistä tietokantaoperaatioista vastaava luokka.
    """
    def __init__(self, connection):
        """luokan konstruktori
        """
        self._connection = connection

    def find_all(self):
        """etsii ja palauttaa kaikki käyttäjät
        """
        cursor = self._connection.cursor()
        cursor.execute('select * from users')
        rows = cursor.fetchall()
        return list(map(get_user_by_row, rows))

    def find_by_username(self, username):
        """etsii ja palauttaa käyttäjän, tunnuksen perusteella
        """
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from users where username = ?',
            (username,)
        )
        row = cursor.fetchone()
        return get_user_by_row(row)

    def create(self, user):
        """tallentaa käyttäjän tietokentaan
        """
        cursor = self._connection.cursor()
        cursor.execute(
            'insert into users (username, password) values (?, ?)',
            (user.username, user.password)
        )
        self._connection.commit()
        return user

    def delete_user(self, username):
        """poistaa tietyn käyttäjän
        """
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users WHERE username= ?", [username])
        return "User deleted"

    def delete_all(self):
        """poistaa kaiken
        """
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")
        self._connection.commit()

user_repository = UserRepository(get_db_connection())
