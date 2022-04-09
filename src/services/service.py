from entities.user import User
from entities.item import Item
from repositories.user_repository import (user_repository as default_user_repo)
from repositories.item_repository import (item_repository as default_item_repo)

class UsernameExistsError(Exception):
    pass
class UsernameNotValidError(Exception):
    pass
class PasswordNotValidError(Exception):
    pass
class InvalidCredentialsError(Exception):
    pass

class Service:
    def __init__(self, user_repository=default_user_repo, item_repository=default_item_repo):
        self._user = None
        self._user_repository = user_repository
        self._item_repository = item_repository

    def create_user(self, username, password):
        existing_user = self._user_repository.find_by_username(username)

        if existing_user is not None:
            raise UsernameExistsError(f'Username {username} already exists')
        if len(username) < 3 or len(username) > 15:
            raise UsernameNotValidError("Username must be 3 to 15 characters long")
        if len(password) < 3 or len(password) > 15:
            raise PasswordNotValidError("Password must be 3 to 15 characters long")

        user = self._user_repository.create_user(User(username, password))
        self._user = user
        return user

    def login(self, username, password):
        user = self._user_repository.find_by_username(username)

        if user is None or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")
        self._user = user

        return user

    def logout(self):
        self._user = None

    def get_current_user(self):
        return self._user
##tÄSTÄ ETEENPÄIN EI MITÄÄN HAJUA TOIMIIKO :D
    
    def add_item(self, item):
        user = self.get_current_user()
        item = Item(item)

        self._item_repository.add_item(item, user)
        return item

    def delete_item(self, item):
        user = self.get_current_user()
        self._item_repository.delete_item(item, user)

    def find_items(self):
        user = self.get_current_user()
        items = self._item_repository.find_by_user(user)

        result = []
        for item in items:
            result.append(item)

        result.sort()
        return result

    def delete_all(self):
        self._user_repository.delete_all()
        self._item_repository.delete_all()

service = Service()
