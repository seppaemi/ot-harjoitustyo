"""entities luokka
"""


class Item:
    """Luokka, joka kuvaa yksittäistä käyttäjän lisäämää tuotetta
     Attributes:
        amount: String, määrä tai lisäinfo tuotteesta
        item: String, tuote
        category: String, kategoria
        user_id: int, tuotteen järjestelmään lisänneen käyttäjän id
    """

    def __init__(self, amount, item, category, user_id=None):
        """Konstruktori, luo uuden tuoteen
        Args:
            amount: String, määrä tai lisäinfo tuotteesta
            item: String, tuote
            category: String, kategoria
            user_id: int, tuotteen järjestelmään lisänneen käyttäjän id
        """
        self.amount = amount
        self.item = item
        self.category = category
        self.user_id = user_id

    def set_user_id(self, user_id):
        """Mahdollistaa user_id:n asettamisen tuotteen alustamisen jälkeen
        Args:
            id: Salasanalle asetettava user_id
        """
        self.user_id = user_id
