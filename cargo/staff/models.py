from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from cargo.utils.db import Base
# from cargo.route.models import Route


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    patronymic = Column(String)
    phone = Column(String)
    info = Column(String)

    routes = relationship('Route', back_populates='person')
