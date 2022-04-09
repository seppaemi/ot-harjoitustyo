from entities.item import Item
from entities.user import User
from repositories.item_repository import( ItemRepository as default_item_repository)
from repositories.user_repository import (user_repository as default_user_repository)

class InvalidCredentialsError(Exception):
    pass

class UsernameExistsError(Exception):
    pass

class Service:
    def __init__(self, ItemRepository=default_item_repository, user_repository=default_user_repository):

        self._user = None
        self._todo_repository = ItemRepository
        self._user_repository = user_repository
        
    def login(self, username, password):
        user = self._user_repository.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError('Username or password is incorrect. Please try again or create and account.')
        self._user = user
        return user

    def get_current_user(self):
        return self._user

    def get_users(self):
        return self._user_repository.find_all()

    def logout(self):
        self._user = None

    def create_user(self, username, password, login=True):
        username_reserved = self._user_repository.find_by_username(username)
        if username_reserved:
            raise UsernameExistsError(f'Username {username} already exists')
        user = self._user_repository.create(User(username, password))
        if login:
            self._user = user
        return user


service = Service()
