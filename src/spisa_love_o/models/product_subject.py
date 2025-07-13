from sqlalchemy import Column, String, Boolean, ForeignKey, Integer, LargeBinary, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import AbstractModel

class ProductSubject(AbstractModel):
    subject_id = Column(UUID(as_uuid=True), ForeignKey("subject.id"))
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"))

    subject = relationship("Subject", back_populates="product_links")
    product = relationship("Product", back_populates="subjects")