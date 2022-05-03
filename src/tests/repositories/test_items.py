import unittest
from repositories.item_repository import item_repository
from repositories.user_repository import user_repository
from entities.item import Item
from entities.user import User


class TestItemRepository(unittest.TestCase):
    def setUp(self):
        item_repository.delete_all_items()
        user_repository.delete_all()

        self.user1 = User('user1', 'abc123')
        self.user2 = User('user2', 'xyz987')

        self.milk = Item('milk', 'fruit', '124')
        self.bananas = Item('bananas', 'fruit', '2345678i')
        self.fries = Item('fries', 'freezer', '34')

    def test_create_item(self):
        item_repository.create_item(self.bananas)
        items = item_repository.get_all_items()

        self.assertEqual(len(items), 1)


"""täältä puuttuu vielä muutama testi :)"""
