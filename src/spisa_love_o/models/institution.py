from sqlalchemy import Column, String, Boolean, ForeignKey, Integer, LargeBinary, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import AbstractModel

class Institution(AbstractModel):
    name = Column(String, nullable=False)
    approved = Column(Boolean, default=False)

    faculties = relationship("Faculty", back_populates="institution")
    product_links = relationship("ProductInstitution", back_populates="institution")