from sqlalchemy import Column, String, Boolean, ForeignKey, Integer, LargeBinary, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import AbstractModel


class Product(AbstractModel):
    info = Column(String)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    price = Column(Float, nullable=False)

    user = relationship("User", back_populates="products")
    files = relationship("ProductFile", back_populates="product")
    accesses = relationship("ProductAccess", back_populates="product")
    reviews = relationship("Review", back_populates="product")

    institutions = relationship("ProductInstitution", back_populates="product")
    faculties = relationship("ProductFaculty", back_populates="product")
    specialties = relationship("ProductSpecialty", back_populates="product")
    subjects = relationship("ProductSubject", back_populates="product")