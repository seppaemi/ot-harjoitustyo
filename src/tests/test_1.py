
import unittest
from repositories.user_repository import UserRepository
from entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.ur = UserRepository("users.db")
        self.ur.create_table()
        self.ur.delete_table()
        self.user1 = User('emilia', 'emilia123')

    def test_create(self):
        self.ur.create_table()
        self.ur.create_user(self.user1)
        all = self.ur.find_users()
        self.assertEqual(all, [(1, 'emilia', 'emilia123')])