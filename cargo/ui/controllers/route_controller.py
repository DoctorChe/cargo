from PyQt5 import QtCore

from cargo.utils.protocol import create_command


class RouteController(QtCore.QObject):
    def __init__(self, view, handler):
        QtCore.QObject.__init__(self)
        self.view = view
        self._handler = handler

        self.read_all_warehouses()
        self.read_all_persons()
        self.read_all_vehicles()
        self.read_all_loads()
        self.read_all_routes()

        self.view.signal_create_route.connect(self.create_route)
        self.view.signal_read_route.connect(self.read_route)
        self.view.signal_update_route.connect(self.update_route)
        self.view.signal_delete_route.connect(self.delete_route)

        self.view.signal_get_from_warehouse_id_by_full_address.connect(self.get_from_warehouse_id_by_full_address)
        self.view.signal_get_to_warehouse_id_by_full_address.connect(self.get_to_warehouse_id_by_full_address)
        self.view.signal_get_person_id_by_fullname.connect(self.get_person_id_by_fullname)
        self.view.signal_get_vehicle_id_by_plate.connect(self.get_vehicle_id_by_plate)
        self.view.signal_get_load_id_by_info.connect(self.get_load_id_by_info)

    def create_route(self, data):
        action = 'create_route'
        self._handler(create_command(action, data))

        self.read_all_routes()

    def read_all_routes(self, data=None):
        action = 'read_all_routes'
        response = self._handler(create_command(action, data))

        routes = response.get('data').get('routes')

        for route in routes:

            from_warehouse_id = route.get('from_warehouse_id')
            if from_warehouse_id is not None:
                warehouse = {'warehouse': {
                    'id': from_warehouse_id
                }}
                route['from_warehouse'] = self.get_warehouse_full_address_by_id(warehouse)

            to_warehouse_id = route.get('to_warehouse_id')
            if to_warehouse_id is not None:
                warehouse = {'warehouse': {
                    'id': to_warehouse_id
                }}
                route['to_warehouse'] = self.get_warehouse_full_address_by_id(warehouse)

            person_id = route.get('person_id')
            if person_id is not None:
                person = {'person': {
                    'id': person_id
                }}
                route['person'] = self.get_person_fullname_by_id(person)

            vehicle_id = route.get('vehicle_id')
            if vehicle_id is not None:
                vehicle = {'vehicle': {
                    'id': vehicle_id
                }}
                route['vehicle'] = self.read_vehicle(vehicle).get('plate')

            load_id = route.get('load_id')
            if load_id is not None:
                load = {'load': {
                    'id': load_id
                }}
                route['load'] = self.read_load(load).get('info')

        self.view.populate_route_table(routes)

    def read_route(self, data):
        action = 'read_route'
        response = self._handler(create_command(action, data))

        route = response.get('data').get('route')

        from_warehouse_id = route.get('from_warehouse_id')
        if from_warehouse_id is not None:
            warehouse = {'warehouse': {
                'id': from_warehouse_id
            }}
            route['from_warehouse'] = self.get_warehouse_full_address_by_id(warehouse)

        to_warehouse_id = route.get('to_warehouse_id')
        if to_warehouse_id is not None:
            warehouse = {'warehouse': {
                'id': to_warehouse_id
            }}
            route['to_warehouse'] = self.get_warehouse_full_address_by_id(warehouse)

        person_id = route.get('person_id')
        if person_id is not None:
            person = {'person': {
                'id': person_id
            }}
            route['person'] = self.get_person_fullname_by_id(person)

        vehicle_id = route.get('vehicle_id')
        if vehicle_id is not None:
            vehicle = {'vehicle': {
                'id': vehicle_id
            }}
            route['vehicle'] = self.read_vehicle(vehicle).get('plate')

        load_id = route.get('load_id')
        if load_id is not None:
            load = {'load': {
                'id': load_id
            }}
            route['load'] = self.read_load(load).get('info')

        self.view.populate_route_card(route)

    def update_route(self, data):
        action = 'update_route'
        self._handler(create_command(action, data))

        self.read_all_routes()

    def delete_route(self, data):
        action = 'delete_route'
        self._handler(create_command(action, data))

        self.read_all_routes()

    def read_all_cities(self, data=None):
        action = 'read_all_cities'
        response = self._handler(create_command(action, data))
        cities = response.get('data').get('cities')
        return cities

    def read_all_warehouses(self, data=None):
        action = 'read_all_warehouses'
        response = self._handler(create_command(action, data))

        warehouses = response.get('data').get('warehouses')
        cities = self.read_all_cities()
        warehouses_list = []
        for warehouse in warehouses:
            address = warehouse.get('address')
            city_id = warehouse.get('city_id')
            city_name = ''
            for city in cities:
                if city_id == city.get('id'):
                    city_name = city.get('name')
                    break
            warehouses_list.append(f"{address} ({city_name})")
        self.view.populate_from_warehouse_combobox(warehouses_list)
        self.view.populate_to_warehouse_combobox(warehouses_list)

    def read_all_persons(self, data=None):
        action = 'read_all_persons'
        response = self._handler(create_command(action, data))

        persons = response.get('data').get('persons')
        persons = [f"{person['name']} {person['surname']} {person['patronymic'] or ''}".strip() for person in persons]
        self.view.populate_persons_combobox(persons)

    def read_all_vehicles(self, data=None):
        action = 'read_all_vehicles'
        response = self._handler(create_command(action, data))

        vehicles = response.get('data').get('vehicles')
        vehicles = [vehicle['plate'] for vehicle in vehicles]
        self.view.populate_vehicles_combobox(vehicles)

    def read_all_loads(self, data=None):
        action = 'read_all_loads'
        response = self._handler(create_command(action, data))

        loads = response.get('data').get('loads')
        loads = [load['info'] for load in loads]
        self.view.populate_loads_combobox(loads)

    def get_person_fullname_by_id(self, data):
        action = 'read_person'
        response = self._handler(create_command(action, data))

        person = response.get('data').get('person')
        return f"{person['name']} {person['surname']} {person['patronymic'] or ''}".strip()

    def get_person_id_by_fullname(self, data):
        action = 'read_person_by_fullname'
        response = self._handler(create_command(action, data))

        person = response.get('data').get('person')
        self.view.person_id = person.get('id')
        return person.get('id')

    def get_from_warehouse_id_by_full_address(self, data):
        action = 'read_warehouse_by_full_address'
        response = self._handler(create_command(action, data))

        warehouse = response.get('data').get('warehouse')
        self.view.from_warehouse_id = warehouse.get('id')

    def get_to_warehouse_id_by_full_address(self, data):
        action = 'read_warehouse_by_full_address'
        response = self._handler(create_command(action, data))

        warehouse = response.get('data').get('warehouse')
        self.view.to_warehouse_id = warehouse.get('id')

    def read_vehicle(self, data):
        action = 'read_vehicle'
        response = self._handler(create_command(action, data))

        vehicle = response.get('data').get('vehicle')
        return vehicle

    def get_vehicle_id_by_plate(self, data):
        action = 'read_vehicle_by_plate'
        response = self._handler(create_command(action, data))

        vehicle = response.get('data').get('vehicle')
        self.view.vehicle_id = vehicle.get('id')
        # return vehicle

    def read_load(self, data):
        action = 'read_load'
        response = self._handler(create_command(action, data))

        load = response.get('data').get('load')
        return load

    def get_load_id_by_info(self, data):
        action = 'read_load_by_info'
        response = self._handler(create_command(action, data))

        load = response.get('data').get('load')
        self.view.load_id = load.get('id')

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
