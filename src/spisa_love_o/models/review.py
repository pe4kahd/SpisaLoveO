from sqlalchemy import Column, String, Boolean, ForeignKey, Integer, LargeBinary, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import AbstractModel


class Review(AbstractModel):
    comment = Column(String)
    score = Column(Integer)  # score: int(0-5)
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))

    user = relationship("User", back_populates="reviews")
    product = relationship("Product", back_populates="reviews")