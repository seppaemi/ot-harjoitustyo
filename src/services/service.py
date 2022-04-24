"""servicelle
"""
from entities.user import User
from entities.item import Item
from repositories.item_repository import( item_repository as default_item_repository)
from repositories.user_repository import (user_repository as default_user_repository)

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

    def __init__(self, default_user_repository=default_user_repository,
     default_item_repository=default_item_repository):
        """Luokan konstruktori
        """

        self._user = None
        self._user_repository = default_user_repository
        self._item_repository = default_item_repository

    def create_user(self, username, password):
        """luo uuden käyttäjän ja kirjaa sen samalla sisään
        """

        existing_user = self._user_repository.find_by_username(username)

        if existing_user is not None:
            raise UsernameExistsError(f'Username {username} is already in use')

        user = self._user_repository.create_user(User(username, password))

        self._user = user

        return user

    def login(self, username, password):
        """kirjaa käyttäjän sisään.
        """

        user = self._user_repository.find_by_username(username)

        if user is None or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user

        return user

    def logout(self):
        """kirjaa nykyisen käyttäjän ulos."""

        self._user = None

    def get_current_user(self):
        """palauttaa kirjautuneen käyttäjän.
        """

        return self._user

    def add_item(self, item):
        """lisää tuotteita"""
        user = self.get_current_user()
        item = Item(item)

        self._item_repository.add_item(item, user)
        return item

    def delete_item(self, item):
        """poistaa tuotteita"""
        user = self.get_current_user()
        self._item_repository.delete_items(item, user)

    def find_items(self):
        """etsii tuotteita"""
        user = self.get_current_user()

        items = self._item_repository.find_by_user(user)

        result = []
        for item in items:
            result.append(item)

        result.sort()
        return result

    def delete_everything(self):
        """Luokan metodi, joka tyhjentää koko tietokannan."""

        self._user_repository.delete_all()
        self._item_repository.delete_all()


service = Service()
