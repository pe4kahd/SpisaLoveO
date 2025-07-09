from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.spisa_love_o.components.injectable import injectable
from src.spisa_love_o.components.mixins.logger import LoggerMixin
from src.spisa_love_o.config import DatabaseRelationalSettings


@injectable()
class AsyncDatabaseRelational(LoggerMixin):
    __db_config: DatabaseRelationalSettings

    def __init__(
        self, db_config: DatabaseRelationalSettings
    ) -> None:
        self.__db_config = db_config

        self._logger.info(
            f"Database wrapper created (Connection: {db_config.host}:{db_config.port}, user={db_config.user}, db={db_config.name})"
        )

        self._engine = create_async_engine(self.__db_config.url, echo=False)
        self._sessionmaker = async_sessionmaker(self._engine, expire_on_commit=False)

        self._logger.info("Database connection established")

    async def get_session(self) -> AsyncSession:
        if not self._sessionmaker:
            raise RuntimeError("Database not connected")
        return self._sessionmaker()

    async def close(self):
        if self._engine:
            await self._engine.dispose()
            self._logger.info("Database connection closed")
