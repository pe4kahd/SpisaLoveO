from sqlalchemy import Column, String, Boolean, ForeignKey, Integer, LargeBinary, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import AbstractModel

class Faculty(AbstractModel):
    name = Column(String, nullable=False)
    institution_id = Column(UUID(as_uuid=True), ForeignKey("institution.id"))
    approved = Column(Boolean, default=False)

    institution = relationship("Institution", back_populates="faculties")
    specialties = relationship("Speciality", back_populates="faculty")
    product_links = relationship("ProductFaculty", back_populates="faculty")