from abc import ABC, abstractmethod

from infrastructure.database.models.users import User


# Define an abstract base class for repositories
class AbstractRepository(ABC):
    @abstractmethod
    async def find_all(self):  # Abstract method to find all records
        raise NotImplementedError


# Concrete repository implementing the abstract class
class TortoiseORMRepository(AbstractRepository):
    model = None  # Placeholder for the model

    async def find_all(self):  # Implementation of find_all method
        res = await self.model.all()
        return res


class UsersORMRepository(TortoiseORMRepository):
    model = User

    # Method to get one user by ID
    async def get_one_by_id(self, data: int):
        res = await self.model.filter(telegram_id=data).first()
        return res
