from aiogram.filters import BaseFilter
from aiogram.types import Message

from core.config import Config


# Defining a custom filter class named AdminFilter, inheriting from BaseFilter
class AdminFilter(BaseFilter):
    # Setting a class attribute is_admin with a default value of True
    is_admin: bool = True

    # Defining an asynchronous method __call__ which takes a Message object and a Config object as arguments
    async def __call__(self, obj: Message, config: Config) -> bool:
        # Checking if the sender's user ID (obj.from_user.id) is in the list of admin IDs (config.tg_bot.admin_ids)
        # The result is then compared with the value of self.is_admin
        # If the user ID is in the list and is_admin is True, or if the user
        # ID is not in the list and is_admin is False, it returns True
        # Otherwise, it returns False
        return (obj.from_user.id in config.tg_bot.admin_ids) == self.is_admin
