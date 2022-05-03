"""servicelle
"""
from repositories.item_repository import (item_repository as item_repository)
from repositories.user_repository import (user_repository as user_repository)


class InvalidCredentialsError(Exception):
    """pass
    """
    pass


class UsernameExistsError(Exception):
    """pass
    """
    pass


class Service:
    """Luokka joka vastaa sovelluslogiikasta."""

    def __init__(self, user_repository=user_repository,
                 item_repository=item_repository):
        """Luokan konstruktori
        """

        self._user = None
        self._user_repository = user_repository
        self._item_repository = item_repository

    def login_user(self, user):
        """Kirjaa käyttäjän järjestelmään
        Args:
            user: User-olio, jolla käyttäjä kirjataan sisään
        Returns
            Palauttaa User-olion, joka kirjataan järjestelmään
        """
        self.user = self._user_repository.login_user(user)

        return self.user

    def get_user(self, user):
        """Hakee halutun käyttäjän tietokannasta
        Args:
            user: User-olio, joka etsitään tietokannasta
        Returns:
            Palauttaa User-olion, jos käyttäjä löytyy tietokannasta
            tai None, jos käyttäjää ei löydy
        """
        user_by_username = self._user_repository.get_single_user(user)

        return user_by_username

    def create_user(self, user):
        """Luo uuden käyttäjän järjestelmään
        Args:
            user: User-olio joka lisätään järjestelmään
        Returns:
            Palauttaa lisätyn User-olion
            Jos käyttäjä löytyy jo järjestelmästä tai User-olio on puutteellinen
            palautetaan None
        """
        if self.get_user(user):
            return None
        if not user.username or not user.password:
            return None
        if len(user.username) > 10:
            return None
        if len(user.password) > 20:
            return None

        new_user = self._user_repository.create_user(user)

        return new_user

    def get_items_by_user(self, user):
        """Hakee tietyn käyttäjän järjestelmään lisäämät tuotteet
        Args:
            user: User-olio, jonka lisäämät tuotteet halutaan hakea
        Returns:
            Halutun käyttäjän lisäämät tuotteet listamuodossa
        """
        items = self._item_repository.get_all_items_by_user(user)

        return items

    def add_new_items(self, item):
        """Lisää uuden tuotteen järjestelmään
        Args:
            item: Item-olio, jonka käyttäjä haluaa lisätä järjestelmään
        Returns
            Palauttaa lisätyn Item-olion
        """
        added_item = self._item_repository.create_item(item)

        return added_item

    def delete_item(self, item):
        """poistaa tuotteita"""
        pass

    def delete_everything(self):
        """Luokan metodi, joka tyhjentää koko tietokannan."""

        self._user_repository.delete_all()
        self._item_repository.delete_all_items()
