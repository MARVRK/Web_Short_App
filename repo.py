import sqlite3
from models import User


class DataBase:
    def __init__(self):
        self.con = sqlite3.connect("users.db", check_same_thread=False)
        self.cursor = self.con.cursor()

    def test_connection(self):
        try:
            if self.con:
                return "connection successful"
        except Exception as e:
            raise e

    def create_table(self) :
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS User(
                                   user_id INTEGER Primary Key AUTOINCREMENT,
                                   user_name TEXT);''')
            return "table successfully created"
        except Exception as e:
            raise e

    def upload_user(self,name: str) -> User:
        try:
            self.cursor.execute('''INSERT INTO User (user_name) 
                                    VALUES (?)
                                    ''', (name,))
            new_user_id = self.cursor.lastrowid
            self.con.commit()
            return User(id=new_user_id, name=name)
        except Exception as e:
            raise e

    def get_user(self, user_id: int) -> User:
        try:
            self.cursor.execute('''SELECT * FROM User WHERE user_id = (?)'''
                                , (user_id,))
            data = self.cursor.fetchone()
            return User(id=data[0], name=data[1])
        except Exception as e:
            raise e