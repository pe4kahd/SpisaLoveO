from logging import Logger
from typing import Optional

from dependency_injector.providers import Factory
from dependency_injector.wiring import inject, Provider


class LoggerMixin:
    """Миксин, внедряющий логгер в класс"""

    __logger: Optional[Logger] = None
    """Логгер приложения"""

    @inject
    def __get_logger(
        self,
        logger_factory: Factory[Logger] = Provider["logger"],
    ) -> Logger:
        return logger_factory.add_kwargs(name=self.__class__.__name__)()

    @property
    def _logger(self) -> Logger:
        """Получение и активация логгера приложения"""
        if self.__class__.__logger is None:
            self.__class__.__logger = self.__get_logger()

        return self.__class__.__logger
