from sqlalchemy import Column, String, Boolean, ForeignKey, Integer, LargeBinary, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import AbstractModel


class ProductFile(AbstractModel):
    name = Column(String, nullable=False)
    file = Column(LargeBinary, nullable=False)
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"))

    product = relationship("Product", back_populates="files")