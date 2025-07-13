import re
import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declared_attr, as_declarative


def camel_to_snake(name: str) -> str:
    """Convert CamelCase to snake_case."""
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

@as_declarative()
class Base:
    id: UUID
    __name__: str

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return camel_to_snake(cls.__name__)


class AbstractModel(Base):
    """
    Базовая модель реляционной базы данных с поддержкой soft-delete.
    """

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    __abstract__ = True

