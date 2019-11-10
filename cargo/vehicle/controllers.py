from cargo.vehicle.models import Vehicle
from cargo.utils.config import OK, WRONG_REQUEST, NOT_FOUND
from cargo.utils.db import session_scope

from cargo.utils.decorators import logged
from cargo.utils.protocol import create_response


@logged
def create_vehicle_controller(command):
    data = command.get('data')
    with session_scope() as session:
        vehicle = Vehicle()
        for k, v in data.get('vehicle').items():
            if v:
                setattr(vehicle, k, v)
        session.add(vehicle)
    return create_response(command, OK, {'message': 'Vehicle added'})


@logged
def read_vehicle_controller(command):
    try:
        vehicle_id = command.get('data').get('vehicle').get('id')
        if not vehicle_id:
            raise IndexError
    except IndexError:
        return create_response(command, WRONG_REQUEST, {'message': 'No id or data specified'})
    else:
        with session_scope() as session:
            vehicle = session.query(Vehicle).filter_by(id=vehicle_id).first()
            if vehicle:
                vehicle = {attr: getattr(vehicle, attr) for attr in vehicle.__dict__ if attr[0] != '_'}
                return create_response(command, OK, {'vehicle': vehicle, 'message': 'Vehicle read'})
            else:
                return create_response(command, NOT_FOUND, {'message': f'Vehicle with id={vehicle_id} not found'})


@logged
def read_vehicles_controller(command):
    with session_scope() as session:
        vehicles = session.query(Vehicle).all()
        vehicles = [{attr: getattr(vehicle, attr) for attr in vehicle.__dict__ if attr[0] != '_'}
                    for vehicle in vehicles]
        return create_response(command, OK, {'vehicles': vehicles, 'message': 'Vehicles read'})


@logged
def update_vehicle_controller(command):
    data = command.get('data')
    try:
        vehicle_attrs = {attr: data.get('vehicle').get(attr) for attr in Vehicle.__dict__ if attr[0] != '_'}
    except IndexError:
        return create_response(command, WRONG_REQUEST, {'message': 'No id or data specified'})
    else:
        with session_scope() as session:
            vehicle = session.query(Vehicle).filter_by(id=vehicle_attrs.get('id')).first()
            if vehicle:
                for k, v in vehicle_attrs.items():
                    if v:
                        setattr(vehicle, k, v)
                return create_response(command, OK, {'message': 'Vehicle updated'})
            else:
                return create_response(command, NOT_FOUND,
                                       {'message': f'Vehicle with id={vehicle_attrs.get("id")} not found'})


@logged
def delete_vehicle_controller(command):
    try:
        vehicle_id = command.get('data').get('vehicle').get('id')
        if not vehicle_id:
            raise IndexError
    except IndexError:
        return create_response(command, WRONG_REQUEST, {'message': 'No id or data specified'})
    else:
        with session_scope() as session:
            vehicle = session.query(Vehicle).filter_by(id=vehicle_id).first()
            if vehicle:
                session.delete(vehicle)
                return create_response(command, OK, {'message': 'Vehicle deleted'})
            else:
                return create_response(command, NOT_FOUND, {'message': f'Vehicle with id={vehicle_id} not found'})
