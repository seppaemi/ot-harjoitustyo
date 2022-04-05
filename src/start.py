from repositories.user_repository import UserRepository

table = UserRepository("users.db")
table.create_table()