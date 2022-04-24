import unittest
from repositories.item_repository import item_repository
from repositories.user_repository import user_repository
from entities.item import Item
from entities.user import User


class TestItemRepository(unittest.TestCase):
    def setUp(self):
        item_repository.delete_all()
        user_repository.delete_all()

        self.user1 = User('user1', 'abc123')
        self.user2 = User('user2', 'xyz987')

        self.milk = Item('milk')
        self.bananas = Item('bananas')
        self.fries = Item('fries')

    def test_add_item_returns_item(self):
        user_repository.create_user(self.user1)
        self.assertEqual(item_repository.add_item(
            self.bananas, self.user1), self.bananas)

    def test_add_items_inserts_into_items_database(self):
        user_repository.create_user(self.user1)
        self.assertEqual(item_repository.find_by_user(
            self.user1), [])
        item_repository.add_item(self.bananas, self.user1)
        self.assertEqual(item_repository.find_by_user(
            self.user1), [('bananas')])

    def test_find_items_returns_correct_ones(self):
        user_repository.create_user(self.user1)
        item_repository.add_item(self.milk, self.user1)
        item_repository.add_item(self.bananas, self.user1)

        self.assertEqual(item_repository.find_by_user(
            self.user1), [('milk'), ('bananas')])

    def test_delete_item(self):
        user_repository.create_user(self.user1)
        item_repository.add_item(self.milk, self.user1)
        item_repository.add_item(self.bananas, self.user1)
        item_repository.delete_items('milk', self.user1)

        self.assertEqual(item_repository.find_by_user(
            self.user1), [('bananas')])

    def test_delete_item_doesnt_remove_it_from_others(self):
        user_repository.create_user(self.user1)
        item_repository.add_item(self.milk, self.user1)
        item_repository.add_item(self.bananas, self.user1)

        user_repository.create_user(self.user2)
        item_repository.add_item(self.milk, self.user2)
        item_repository.add_item(self.bananas, self.user2)
        item_repository.delete_items('bananas', self.user2)

        self.assertEqual(item_repository.find_by_user(
            self.user1)[0], ('milk'))

