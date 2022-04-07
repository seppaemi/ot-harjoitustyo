
class User:
    """Luokka, joka kuvaa käyttäjää.
    Attributes:
        username: Merkkijono käyttäjän käyttäjätunnuksesta.
        password: Merkkijono käyttäjän salasanasta.
    """
    def __init__(self, username:str, password: str):
        """Tämä luo uuden käyttäjän.
        Args:
            username: Merkkijono käyttäjätunnuksesta.
            password: Merkkijono salasanasta.
        """
        self.username=username
        self.password=password

