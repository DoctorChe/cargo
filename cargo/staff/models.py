from sqlalchemy import Column, Integer, String

from cargo.utils.db import Base


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    patronymic = Column(String)
    phone = Column(String)
    info = Column(String)
