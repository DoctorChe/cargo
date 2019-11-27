from PyQt5 import QtCore

from cargo.utils.protocol import create_command


class StaffController(QtCore.QObject):
    def __init__(self, view, handler):
        QtCore.QObject.__init__(self)
        self.view = view
        self._handler = handler

        self.read_all_persons()

        self.view.signal_create_person.connect(self.create_person)
        self.view.signal_read_person.connect(self.read_person)
        self.view.signal_update_person.connect(self.update_person)
        self.view.signal_delete_person.connect(self.delete_person)

    def create_person(self, data):
        action = 'create_person'
        self._handler(create_command(action, data))

        self.read_all_persons()

    def read_all_persons(self, data=None):
        action = 'read_all_persons'
        response = self._handler(create_command(action, data))

        persons = response.get('data').get('persons')
        self.view.populate_staff_table(persons)

    def read_person(self, data):
        action = 'read_person'
        response = self._handler(create_command(action, data))

        person = response.get('data').get('person')
        self.view.populate_staff_card(person)

        self.read_routes_of_person(data)

    def update_person(self, data):
        action = 'update_person'
        self._handler(create_command(action, data))

        self.read_all_persons()

    def delete_person(self, data):
        action = 'delete_person'
        self._handler(create_command(action, data))

        self.read_all_persons()

    def read_routes_of_person(self, data):
        action = 'read_routes_of_person'
        response = self._handler(create_command(action, data))

        routes = response.get('data').get('routes')
        self.view.populate_routes_table(routes)
