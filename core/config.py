from dataclasses import dataclass
from typing import Optional

from environs import Env

from core.configs.bot import TgBot
from core.configs.database import DbConfig


@dataclass
class Config:
    """The main configuration class that integrates all the other configuration
    classes.

    This class holds the other configuration classes, providing a centralized point of access for all settings.

    Attributes
    ----------
    tg_bot : TgBot
        Holds the settings related to the Telegram Bot.
    db : Optional[DbConfig]
        Holds the settings specific to the database (default is None).

    """

    tg_bot: TgBot
    db: Optional[DbConfig] = None


def load_config(path: str = None) -> Config:
    """This function takes an optional file path as input and returns a Config
    object.

    :param path: The path of env file from where to load the
        configuration variables. It reads environment variables from a
        .env file if provided, else from the process environment.
    :return: Config object with attributes set as per environment
        variables.

    """

    # Create an Env object.
    # The Env object will be used to read environment variables.
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot.from_env(env),
        db=DbConfig.from_env(env),
    )
