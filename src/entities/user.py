""" entities luokka
"""

class User:
    """Luokka, joka kuvaa yksittäistä käyttäjää
    """
    def __init__(self, username, password, user_id = None):
        """Konstruktori, luo uuden käyttäjän
        """
        self.username = username
        self.password = password
        self.user_id = user_id

    def set_user_id(self, id):
        """Mahdollistaa user_id:n asettamisen käyttäjän alustamisen jälkeen
        """
        self.user_id = id
