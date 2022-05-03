"""Testausta
"""
import unittest
from entities.user import User
from repositories.user_repository import user_repository


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user1 = User('user1', 'abc123')

    def test_create_user_returns_user(self):
        self.assertEqual(user_repository.create_user(
            self.user1), self.user1)

    def test_get_single_user(self):
        user_repository.create_user(self.user1)
        user = user_repository.get_single_user(self.user1)
        self.assertEqual(user.username, self.user1.username)
