from dataclasses import dataclass
from abc import ABC, abstractmethod
from models import User
from repo import DataBase

db = DataBase()


class UserAbstraction(ABC):
    @abstractmethod
    def save_user(self, name: str) -> User:
        pass

    @abstractmethod
    def download_user(self, user_id: int) -> User:
        pass


class UserRepository(UserAbstraction):

    def save_user(self, name: str) -> User:
        return db.upload_user(name)

    def download_user(self, user_id: int) -> User:
        return db.get_user(user_id)

@dataclass()
class MockUserRepository(UserAbstraction):
    store : dict[str | int, User] | None

    def save_user(self, name: str) -> User:
        return self.store.get(name)

    def download_user(self, user_id: int) -> User:
        return self.store.get(user_id)

