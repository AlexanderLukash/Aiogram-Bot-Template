import asyncio
import logging

from environs import Env
from tortoise import run_async

from bot.main import main
from core.configs.database import DbConfig
from infrastructure.database.setup import init_tortoise

if __name__ == "__main__":
    env = Env()
    env.read_env()  # прочитати .env файл

    db_config = DbConfig.from_env(env)
    modules = {
        "models": [
            "infrastructure.database.models.users",
        ],  # Update with your actual model modules
    }
    run_async(init_tortoise(db_config, modules))
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("The bot has been disabled!")
