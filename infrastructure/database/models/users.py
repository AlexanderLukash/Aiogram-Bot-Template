from tortoise import fields
from tortoise.models import Model


# Defining a Tortoise ORM model for User
class User(Model):
    # Primary key field for the user's ID
    id = fields.IntField(pk=True)  # noqa
    telegram_id = fields.IntField(
        unique=True,
    )  # Unique field for the user's Telegram ID
    name = fields.CharField(
        max_length=100,
    )  # Field for the user's name, limited to 100 characters
    username = fields.CharField(
        max_length=235,
        null=True,
    )  # Field for the user's username, nullable and limited to 235 characters

    def __str__(self) -> str:
        return (
            self.name
        )  # String representation of the User model, returns the user's name
