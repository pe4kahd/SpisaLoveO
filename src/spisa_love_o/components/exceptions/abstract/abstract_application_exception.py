from abc import ABC
from typing import Optional



class AbstractApplicationException(Exception, ABC):
    """Абстрактный класс исключения приложения"""

    code: str
    """Код ошибки"""
    name: str
    """Название"""
    original_error: Optional[Exception]
    """Изначальная ошибка"""

    app_domain: str = ""

    def __init__(
        self,
        name: str,
        code: str,
        original_error: Optional[Exception] = None,
    ):
        """
        :param code: код ошибки (http)
        :param name: название ошибки
        :param original_error: изначальная ошибка
        """

        self.code = code
        self.name = name
        self.original_error = original_error

        super().__init__(name)
