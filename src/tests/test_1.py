
import unittest
from entities.user import User
from repositories.user_repository import user_repository


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.repo = user_repository
        self.repo.delete_all()
        self.user = User("user1", "abc123")

    def test_create_user(self):
        new_user = self.repo.create(self.user)
        self.assertEqual(new_user, new_user)

    def test_find_user(self):
        self.repo.create(self.user)
        user = self.repo.find_by_username(self.user.username)
        self.assertEqual(user, user)

    def test_find_all(self):
        self.repo.create(self.user)
        users = self.repo.find_all()
        amount = len(users)
        self.assertEqual(amount, 1)

    def test_delete_user(self):
        self.repo.create(self.user)
        delete = self.repo.delete_user(self.user.username)
        self.assertEqual(delete, delete)

    def test_delete_all_users(self):
        self.repo.create(self.user)
        delete = self.repo.delete_all()
        self.assertEqual(delete, None)
        