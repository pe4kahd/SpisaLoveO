from typing import Optional

from src.spisa_love_o.components.exceptions.abstract import AbstractApplicationException


class InternalServerException(AbstractApplicationException):
    """Класс ошибки со стороны сервера"""

    def __init__(
        self,
        original_error: Optional[Exception] = None,
    ):
        super().__init__(
            code="500",
            name=f"{self.app_domain}.general.internal-server-error",
            original_error=original_error,
        )
