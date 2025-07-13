from sqlalchemy import Column, String, Boolean, ForeignKey, Integer, LargeBinary, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import AbstractModel

class SubjectSpeciality(AbstractModel):
    subject_id = Column(UUID(as_uuid=True), ForeignKey("subject.id"))
    speciality_id = Column(UUID(as_uuid=True), ForeignKey("speciality.id"))
    approved = Column(Boolean, default=False)

    subject = relationship("Subject", back_populates="specialties")
    specialty = relationship("Speciality", back_populates="subject_links")