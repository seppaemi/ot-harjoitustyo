"""user repo"""
from entities.user import User
from database_connection import get_db_connection


def get_user_by_row(row):
    """hakee käyttäjän"""
    return User(row['username'], row['password']) if row else None


class UserRepository:
    """Luokka joka vastaa käyttäjiin liittyvistä tietokantaoperaatioista."""

    def __init__(self, connection):
        """Luokan konstruktori
        """

        self._connection = connection

    def create_user(self, user):
        """tallentaa uuden käyttäjän tietokantaan.
        """

        cursor = self._connection.cursor()

        cursor.execute('INSERT INTO users (username, password) values (?, ?)',
                       [user.username, user.password])

        self._connection.commit()
        cursor.close()

        return user

    def find_by_username(self, username):
        """palauttaa käyttäjän käyttäjätunnuksen
           perusteella
        """

        cursor = self._connection.cursor()

        cursor.execute('SELECT * FROM users WHERE username = ?', [username])

        row = cursor.fetchone()
        cursor.close()

        return get_user_by_row(row)

    def delete_all(self):
        """poistaa kaikki käyttäjät"""

        cursor = self._connection.cursor()

        cursor.execute('DELETE FROM users')

        self._connection.commit()
        cursor.close()


user_repository = UserRepository(get_db_connection())
