""" entities luokka
"""
class User:
    """Luokka yksittäisestä käyttäjästä
    Attributes:
        username: käyttäjätunnis merkkijonona
        password: salasana merkkijonona
    """

    def __init__(self, username, password):
        """Luokan konstruktori: luo käyttäjän
        Args:
            username: käyttäjätunnus merkkijonona
            password: salasana merkkijonona
        """

        self.username = username
        self.password = password
