from cargo.load.models import Load
from cargo.utils.config import OK, WRONG_REQUEST, NOT_FOUND
from cargo.utils.db import session_scope

from cargo.utils.decorators import logged
from cargo.utils.protocol import create_response


@logged
def create_load_controller(command):
    data = command.get('data')
    with session_scope() as session:
        load = Load()
        for k, v in data.get('load').items():
            if v:
                setattr(load, k, v)
        session.add(load)
    return create_response(command, OK, {'message': 'Load added'})


@logged
def read_load_controller(command):
    try:
        load_id = command.get('data').get('load').get('id')
        if not load_id:
            raise IndexError
    except IndexError:
        return create_response(command, WRONG_REQUEST, {'message': 'No id or data specified'})
    else:
        with session_scope() as session:
            load = session.query(Load).filter_by(id=load_id).first()
            if load:
                load = {attr: getattr(load, attr) for attr in load.__dict__ if attr[0] != '_'}
                return create_response(command, OK, {'load': load, 'message': 'Load read'})
            else:
                return create_response(command, NOT_FOUND, {'message': f'Load with id={load_id} not found'})


@logged
def read_load_by_info_controller(command):
    try:
        load_info = command.get('data').get('load').get('info')
        if not load_info:
            raise IndexError
    except IndexError:
        return create_response(command, WRONG_REQUEST, {'message': 'No id or data specified'})
    else:
        with session_scope() as session:
            load = session.query(Load).filter_by(info=load_info).first()
            if load:
                load = {attr: getattr(load, attr) for attr in load.__dict__ if attr[0] != '_'}
                return create_response(command, OK, {'load': load, 'message': 'Load read'})
            else:
                return create_response(command, NOT_FOUND, {'message': f'Load with info={load_info} not found'})


@logged
def read_loads_controller(command):
    with session_scope() as session:
        loads = session.query(Load).all()
        loads = [{attr: getattr(load, attr) for attr in load.__dict__ if attr[0] != '_'}
                 for load in loads]
        return create_response(command, OK, {'loads': loads, 'message': 'Loads read'})


@logged
def update_load_controller(command):
    data = command.get('data')
    try:
        load_attrs = {attr: data.get('load').get(attr) for attr in Load.__dict__ if attr[0] != '_'}
    except IndexError:
        return create_response(command, WRONG_REQUEST, {'message': 'No id or data specified'})
    else:
        with session_scope() as session:
            load = session.query(Load).filter_by(id=load_attrs.get('id')).first()
            if load:
                for k, v in load_attrs.items():
                    if v:
                        setattr(load, k, v)
                return create_response(command, OK, {'message': 'Load updated'})
            else:
                return create_response(command, NOT_FOUND,
                                       {'message': f'Load with id={load_attrs.get("id")} not found'})


@logged
def delete_load_controller(command):
    try:
        load_id = command.get('data').get('load').get('id')
        if not load_id:
            raise IndexError
    except IndexError:
        return create_response(command, WRONG_REQUEST, {'message': 'No id or data specified'})
    else:
        with session_scope() as session:
            load = session.query(Load).filter_by(id=load_id).first()
            if load:
                session.delete(load)
                return create_response(command, OK, {'message': 'Load deleted'})
            else:
                return create_response(command, NOT_FOUND, {'message': f'Load with id={load_id} not found'})
