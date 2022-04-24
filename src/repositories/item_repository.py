"tuotteiden tietokannat"
from database_connection import get_db_connection


def get_id_by_row(row):
    """hakee id:n"""
    return row['id'] if row else None


def get_name_by_row(row):
    """hakee tuotteen"""
    return row['item'] if row else None


class ItemRepository:
    """tuotteiden tietokantaluokka"""

    def __init__(self, connection):
        """Luokan konstruktori.
        Args:
            connection: Connection-olio, joka kuvaa tietokantayhteyttä
        """

        self._connection = connection

    def _get_user_id(self, user):
        """palauttaa käyttäjän id:n
        """

        cursor = self._connection.cursor()

        row = cursor.execute(
            "SELECT * FROM users WHERE username=?", [user.username]).fetchone()

        user_id = get_id_by_row(row)

        cursor.close()

        return user_id

    def add_item(self, item, user):
        """lisää tuotteita"""
        user_id = self._get_user_id(user)

        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO Items (item, user_id) VALUES (?, ?)",
            [item.item, user_id])

        cursor.execute(
            "SELECT * FROM Items WHERE item=? AND user_id=?",
            (item.item, user_id))

        self._connection.commit()
        cursor.close()

        return item

    def delete_items(self, item, user):
        """poistaa tuotteita"""
        user_id = self._get_user_id(user)

        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM Items WHERE item=? AND user_id=?",
            (item, user_id))

        row = cursor.fetchone()

        item_id = get_id_by_row(row)

        cursor.execute("DELETE FROM Items WHERE id=?", [item_id])

        self._connection.commit()
        cursor.close()

    def find_by_user(self, user):
        """etsii tuotteet käyttäjän perusteella"""
        user_id = self._get_user_id(user)

        cursor = self._connection.cursor()

        items = cursor.execute(
            "SELECT * FROM Items WHERE user_id=?", [user_id]).fetchall()

        cursor.close()

        result = []
        for row in items:
            result.append((get_name_by_row(row)))

        return result

    def delete_all(self):
        """Luokan metodi, joka poistaa kaikki reseptit ja ainekset."""

        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM Items")

        self._connection.commit()
        cursor.close()


item_repository = ItemRepository(get_db_connection())
