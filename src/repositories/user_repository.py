import sqlite3
from entities.user import User

class UserRepository:
    def __init__(self, name):
        self.db = sqlite3.connect(name)
        self.db.isolation_level = None

    def create_table(self):
        self.db.execute("begin")
        self.db.execute("create table users2 (id integer primary key, name text, password text)")
        self.db.execute("commit")

    def create_user(self, users2: User):
        self.db.execute("begin")
        self.db.execute("insert into users2 (name, password) values (?,?)", [users2.username, users2.password])
        self.db.execute("commit")
        return users2

    def find_users(self):
        self.db.execute("begin")
        all_users=self.db.execute("select * from users2").fetchall()
        self.db.execute("commit")
        return all_users

    def delete_table(self):
        self.db.execute("begin")
        self.db.execute("drop table users2")
        self.db.execute("commit")

if __name__ == "__main__":
    u = UserRepository()
    u.create_table()
