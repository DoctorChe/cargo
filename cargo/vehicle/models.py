from sqlalchemy import Column, Integer, String, Float

from cargo.utils.db import Base


class Vehicle(Base):
    __tablename__ = "vehicle"
    id = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(String, nullable=False)
    plate = Column(String, nullable=False)
    year = Column(Integer)
    payload = Column(Integer, nullable=False)  # kg
    run = Column(Integer)  # km
    fuel_consumption = Column(Float)  # l/100km
    volume = Column(Float, nullable=False)  # m3
