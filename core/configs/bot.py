from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    """Creates the TgBot object from environment variables."""

    token: str
    admin_ids: list[int]

    @staticmethod
    def from_env(env: Env):
        """Creates the TgBot object from environment variables."""
        token = env.str("BOT_TOKEN")
        admin_ids = env.list("ADMINS", subcast=int)
        return TgBot(token=token, admin_ids=admin_ids)
