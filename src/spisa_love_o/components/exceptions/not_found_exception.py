from src.spisa_love_o.components.exceptions.abstract import AbstractApplicationException


class NotFoundException(AbstractApplicationException):
    """Класс ошибки поиска сущности"""

    def __init__(
        self, name: str = f"{AbstractApplicationException.app_domain}.general.not-found"
    ):
        super().__init__(code="404", name=name)
