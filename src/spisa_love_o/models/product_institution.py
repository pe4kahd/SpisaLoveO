from sqlalchemy import Column, String, Boolean, ForeignKey, Integer, LargeBinary, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import AbstractModel

class ProductInstitution(AbstractModel):
    institution_id = Column(UUID(as_uuid=True), ForeignKey("institution.id"))
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"))

    institution = relationship("Institution", back_populates="product_links")
    product = relationship("Product", back_populates="institutions")