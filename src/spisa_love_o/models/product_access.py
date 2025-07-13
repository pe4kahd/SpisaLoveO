from sqlalchemy import Column, String, Boolean, ForeignKey, Integer, LargeBinary, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import AbstractModel

class ProductAccess(AbstractModel):
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"))

    user = relationship("User", back_populates="accesses")
    product = relationship("Product", back_populates="accesses")