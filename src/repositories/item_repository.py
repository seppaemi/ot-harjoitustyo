from entities.item import Item
from entities.user import User
from database_connection import get_db_connection
def get_id_by_row(row):
    return row['id'] if row else None

def get_name_by_row(row):
    return row['name'] if row else None

class ShoppinglistRepository:
    def __init__(self, connection):
        self._connection = connection

    def _get_user_id(self, user):
        #palauttaa käyttäjän id numeron
        cursor = self._connection.cursor()
        row = cursor.execute("SELECT * FROM Users WHERE username=?", [user.username]).fetchone()
        user_id = get_id_by_row(row)
        cursor.close()
        return user_id

    def add_item(self, item, user):
        #tallentaa uusen ostoksen titokantaan
        user_id = self._get_user_id(user)
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO Items (name, user_id) VALUES (?, ?)",
            [Item.name, user_id])

        row = cursor.fetchone()
        self._connection.commit()
        cursor.close()
        return item

    def delete_item(self, item, user):
        #poistaa tuotteen tietokannasta
        user_id = self._get_user_id(user)
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Items WHERE name=? AND user_id=?",(item, user_id))
        row = cursor.fetchone()
        item_id = get_id_by_row(row)

        cursor.execute("DELETE FROM Items WHERE item_id=?", [item_id])
        cursor.execute("DELETE FROM Items WHERE id=?", [item_id])

        self._connection.commit()
        cursor.close()

    def find_items_by_user(self, user, category=None):
        #etsii kikkien käyttäjän tallentamien tuotteiden nimet
        user_id = self._get_user_id(user)
        cursor = self._connection.cursor()
        items = cursor.execute("SELECT * FROM Items WHERE user_id=?",[user_id]).fetchall()

        cursor.close()
        result = []
        for row in items:
            result.append((get_name_by_row(row)))
        return result

    def delete_all(self):
        #luokan metodi joka poistaa kaikki tuotteet
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM Items")

        self._connection.commit()
        cursor.close()


recipe_repository = ShoppinglistRepository(get_db_connection())