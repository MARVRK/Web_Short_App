from abc import ABC, abstractmethod
from models import User
from repo import DataBase

db = DataBase()

class UserAbstraction(ABC):
    @abstractmethod
    def save_user(self, name: str):
        pass

    @abstractmethod
    def upload_user(self, user_id: int):
        pass


class UserRepository(UserAbstraction):

    def save_user(self, name: str):
        return db.upload_user(name)

    def upload_user(self, user_id: int):
        return db.get_user(user_id)