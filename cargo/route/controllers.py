from cargo.route.models import City, Warehouse, Route
from cargo.utils.config import OK, WRONG_REQUEST, NOT_FOUND
from cargo.utils.db import session_scope

from cargo.utils.decorators import logged
from cargo.utils.protocol import create_response


@logged
def create_city_controller(command):
    data = command.get('data')
    with session_scope() as session:
        city = City()
        for k, v in data.get('city').items():
            if v:
                setattr(city, k, v)
        session.add(city)
    return create_response(command, OK, {'message': 'City added'})


@logged
def read_city_name_by_id_controller(command):
    try:
        city_id = command.get('data').get('city').get('id')
        if not city_id:
            raise IndexError
    except IndexError:
        return create_response(command, WRONG_REQUEST, {'message': 'No id or data specified'})
    else:
        with session_scope() as session:
            city = session.query(City).filter_by(id=city_id).first()
            if city:
                city = {attr: getattr(city, attr) for attr in city.__dict__ if attr[0] != '_'}
                return create_response(command, OK, {'city': city, 'message': 'City read'})
            else:
                return create_response(command, NOT_FOUND, {'message': f'City with id={city_id} not found'})


@logged
def read_city_id_by_name_controller(command):
    try:
        city_name = command.get('data').get('city').get('name')
        if not city_name:
            raise IndexError
    except IndexError:
        return create_response(command, WRONG_REQUEST, {'message': 'No id or data specified'})
    else:
        with session_scope() as session:
            city = session.query(City).filter_by(name=city_name).first()
            if city:
                city = {attr: getattr(city, attr) for attr in city.__dict__ if attr[0] != '_'}
                return create_response(command, OK, {'city': city, 'message': 'City read'})
            else:
                return create_response(command, NOT_FOUND, {'message': f'City with name={city_name} not found'})


@logged
def read_cities_controller(command):
    with session_scope() as session:
        cities = session.query(City).all()
        cities = [{attr: getattr(city, attr) for attr in city.__dict__ if attr[0] != '_'}
                  for city in cities]
        return create_response(command, OK, {'cities': cities, 'message': 'Cities read'})


@logged
def update_city_controller(command):
    data = command.get('data')
    try:
        city_attrs = {attr: data.get('city').get(attr) for attr in City.__dict__ if attr[0] != '_'}
    except IndexError:
        return create_response(command, WRONG_REQUEST, {'message': 'No id or data specified'})
    else:
        with session_scope() as session:
            city = session.query(City).filter_by(id=city_attrs.get('id')).first()
            if city:
                for k, v in city_attrs.items():
                    if v:
                        setattr(city, k, v)
                return create_response(command, OK, {'message': 'City updated'})
            else:
                return create_response(command, NOT_FOUND,
                                       {'message': f'City with id={city_attrs.get("id")} not found'})


@logged
def delete_city_controller(command):
    try:
        city_id = command.get('data').get('city').get('id')
        if not city_id:
            raise IndexError
    except IndexError:
        return create_response(command, WRONG_REQUEST, {'message': 'No id or data specified'})
    else:
        with session_scope() as session:
            city = session.query(City).filter_by(id=city_id).first()
            if city:
                session.delete(city)
                return create_response(command, OK, {'message': 'City deleted'})
            else:
                return create_response(command, NOT_FOUND, {'message': f'City with id={city_id} not found'})


@logged
def create_warehouse_controller(command):
    data = command.get('data')
    with session_scope() as session:
        warehouse = Warehouse()
        for k, v in data.get('warehouse').items():
            if v:
                setattr(warehouse, k, v)
        session.add(warehouse)
    return create_response(command, OK, {'message': 'Warehouse added'})


@logged
def read_warehouse_controller(command):
    try:
        warehouse_id = command.get('data').get('warehouse').get('id')
        if not warehouse_id:
            raise IndexError
    except IndexError:
        return create_response(command, WRONG_REQUEST, {'message': 'No id or data specified'})
    else:
        with session_scope() as session:
            warehouse = session.query(Warehouse).filter_by(id=warehouse_id).first()
            if warehouse:
                warehouse = {attr: getattr(warehouse, attr) for attr in warehouse.__dict__ if attr[0] != '_'}
                return create_response(command, OK, {'warehouse': warehouse, 'message': 'Warehouse read'})
            else:
                return create_response(command, NOT_FOUND, {'message': f'Warehouse with id={warehouse_id} not found'})


@logged
def read_warehouses_controller(command):
    with session_scope() as session:
        warehouses = session.query(Warehouse).all()
        warehouses = [{attr: getattr(warehouse, attr) for attr in warehouse.__dict__ if attr[0] != '_'}
                      for warehouse in warehouses]
        return create_response(command, OK, {'warehouses': warehouses, 'message': 'Warehouses read'})


@logged
def read_warehouses_of_city_controller(command):
    city_id = command.get('data').get('city').get('id')
    with session_scope() as session:
        warehouses = session.query(Warehouse).filter_by(city_id=city_id)
        warehouses = [{attr: getattr(warehouse, attr) for attr in warehouse.__dict__ if attr[0] != '_'}
                      for warehouse in warehouses]
        return create_response(command, OK, {'warehouses': warehouses, 'message': 'Warehouses read'})


@logged
def update_warehouse_controller(command):
    data = command.get('data')
    try:
        warehouse_attrs = {attr: data.get('warehouse').get(attr) for attr in Warehouse.__dict__ if attr[0] != '_'}
    except IndexError:
        return create_response(command, WRONG_REQUEST, {'message': 'No id or data specified'})
    else:
        with session_scope() as session:
            warehouse = session.query(Warehouse).filter_by(id=warehouse_attrs.get('id')).first()
            if warehouse:
                for k, v in warehouse_attrs.items():
                    if v:
                        setattr(warehouse, k, v)
                return create_response(command, OK, {'message': 'Warehouse updated'})
            else:
                return create_response(command, NOT_FOUND,
                                       {'message': f'Warehouse with id={warehouse_attrs.get("id")} not found'})


@logged
def delete_warehouse_controller(command):
    try:
        warehouse_id = command.get('data').get('warehouse').get('id')
        if not warehouse_id:
            raise IndexError
    except IndexError:
        return create_response(command, WRONG_REQUEST, {'message': 'No id or data specified'})
    else:
        with session_scope() as session:
            warehouse = session.query(Warehouse).filter_by(id=warehouse_id).first()
            if warehouse:
                session.delete(warehouse)
                return create_response(command, OK, {'message': 'Warehouse deleted'})
            else:
                return create_response(command, NOT_FOUND, {'message': f'Warehouse with id={warehouse_id} not found'})


@logged
def create_route_controller(command):
    data = command.get('data')
    with session_scope() as session:
        route = Route()
        for k, v in data.get('route').items():
            if v:
                setattr(route, k, v)
        session.add(route)
    return create_response(command, OK, {'message': 'Route added'})


@logged
def read_route_controller(command):
    try:
        route_id = command.get('data').get('route').get('id')
        if not route_id:
            raise IndexError
    except IndexError:
        return create_response(command, WRONG_REQUEST, {'message': 'No id or data specified'})
    else:
        with session_scope() as session:
            route = session.query(Route).filter_by(id=route_id).first()
            if route:
                route = {attr: getattr(route, attr) for attr in route.__dict__ if attr[0] != '_'}
                return create_response(command, OK, {'route': route, 'message': 'Route read'})
            else:
                return create_response(command, NOT_FOUND, {'message': f'Route with id={route_id} not found'})


@logged
def read_routes_controller(command):
    with session_scope() as session:
        routes = session.query(Route).all()
        routes = [{attr: getattr(route, attr) for attr in route.__dict__ if attr[0] != '_'}
                  for route in routes]
        return create_response(command, OK, {'routes': routes, 'message': 'Routes read'})


# @logged
# def read_routes_of_city_controller(command):
#     with session_scope() as session:
#         routes = session.query(Route).filter(city_id=city_id)
#         routes = [{attr: getattr(route, attr) for attr in route.__dict__ if attr[0] != '_'}
#                   for route in routes]
#         return create_response(command, OK, {'routes': routes, 'message': 'Routes read'})


@logged
def update_route_controller(command):
    data = command.get('data')
    try:
        route_attrs = {attr: data.get('route').get(attr) for attr in Route.__dict__ if attr[0] != '_'}
    except IndexError:
        return create_response(command, WRONG_REQUEST, {'message': 'No id or data specified'})
    else:
        with session_scope() as session:
            route = session.query(Route).filter_by(id=route_attrs.get('id')).first()
            if route:
                for k, v in route_attrs.items():
                    if v:
                        setattr(route, k, v)
                return create_response(command, OK, {'message': 'Route updated'})
            else:
                return create_response(command, NOT_FOUND,
                                       {'message': f'Route with id={route_attrs.get("id")} not found'})


@logged
def delete_route_controller(command):
    try:
        route_id = command.get('data').get('route').get('id')
        if not route_id:
            raise IndexError
    except IndexError:
        return create_response(command, WRONG_REQUEST, {'message': 'No id or data specified'})
    else:
        with session_scope() as session:
            route = session.query(Route).filter_by(id=route_id).first()
            if route:
                session.delete(route)
                return create_response(command, OK, {'message': 'Route deleted'})
            else:
                return create_response(command, NOT_FOUND, {'message': f'Route with id={route_id} not found'})
