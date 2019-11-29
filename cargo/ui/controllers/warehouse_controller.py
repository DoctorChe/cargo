from PyQt5 import QtCore

from cargo.utils.protocol import create_command


class WarehouseController(QtCore.QObject):
    def __init__(self, view, handler):
        QtCore.QObject.__init__(self)
        self.view = view
        self._handler = handler

        self.read_all_cities()
        self.read_all_warehouses()

        self.view.signal_create_warehouse.connect(self.create_warehouse)
        self.view.signal_read_warehouse.connect(self.read_warehouse)
        self.view.signal_update_warehouse.connect(self.update_warehouse)
        self.view.signal_delete_warehouse.connect(self.delete_warehouse)

        self.view.signal_get_city_id_by_name.connect(self.get_city_id_by_name)
        self.view.signal_get_city_name_by_id.connect(self.get_city_name_by_id)
        self.view.signal_get_all_cities.connect(self.read_all_cities)

    def create_warehouse(self, data):
        action = 'create_warehouse'
        self._handler(create_command(action, data))

        self.read_all_warehouses()

    def read_all_warehouses(self, data=None):
        action = 'read_all_warehouses'
        response = self._handler(create_command(action, data))

        warehouses = response.get('data').get('warehouses')

        for warehouse in warehouses:
            city_id = warehouse.get('city_id')
            if city_id is not None:
                city = {'city': {
                    'id': city_id
                }}
                warehouse['city'] = self.get_city_name_by_id(city)

        self.view.populate_warehouse_table(warehouses)

    def read_warehouse(self, data):
        action = 'read_warehouse'
        response = self._handler(create_command(action, data))

        warehouse = response.get('data').get('warehouse')

        city_id = warehouse.get('id')
        if city_id is not None:
            city = {'city': {
                'id': city_id
            }}
            warehouse['city'] = self.get_city_name_by_id(city)

        self.view.populate_warehouse_card(warehouse)

        # self.read_routes_of_warehouse(data)

    def update_warehouse(self, data):
        action = 'update_warehouse'
        self._handler(create_command(action, data))

        self.read_all_warehouses()

    def delete_warehouse(self, data):
        action = 'delete_warehouse'
        self._handler(create_command(action, data))

        self.read_all_warehouses()

    def read_routes_of_warehouse(self, data):
        action = 'read_routes_of_warehouse'
        response = self._handler(create_command(action, data))

        routes = response.get('data').get('routes')
        self.view.populate_routes_table(routes)

    def read_all_cities(self, data=None):
        action = 'read_all_cities'
        response = self._handler(create_command(action, data))

        cities = response.get('data').get('cities')
        self.view.cities = cities
        cities = [city['name'] for city in cities]
        self.view.populate_cities_combobox(cities)

    def get_city_id_by_name(self, data):
        action = 'read_city_id_by_name'
        response = self._handler(create_command(action, data))

        city = response.get('data').get('city')
        self.view.city_id = city.get('id')

    def get_city_name_by_id(self, data):
        action = 'read_city'
        response = self._handler(create_command(action, data))

        city = response.get('data').get('city')
        return city.get('name')
