"tuotteiden tietokannat"
from database_connection import get_db_connection
from entities.item import Item


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

    def tuple_to_item(self, item):
        """Apufunktio, joka muuttaa tuple-syötteen Item-olioksi
        Args:
            item: Tuple, joka sisältää halutun Item-olion kentät
        Returns:
            Item-olio, joka muodostetaan parametristä item
        """
        if not item:
            return None

        item_to_return = Item(item[1], item[2], item[3])
        item_to_return.set_user_id(item[4])

        return item_to_return

    def get_all_items_by_user(self, user):
        """Palauttaa halutun käyttäjän lisäämät tuotteet
        Args:
            user: User-olio, jonka lisäämät tuotteet haetaan
        Returns:
            Palauttaa halutun käyttäjän lisäämät tuotteet listamuodossa
        """
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM Items WHERE user_id = ?',
                       (user.user_id,))
        fetch_items = cursor.fetchall()
        fetch_items = map(self.tuple_to_item, fetch_items)

        return list(fetch_items)

    def get_all_items(self):
        """Palauttaa kaikki järjestelmään lisätyt tuotteet
        Returns:
            Palauttaa kaikki järjestelmään lisätyt tuotteet listamuodossa
        """
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM Items')
        fetch_items = cursor.fetchall()
        fetch_items = map(self.tuple_to_item, fetch_items)

        return list(fetch_items)

    def create_item(self, item):
        """Lisää järjestelmään halutun tuotteen
        Args:
            item: Item-olio, joka halutaan lisätä järjestelmään
        Returns:
            Palauttaa luodun Item-olion
        """
        cursor = self._connection.cursor()
        cursor.execute('''INSERT INTO Items (item, category, amount, user_id)
                        VALUES (?, ?, ?, ?)''', (item.item, item.category,
                        item.amount, item.user_id))

        self._connection.commit()
        return item

    def delete_all_items(self):
        """POISTAA KAIKKI JÄRJESTELMÄÄN LISÄTYT TUOTTEET"""
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM Items')
        self._connection.commit()

    def delete_item(self, item):
        """poistaa tuotteen"""
        pass


item_repository = ItemRepository(get_db_connection())
