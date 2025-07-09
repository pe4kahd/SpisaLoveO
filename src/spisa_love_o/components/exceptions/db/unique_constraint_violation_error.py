class UniqueConstraintViolationError(Exception):
    """Класс ошибки нарушения уникального ограничения"""

    def __init__(self, message, field_name=None, value=None, original_exception=None):
        super().__init__(message)
        self.field_name = field_name
        self.value = value
        self.original_exception = original_exception
