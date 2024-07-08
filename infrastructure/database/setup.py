from tortoise import Tortoise

from core.configs.database import DbConfig


async def init_tortoise(db: DbConfig, modules: dict):
    """Initializes Tortoise ORM with the given database configuration and
    modules.

    Parameters
    ----------
    db : DbConfig
        The database configuration.
    modules : dict
        A dictionary containing the module configurations.

    """
    tortoise_url = db.construct_tortoise_url()
    await Tortoise.init(
        db_url=tortoise_url,
        modules=modules,
    )
    await Tortoise.generate_schemas()


async def close_tortoise():
    """Closes Tortoise ORM connections."""
    await Tortoise.close_connections()
