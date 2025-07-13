from sqlalchemy import Column, String, Boolean, ForeignKey, Integer, LargeBinary, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import AbstractModel

class User(AbstractModel):
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)

    products = relationship("Product", back_populates="user")
    reviews = relationship("Review", back_populates="user")
    accesses = relationship("ProductAccess", back_populates="user")