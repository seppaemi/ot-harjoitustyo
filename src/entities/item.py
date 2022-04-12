"""entities luokka
"""
class Item:
    """ kuvaa luokassa yksittäistä ostosta
    """
    def __init__(self, item, user, item_id):
        """item on tuote merkijonona
        user on käyttäjä
        item id on tuotteen id"""
        self.item=item
        self.user=user
        self.item_id=item_id
        