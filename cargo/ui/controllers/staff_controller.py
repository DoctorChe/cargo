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
        for route in routes:
            from_warehouse = {'warehouse': {'id': route.get('from_warehouse_id')}}
            route['from_warehouse'] = self.get_warehouse_full_address_by_id(from_warehouse)
            to_warehouse = {'warehouse': {'id': route.get('to_warehouse_id')}}
            route['to_warehouse'] = self.get_warehouse_full_address_by_id(to_warehouse)
        self.view.populate_routes_table(routes)

    def get_warehouse_full_address_by_id(self, data):
        action = 'read_warehouse'
        response = self._handler(create_command(action, data))

        warehouse = response.get('data').get('warehouse')

        cities = self.read_all_cities()
        city_id = warehouse.get('city_id')
        city_name = ''
        for city in cities:
            if city_id == city.get('id'):
                city_name = city.get('name')
                break
        warehouse = f"{warehouse.get('address')} ({city_name})"

        return warehouse

    def read_all_cities(self, data=None):
        action = 'read_all_cities'
        response = self._handler(create_command(action, data))
        cities = response.get('data').get('cities')
        return cities
