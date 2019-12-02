from PyQt5 import QtCore

from cargo.utils.protocol import create_command


class VehicleController(QtCore.QObject):
    def __init__(self, view, handler):
        QtCore.QObject.__init__(self)
        self.view = view
        self._handler = handler

        self.read_all_vehicles()

        self.view.signal_create_vehicle.connect(self.create_vehicle)
        self.view.signal_read_vehicle.connect(self.read_vehicle)
        self.view.signal_update_vehicle.connect(self.update_vehicle)
        self.view.signal_delete_vehicle.connect(self.delete_vehicle)

    def create_vehicle(self, data):
        action = 'create_vehicle'
        self._handler(create_command(action, data))

        self.read_all_vehicles()

    def read_all_vehicles(self, data=None):
        action = 'read_all_vehicles'
        response = self._handler(create_command(action, data))

        vehicles = response.get('data').get('vehicles')
        self.view.populate_vehicle_table(vehicles)

    def read_vehicle(self, data):
        action = 'read_vehicle'
        response = self._handler(create_command(action, data))

        vehicle = response.get('data').get('vehicle')
        self.view.populate_vehicle_card(vehicle)

        self.read_routes_of_vehicle(data)

    def update_vehicle(self, data):
        action = 'update_vehicle'
        self._handler(create_command(action, data))

        self.read_all_vehicles()

    def delete_vehicle(self, data):
        action = 'delete_vehicle'
        self._handler(create_command(action, data))

        self.read_all_vehicles()

    def read_routes_of_vehicle(self, data):
        action = 'read_routes_of_vehicle'
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
