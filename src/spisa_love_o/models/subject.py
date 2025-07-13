from sqlalchemy import Column, String, Boolean, ForeignKey, Integer, LargeBinary, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import AbstractModel

class Subject(AbstractModel):
    name = Column(String, nullable=False)
    approved = Column(Boolean, default=False)

    specialties = relationship("SubjectSpeciality", back_populates="subject")
    product_links = relationship("ProductSubject", back_populates="subject")