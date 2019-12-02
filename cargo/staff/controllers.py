from cargo.staff.models import Person
from cargo.utils.config import OK, WRONG_REQUEST, NOT_FOUND
from cargo.utils.db import session_scope

from cargo.utils.decorators import logged
from cargo.utils.protocol import create_response


@logged
def create_person_controller(command):
    data = command.get('data')
    with session_scope() as session:
        person = Person()
        for k, v in data.get('person').items():
            if v:
                setattr(person, k, v)
        session.add(person)
    return create_response(command, OK, {'message': 'Person added'})


@logged
def read_person_controller(command):
    try:
        person_id = command.get('data').get('person').get('id')
        if not person_id:
            raise IndexError
    except IndexError:
        return create_response(command, WRONG_REQUEST, {'message': 'No id or data specified'})
    else:
        with session_scope() as session:
            person = session.query(Person).filter_by(id=person_id).first()
            if person:
                person = {attr: getattr(person, attr) for attr in person.__dict__ if attr[0] != '_'}
                return create_response(command, OK, {'person': person, 'message': 'Person read'})
            else:
                return create_response(command, NOT_FOUND, {'message': f'Person with id={person_id} not found'})


@logged
def read_person_by_fullname_controller(command):
    try:
        person_name = command.get('data').get('person').get('name')
        person_surname = command.get('data').get('person').get('surname')
        person_patronymic = command.get('data').get('person').get('patronymic')
        if not person_name or not person_surname:
            raise IndexError
    except IndexError:
        return create_response(command, WRONG_REQUEST, {'message': 'No id or data specified'})
    else:
        with session_scope() as session:
            if person_patronymic:
                person = session.query(Person).filter_by(name=person_name).filter_by(surname=person_surname).filter_by(
                    patronymic=person_patronymic).first()
            else:
                person = session.query(Person).filter_by(name=person_name).filter_by(surname=person_surname).first()
            if person:
                person = {attr: getattr(person, attr) for attr in person.__dict__ if attr[0] != '_'}
                return create_response(command, OK, {'person': person, 'message': 'Person read'})
            else:
                return create_response(command, NOT_FOUND, {
                    'message': f'Person with name={person_name} and surname={person_surname} not found'})


@logged
def read_persons_controller(command):
    with session_scope() as session:
        persons = session.query(Person).all()
        persons = [{attr: getattr(person, attr) for attr in person.__dict__ if attr[0] != '_'} for person in persons]
        return create_response(command, OK, {'persons': persons, 'message': 'Persons read'})


@logged
def read_routes_of_person_controller(command):
    try:
        person_id = command.get('data').get('person').get('id')
        if not person_id:
            raise IndexError
    except IndexError:
        return create_response(command, WRONG_REQUEST, {'message': 'No id or data specified'})
    else:
        with session_scope() as session:
            person = session.query(Person).filter_by(id=person_id).first()
            if person:
                routes = person.routes
                routes = [{attr: getattr(route, attr) for attr in route.__dict__ if attr[0] != '_'} for route in routes]
                return create_response(command, OK, {'routes': routes, 'message': 'Routes read'})
            else:
                return create_response(command, NOT_FOUND, {'message': f'Person with id={person_id} not found'})


@logged
def update_person_controller(command):
    data = command.get('data')
    try:
        person_attrs = {attr: data.get('person').get(attr) for attr in Person.__dict__ if attr[0] != '_'}
    except IndexError:
        return create_response(command, WRONG_REQUEST, {'message': 'No id or data specified'})
    else:
        with session_scope() as session:
            person = session.query(Person).filter_by(id=person_attrs.get('id')).first()
            if person:
                for k, v in person_attrs.items():
                    if v:
                        setattr(person, k, v)
                return create_response(command, OK, {'message': 'Person updated'})
            else:
                return create_response(command, NOT_FOUND,
                                       {'message': f'Person with id={person_attrs.get("id")} not found'})


@logged
def delete_person_controller(command):
    try:
        person_id = command.get('data').get('person').get('id')
        if not person_id:
            raise IndexError
    except IndexError:
        return create_response(command, WRONG_REQUEST, {'message': 'No id or data specified'})
    else:
        with session_scope() as session:
            person = session.query(Person).filter_by(id=person_id).first()
            if person:
                session.delete(person)
                return create_response(command, OK, {'message': 'Person deleted'})
            else:
                return create_response(command, NOT_FOUND, {'message': f'Person with id={person_id} not found'})
