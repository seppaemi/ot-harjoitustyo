import unittest
from repositories.user_repository import UserRepository
from entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.ur = UserRepository("tests.db")
        self.ur.delete_table()
        self.ur.create_table()
        self.user1 = User('emilia', '123456')

    def test_create(self):
        self.ur.create_user(self.user1)
        all = self.ur.find_users()
        self.assertEqual(all, [(1, 'emilia', '123456')])