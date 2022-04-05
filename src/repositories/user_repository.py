import sqlite3
from entities.users import User

class UserRepository:
    def __init__(self, name):
        self.db = sqlite3.connect(name)
        self.db.isolation_level = None

    def create_table(self):
        self.db.execute("begin")
        self.db.execute("create table users (id integer primary key, name text, password text)")
        self.db.execute("commit")

    def create_user(self, users: User):
        self.db.execute("begin")
        self.db.execute("insert into users (name, password) values (?,?)", [users.username, users.password])
        self.db.execute("commit")
        return users

    def find_users(self):
        self.db.execute("begin")
        all_users=self.db.execute("select * from users").fetchall()
        self.db.execute("commit")
        return all_users

    def delete_table(self):
        self.db.execute("begin")
        self.db.execute("drop table users")
        self.db.execute("commit")

if __name__ == "__main__":
    u = UserRepository()
    u.create_table()
