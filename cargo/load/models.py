from sqlalchemy import Column, Integer, String, Float

from cargo.utils.db import Base


class Load(Base):
    __tablename__ = "load"
    id = Column(Integer, primary_key=True, autoincrement=True)
    length = Column(Float, nullable=False)  # m
    height = Column(Float, nullable=False)  # m
    width = Column(Float, nullable=False)  # m
    weight = Column(Float, nullable=False)  # kg
    load_from = Column(String, nullable=False)
    load_to = Column(String, nullable=False)
    info = Column(String)
