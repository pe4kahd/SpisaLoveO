from sqlalchemy import Column, String, Boolean, ForeignKey, Integer, LargeBinary, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import AbstractModel

class ProductSpecialty(AbstractModel):
    speciality_id = Column(UUID(as_uuid=True), ForeignKey("speciality.id"))
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"))

    specialty = relationship("Speciality", back_populates="product_links")
    product = relationship("Product", back_populates="specialties")