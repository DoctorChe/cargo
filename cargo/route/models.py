from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from cargo.utils.db import Base


class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    warehouses = relationship('Warehouse')


class Warehouse(Base):
    __tablename__ = 'warehouse'
    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'))
    city = relationship('City', back_populates='warehouses')
    # route_id = Column(Integer, ForeignKey('route.id'))
    # from_warehouse = relationship('Route', back_populates='warehouses')
    # to_warehouse = relationship('Route', back_populates='warehouses')
    # route = relationship('Route',
    #                      uselist=False,
    #                      viewonly=True,
    #                      primaryjoin='''or_(
    #                      Route.from_id == id,
    #                      Route.route_to == id,
    #                      )''')


class Route(Base):
    __tablename__ = 'route'
    id = Column(Integer, primary_key=True)

    from_warehouse_id = Column(Integer, ForeignKey('warehouse.id'))
    to_warehouse_id = Column(Integer, ForeignKey('warehouse.id'))

    # from_ = relationship('Warehouse', foreign_keys=from_id, uselist=False, back_populates='route')
    # from_warehouse = relationship('Warehouse', foreign_keys='[Route.from_id]')
    from_warehouse = relationship('Warehouse', foreign_keys=[from_warehouse_id])
    # to_ = relationship('Warehouse', foreign_keys=to_id, uselist=False, back_populates='route')
    # to_warehouse = relationship('Warehouse', foreign_keys='[Route.to_id]')
    to_warehouse = relationship('Warehouse', foreign_keys=[to_warehouse_id])

    # warehouses = relationship('Warehouse', back_populates='route')
