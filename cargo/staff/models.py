from sqlalchemy import Column, Integer, String, UniqueConstraint
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

    __table_args__ = (
        UniqueConstraint('name', 'surname', 'patronymic', name='_name_surname_patronymic_uc'),
        )
