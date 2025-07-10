from sqlalchemy import Column, String, Boolean, ForeignKey, Integer, LargeBinary
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from .base import AbstractModel

class User(AbstractModel):
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)

    products = relationship("Product", back_populates="user")
    reviews = relationship("Review", back_populates="user")
    accesses = relationship("ProductAccess", back_populates="user")

class Product(AbstractModel):
    info = Column(String)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))

    user = relationship("User", back_populates="products")
    files = relationship("ProductFile", back_populates="product")
    accesses = relationship("ProductAccess", back_populates="product")
    reviews = relationship("Review", back_populates="product")

    institutions = relationship("ProductInstitution", back_populates="product")
    faculties = relationship("ProductFaculty", back_populates="product")
    specialties = relationship("ProductSpecialty", back_populates="product")
    subjects = relationship("ProductSubject", back_populates="product")


class ProductAccess(AbstractModel):
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"))

    user = relationship("User", back_populates="accesses")
    product = relationship("Product", back_populates="accesses")

class ProductFile(AbstractModel):
    name = Column(String, nullable=False)
    file = Column(LargeBinary, nullable=False)
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"))

    product = relationship("Product", back_populates="files")

class Review(AbstractModel):
    comment = Column(String)
    score = Column(Integer)  # score: int(0-5)
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))

    user = relationship("User", back_populates="reviews")
    product = relationship("Product", back_populates="reviews")

class Institution(AbstractModel):
    name = Column(String, nullable=False)
    approved = Column(Boolean, default=False)

    faculties = relationship("Faculty", back_populates="institution")
    product_links = relationship("ProductInstitution", back_populates="institution")

class Faculty(AbstractModel):
    name = Column(String, nullable=False)
    institution_id = Column(UUID(as_uuid=True), ForeignKey("institution.id"))
    approved = Column(Boolean, default=False)

    institution = relationship("Institution", back_populates="faculties")
    specialties = relationship("Speciality", back_populates="faculty")
    product_links = relationship("ProductFaculty", back_populates="faculty")

class Speciality(AbstractModel):
    name = Column(String, nullable=False)
    course_count = Column(Integer)
    faculty_id = Column(UUID(as_uuid=True), ForeignKey("faculty.id"))
    approved = Column(Boolean, default=False)

    faculty = relationship("Faculty", back_populates="specialties")
    product_links = relationship("ProductSpecialty", back_populates="specialty")
    subject_links = relationship("SubjectSpeciality", back_populates="specialty")

class Subject(AbstractModel):
    name = Column(String, nullable=False)
    approved = Column(Boolean, default=False)

    specialties = relationship("SubjectSpeciality", back_populates="subject")
    product_links = relationship("ProductSubject", back_populates="subject")

class SubjectSpeciality(AbstractModel):
    subject_id = Column(UUID(as_uuid=True), ForeignKey("subject.id"))
    speciality_id = Column(UUID(as_uuid=True), ForeignKey("speciality.id"))
    approved = Column(Boolean, default=False)

    subject = relationship("Subject", back_populates="specialties")
    specialty = relationship("Speciality", back_populates="subject_links")

class ProductInstitution(AbstractModel):
    institution_id = Column(UUID(as_uuid=True), ForeignKey("institution.id"))
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"))

    institution = relationship("Institution", back_populates="product_links")
    product = relationship("Product", back_populates="institutions")

class ProductFaculty(AbstractModel):
    faculty_id = Column(UUID(as_uuid=True), ForeignKey("faculty.id"))
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"))

    faculty = relationship("Faculty", back_populates="product_links")
    product = relationship("Product", back_populates="faculties")

class ProductSpecialty(AbstractModel):
    speciality_id = Column(UUID(as_uuid=True), ForeignKey("speciality.id"))
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"))

    specialty = relationship("Speciality", back_populates="product_links")
    product = relationship("Product", back_populates="specialties")


class ProductSubject(AbstractModel):
    subject_id = Column(UUID(as_uuid=True), ForeignKey("subject.id"))
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"))

    subject = relationship("Subject", back_populates="product_links")
    product = relationship("Product", back_populates="subjects")