"""entities luokka
"""


class Item:
    """Luokka, joka kuvaa yksittäistä käyttäjän lisäämää tuotetta
    """

    def __init__(self, amount, item, category, user_id=None):
        """Konstruktori, luo uuden tuoteen
        """
        self.amount = amount
        self.item = item
        self.category = category
        self.user_id = user_id

    def set_user_id(self, user_id):
        """Mahdollistaa user_id:n asettamisen tuotteen alustamisen jälkeen
        """
        self.user_id = user_id
