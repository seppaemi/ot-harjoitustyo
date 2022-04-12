"""repo kaikille tuotteille, tämä ei toimi vielä :)
"""
from database_connection import get_db_connection

def get_id_by_row(row):
    """hakee id:n"""
    return row['id'] if row else None

def get_name_by_row(row):
    """hakee nimen"""
    return row['item'] if row else None



class ItemRepository:
    """ostoksista vastaava luokka
    """
    def __init__(self, connection):
        """luokan konstruktori
        """
        self._connection = connection

    def _get_user_id(self, user):
        """palauttaa käyttäjän id:n
        """
        cursor = self._connection.cursor()
        row = cursor.execute("SELECT * FROM Users WHERE username=?", [user.username]).fetchone()
        user_id = get_id_by_row(row)
        cursor.close()

        return user_id

    def add_item(self, item, user):
        """lisää tuotteen tietokantaan
        """
        user_id = self._get_user_id(user)
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO Items (item, user_id) VALUES (?, ?)",[item.item, user_id])

        cursor.execute("SELECT * FROM Items WHERE item=? AND user_id=?",(item.item, user_id))
        self._connection.commit()
        cursor.close()

        return item

    def delete_item(self, item, user):
        """poistaa tuotteen tietokannasta
        """
        user_id = self._get_user_id(user)
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM Items WHERE item=? AND user_id=?",(item, user_id))
        row = cursor.fetchone()

        item_id = get_id_by_row(row)
        cursor.execute("DELETE FROM Items WHERE id=?", [item_id])
        self._connection.commit()
        cursor.close()

    def find_by_user(self, user):
        """etsii tuotteita tietokannasta
        käyttäjän avulla
        """
        user_id = self._get_user_id(user)
        cursor = self._connection.cursor()
        items = cursor.execute("SELECT * FROM Items WHERE user_id=?", [user_id]).fetchall()
        cursor.close()

        result = []
        for row in items:
            result.append((get_name_by_row(row)))

        return result


    def delete_all(self):
        """poistaa kaiken
        """
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM Items")
        self._connection.commit()
        cursor.close()

item_repository = ItemRepository(get_db_connection())
