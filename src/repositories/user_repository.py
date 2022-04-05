import entities
import sqlite3

class UserRepository:
    def __init__(self, name):
        self.db = sqlite3.connect(name)
        self.db.isolation_level = None

    def create_table(self):
        self.db.execute("begin")
        self.db.execute("create table users1 (id integer primary key, name text, password text)")
        self.db.execute("commit")

    def create_user(self, user: User):
        self.db.execute("begin")
        self.db.execute("insert into users1 (name, password) values (?,?)", [user.username, user.password])
        self.db.execute("commit")
        return user

    def find_users(self):
        self.db.execute("begin")
        all_users=self.db.execute("select * from users1").fetchall()
        self.db.execute("commit")
        return all_users

    def delete_table(self):
        self.db.execute("begin")
        self.db.execute("drop table users1")
        self.db.execute("commit")

if __name__ == "__main__":
    u = UserRepository()
    u.create_table()