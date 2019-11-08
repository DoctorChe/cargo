from cargo.staff.models import Person
from cargo.utils.db import session_scope

from cargo.utils.decorators import logged
from cargo.utils.protocol import create_response


@logged
def create_person_controller(command):
    data = command.get('data')
    with session_scope() as session:
        person = data.get('person')
        p = Person(
            name=person.get('name'),
            surname=person.get('surname'),
            patronymic=person.get('patronymic'),
            phone=person.get('phone'),
            info=person.get('info'),
        )
        session.add(p)
    return create_response(command, 'Person added')


@logged
def read_persons_controller(command):
    with session_scope() as session:
        persons = session.query(Person).all()
        return create_response(command, 'Persons read', {'persons': persons})


@logged
def update_person_controller(command):
    data = command.get('data')
    try:
        person = data.get('person')
        person_id = person.get('id')
        name = person.get('name')
        surname = person.get('surname')
        patronymic = person.get('patronymic')
        phone = person.get('phone')
        info = person.get('info')
    except IndexError:
        return create_response(command, 'WRONG_REQUEST', {'message': 'Не задан id или данные'})
    else:
        with session_scope() as session:
            p = session.query(Person).filter_by(id=person_id).first()
            p.name = name
            p.surname = surname
            p.patronymic = patronymic
            p.phone = phone
            p.info = info
        return create_response(command, 'OK')


@logged
def delete_person_controller(command):
    try:
        person_id = command.get('data').get('person').get('id')
    except IndexError:
        return create_response(command, 'WRONG_REQUEST', {'message': 'Не задан id или данные'})
    else:
        with session_scope() as session:
            p = session.query(Person).filter_by(id=person_id).first()
            session.delete(p)
        return create_response(command, 'OK')
