from sqlalchemy import Column, String, Boolean, ForeignKey, Integer, LargeBinary, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import AbstractModel

class Speciality(AbstractModel):
    name = Column(String, nullable=False)
    course_count = Column(Integer)
    faculty_id = Column(UUID(as_uuid=True), ForeignKey("faculty.id"))
    approved = Column(Boolean, default=False)

    faculty = relationship("Faculty", back_populates="specialties")
    product_links = relationship("ProductSpecialty", back_populates="specialty")
    subject_links = relationship("SubjectSpeciality", back_populates="specialty")