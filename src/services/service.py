"""servicelle
"""
from entities.user import User
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
    """luokka
    """
    def __init__(self, item_repository=default_item_repository,
        user_repository=default_user_repository):
        """alustaa tarvittavat
        """
        self._user = None
        self._todo_repository = item_repository
        self._user_repository = user_repository

    def login(self, username, password):
        """kirjautumissivu
        """
        user = self._user_repository.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError(
                'Username or password is incorrect. Please try again or create and account.'
            )
        self._user = user
        return user

    def get_current_user(self):
        """palauttaa krijautuneen käyttäjän
        """
        return self._user

    def get_users(self):
        """palauttaa kaikki käyttäjät
        """
        return self._user_repository.find_all()

    def logout(self):
        """Kirjaa käyttäjän ulos
        """
        self._user = None

    def create_user(self, username, password, login=True):
        """luo käyttäjän
        """
        username_reserved = self._user_repository.find_by_username(username)
        if username_reserved:
            raise UsernameExistsError(f'Username {username} already exists')
        user = self._user_repository.create(User(username, password))
        if login:
            self._user = user
        return user

service = Service()
