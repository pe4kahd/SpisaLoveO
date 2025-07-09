from src.spisa_love_o.components.exceptions.abstract import AbstractApplicationException


class NotAuthorizedException(AbstractApplicationException):
    """Класс ошибки авторизации"""

    def __init__(self):
        super().__init__(code="401", name=f"{self.app_domain}.general.not-authorized")
