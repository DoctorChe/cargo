from PyQt5 import QtCore

from cargo.utils.protocol import create_command


class CityController(QtCore.QObject):
    def __init__(self, view, handler):
        QtCore.QObject.__init__(self)
        self.view = view
        self._handler = handler

        # self.read_all_routes()
        self.read_all_cities()

        self.view.signal_create_city.connect(self.create_city)
        self.view.signal_read_city.connect(self.read_city)
        self.view.signal_update_city.connect(self.update_city)
        self.view.signal_delete_city.connect(self.delete_city)

    def create_city(self, data):
        action = 'create_city'
        self._handler(create_command(action, data))

        self.read_all_cities()

    def read_all_cities(self, data=None):
        action = 'read_all_cities'
        response = self._handler(create_command(action, data))

        cities = response.get('data').get('cities')
        self.view.populate_city_table(cities)

    def read_city(self, data):
        action = 'read_city'
        response = self._handler(create_command(action, data))

        city = response.get('data').get('city')
        self.view.populate_city_card(city)

        # self.read_routes_of_city(data)
        # self.read_warehouses_of_city(data)

    def update_city(self, data):
        action = 'update_city'
        self._handler(create_command(action, data))

        self.read_all_cities()

    def delete_city(self, data):
        action = 'delete_city'
        self._handler(create_command(action, data))

        self.read_all_cities()

    # def read_routes_of_city(self, data):
    #     action = 'read_routes_of_city'
    #     response = self._handler(create_command(action, data))
    #
    #     routes = response.get('data').get('routes')
    #     self.view.populate_routes_table(routes)

    # def read_warehouses_of_city(self, data):
    #     action = 'warehouses_of_city'
    #     response = self._handler(create_command(action, data))
    #
    #     warehouses = response.get('data').get('warehouses')
    #     self.view.populate_warehouses_table(warehouses)
