from sqlalchemy import Column, String, Boolean, ForeignKey, Integer, LargeBinary, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import AbstractModel

class ProductFaculty(AbstractModel):
    faculty_id = Column(UUID(as_uuid=True), ForeignKey("faculty.id"))
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"))

    faculty = relationship("Faculty", back_populates="product_links")
    product = relationship("Product", back_populates="faculties")