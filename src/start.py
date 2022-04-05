
from repositories.user_repository import UserRepository

u = UserRepository("users.db")
u.create_table()