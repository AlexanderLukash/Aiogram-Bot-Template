from infrastructure.database.repository.repository import UsersORMRepository


class UsersService:
    # Initialize the UsersService with a UsersORMRepository instance
    def __init__(self, users_repo: UsersORMRepository):
        self.users_repo: UsersORMRepository = users_repo()

    async def get_user_by_id(self, data: int):
        user = await self.users_repo.get_one_by_id(
            data,
        )  # Get a user by ID using the repository
        return user
