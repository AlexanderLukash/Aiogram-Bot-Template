from dataclasses import dataclass

from environs import Env


@dataclass
class DbConfig:
    """Database configuration class. This class holds the settings for the
    database, such as host, password, port, etc.

    Attributes
    ----------
    host : str
        The host where the database server is located.
    password : str
        The password used to authenticate with the database.
    user : str
        The username used to authenticate with the database.
    database : str
        The name of the database.
    port : int
        The port where the database server is listening.

    """

    host: str
    password: str
    user: str
    database: str
    port: int = 5432

    def construct_tortoise_url(self, driver="asyncpg", host=None, port=None) -> str:
        """Constructs and returns a TortoiseORM URL for this database
        configuration."""
        if not host:
            host = self.host
        if not port:
            port = self.port
        return f"{driver}://{self.user}:{self.password}@{host}:{port}/{self.database}"

    @staticmethod
    def from_env(env: Env):
        """Creates the DbConfig object from environment variables."""
        host = env.str("DB_HOST")
        password = env.str("POSTGRES_PASSWORD")
        user = env.str("POSTGRES_USER")
        database = env.str("POSTGRES_DB")
        port = env.int("DB_PORT", 5432)
        return DbConfig(
            host=host,
            password=password,
            user=user,
            database=database,
            port=port,
        )
