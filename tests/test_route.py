import os
import sys
import unittest

from cargo.utils.config import DATABASE
from cargo.utils.db import Base
from cargo.utils.handlers import handler

sys.path.append(os.path.join(os.getcwd(), "../cargo"))

from cargo.app import Cargo
from cargo.route.models import City, Warehouse, Route

CITY1 = {
    'name': 'Moscow',
}

CITY2 = {
    'name': 'SPb',
}

CITY3 = {
    'name': 'Barnaul',
}

CREATE_CITY1_COMMAND = {
    'action': 'create_city',
    'time': 1.1,
    'data': {'city': CITY1},
}

CREATE_CITY2_COMMAND = {
    'action': 'create_city',
    'time': 1.1,
    'data': {'city': CITY2},
}

CREATE_CITY3_COMMAND = {
    'action': 'create_city',
    'time': 1.1,
    'data': {'city': CITY3},
}

WAREHOUSE1 = {
    'address': 'пр. Ленина 51',
    'city_id': 1,
}

WAREHOUSE2 = {
    'address': 'пр. К.Маркса 1',
    'city_id': 2,
}

WAREHOUSE3 = {
    'address': 'пр. Калинина 1',
    'city_id': 3,
}

CREATE_WAREHOUSE1_COMMAND = {
    'action': 'create_warehouse',
    'time': 1.1,
    'data': {'warehouse': WAREHOUSE1},
}

CREATE_WAREHOUSE2_COMMAND = {
    'action': 'create_warehouse',
    'time': 1.1,
    'data': {'warehouse': WAREHOUSE2},
}

CREATE_WAREHOUSE3_COMMAND = {
    'action': 'create_warehouse',
    'time': 1.1,
    'data': {'warehouse': WAREHOUSE3},
}

ROUTE1 = {
    'from_warehouse_id': 1,
    'to_warehouse_id': 2,
}

ROUTE2 = {
    'from_warehouse_id': 3,
    'to_warehouse_id': 2,
}

CREATE_ROUTE1_COMMAND = {
    'action': 'create_route',
    'time': 1.1,
    'data': {
        'route': ROUTE1,
    },
}

CREATE_ROUTE2_COMMAND = {
    'action': 'create_route',
    'time': 1.1,
    'data': {
        'route': ROUTE2,
    },
}

PERSON1 = {
    'name': 'Duncan',
    'surname': 'MacLeod'
}

CREATE_PERSON1_COMMAND = {
    'action': 'create_person',
    'time': 1.1,
    'data': {
        'person': PERSON1,
    },
}


class TestCity(unittest.TestCase):

    def setUp(self):
        Base.metadata.create_all()
        self.cargo = Cargo(handler=handler)

    def tearDown(self):
        os.remove(os.path.basename(DATABASE))

    def test_create_city(self):
        response = self.cargo._handler(CREATE_CITY1_COMMAND)
        expected_response = {
            'action': 'create_city',
            'data': {
                'message': 'City added',
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_city(self):
        self.cargo._handler(CREATE_CITY1_COMMAND)
        cmd = {
            'action': 'read_city',
            'time': 1.1,
            'data': {'city': {'id': 1}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_city',
            'data': {
                'message': 'City read',
                'city': {
                    'id': 1,
                    'name': 'Moscow',
                },
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_city_wrong_data(self):
        self.cargo._handler(CREATE_CITY1_COMMAND)
        cmd = {
            'action': 'read_city',
            'time': 1.1,
            'data': {'city': {'id': 999}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_city',
            'data': {
                'message': 'City with id=999 not found',
            },
            'response': 404,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_city_wrong_request(self):
        self.cargo._handler(CREATE_CITY1_COMMAND)
        cmd = {
            'action': 'read_city',
            'time': 1.1,
            'data': {'city': {}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_city',
            'data': {
                'message': 'No id or data specified',
            },
            'response': 400,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_all_cities_empty(self):
        cmd = {
            'action': 'read_all_cities',
            'time': 1.1,
            'data': dict(),
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_all_cities',
            'data': {
                'message': 'Cities read',
                'cities': []
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_all_cities(self):
        self.cargo._handler(CREATE_CITY1_COMMAND)
        self.cargo._handler(CREATE_CITY2_COMMAND)
        cmd = {
            'action': 'read_all_cities',
            'time': 1.1,
            'data': dict(),
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_all_cities',
            'data': {
                'message': 'Cities read',
                'cities': [
                    {'id': 1, 'name': 'Moscow'},
                    {'id': 2, 'name': 'SPb'},
                ]
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_update_city(self):
        self.cargo._handler(CREATE_CITY1_COMMAND)
        cmd = {
            'action': 'update_city',
            'time': 1.1,
            'data': {'city': {
                'id': 1,
                'name': 'Barnaul',
            }},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'update_city',
            'data': {
                'message': 'City updated',
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)
        cmd = {
            'action': 'read_city',
            'time': 1.1,
            'data': {'city': {'id': 1}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_city',
            'data': {
                'message': 'City read',
                'city': {
                    'id': 1,
                    'name': 'Barnaul',
                },
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_update_city_wrong_data(self):
        self.cargo._handler(CREATE_CITY1_COMMAND)
        cmd = {
            'action': 'update_city',
            'time': 1.1,
            'data': {'city': {
                'id': 999,
                'name': 'Barnaul',
            }},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'update_city',
            'data': {
                'message': 'City with id=999 not found',
            },
            'response': 404,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_delete_city(self):
        self.cargo._handler(CREATE_CITY1_COMMAND)
        cmd = {
            'action': 'delete_city',
            'time': 1.1,
            'data': {'city': {'id': 1}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'delete_city',
            'data': {
                'message': 'City deleted',
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)


class TestWarehouse(unittest.TestCase):

    def setUp(self):
        Base.metadata.create_all()
        self.cargo = Cargo(handler=handler)

    def tearDown(self):
        os.remove(os.path.basename(DATABASE))

    def test_create_warehouse(self):
        self.cargo._handler(CREATE_CITY1_COMMAND)
        self.cargo._handler(CREATE_CITY2_COMMAND)
        response = self.cargo._handler(CREATE_WAREHOUSE1_COMMAND)
        expected_response = {
            'action': 'create_warehouse',
            'data': {
                'message': 'Warehouse added',
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_warehouse(self):
        self.cargo._handler(CREATE_CITY1_COMMAND)
        self.cargo._handler(CREATE_CITY2_COMMAND)
        self.cargo._handler(CREATE_WAREHOUSE1_COMMAND)
        cmd = {
            'action': 'read_warehouse',
            'time': 1.1,
            'data': {'warehouse': {'id': 1}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_warehouse',
            'data': {
                'message': 'Warehouse read',
                'warehouse': {
                    'id': 1,
                    'address': 'пр. Ленина 51',
                    'city_id': 1,
                },
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_warehouse_wrong_data(self):
        self.cargo._handler(CREATE_CITY1_COMMAND)
        self.cargo._handler(CREATE_CITY2_COMMAND)
        self.cargo._handler(CREATE_WAREHOUSE1_COMMAND)
        cmd = {
            'action': 'read_warehouse',
            'time': 1.1,
            'data': {'warehouse': {'id': 999}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_warehouse',
            'data': {
                'message': 'Warehouse with id=999 not found',
            },
            'response': 404,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_warehouse_wrong_request(self):
        self.cargo._handler(CREATE_CITY1_COMMAND)
        self.cargo._handler(CREATE_CITY2_COMMAND)
        self.cargo._handler(CREATE_WAREHOUSE1_COMMAND)
        cmd = {
            'action': 'read_warehouse',
            'time': 1.1,
            'data': {'warehouse': {}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_warehouse',
            'data': {
                'message': 'No id or data specified',
            },
            'response': 400,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_all_warehouses_empty(self):
        cmd = {
            'action': 'read_all_warehouses',
            'time': 1.1,
            'data': dict(),
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_all_warehouses',
            'data': {
                'message': 'Warehouses read',
                'warehouses': []
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_all_warehouses(self):
        self.cargo._handler(CREATE_CITY1_COMMAND)
        self.cargo._handler(CREATE_CITY2_COMMAND)
        self.cargo._handler(CREATE_WAREHOUSE1_COMMAND)
        self.cargo._handler(CREATE_WAREHOUSE2_COMMAND)
        cmd = {
            'action': 'read_all_warehouses',
            'time': 1.1,
            'data': dict(),
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_all_warehouses',
            'data': {
                'message': 'Warehouses read',
                'warehouses': [
                    {
                        'id': 1,
                        'address': 'пр. Ленина 51',
                        'city_id': 1,
                    },
                    {
                        'id': 2,
                        'address': 'пр. К.Маркса 1',
                        'city_id': 2,
                    },
                ]
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_update_warehouse(self):
        self.cargo._handler(CREATE_CITY1_COMMAND)
        self.cargo._handler(CREATE_WAREHOUSE1_COMMAND)
        cmd = {
            'action': 'update_warehouse',
            'time': 1.1,
            'data': {'warehouse': {
                'id': 1,
                'address': 'ул. Советская 2',
            }},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'update_warehouse',
            'data': {
                'message': 'Warehouse updated',
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)
        cmd = {
            'action': 'read_warehouse',
            'time': 1.1,
            'data': {'warehouse': {'id': 1}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_warehouse',
            'data': {
                'message': 'Warehouse read',
                'warehouse': {
                    'id': 1,
                    'address': 'ул. Советская 2',
                    'city_id': 1,
                },
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_update_warehouse_wrong_data(self):
        self.cargo._handler(CREATE_CITY1_COMMAND)
        self.cargo._handler(CREATE_WAREHOUSE1_COMMAND)
        cmd = {
            'action': 'update_warehouse',
            'time': 1.1,
            'data': {'warehouse': {
                'id': 999,
                'address': 'ул. Советская 2',
            }},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'update_warehouse',
            'data': {
                'message': 'Warehouse with id=999 not found',
            },
            'response': 404,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_delete_warehouse(self):
        self.cargo._handler(CREATE_CITY1_COMMAND)
        self.cargo._handler(CREATE_WAREHOUSE1_COMMAND)
        cmd = {
            'action': 'delete_warehouse',
            'time': 1.1,
            'data': {'warehouse': {'id': 1}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'delete_warehouse',
            'data': {
                'message': 'Warehouse deleted',
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)


class TestRoute(unittest.TestCase):

    def setUp(self):
        Base.metadata.create_all()
        self.cargo = Cargo(handler=handler)

    def tearDown(self):
        os.remove(os.path.basename(DATABASE))

    def test_create_route(self):
        self.cargo._handler(CREATE_WAREHOUSE1_COMMAND)
        self.cargo._handler(CREATE_WAREHOUSE2_COMMAND)
        response = self.cargo._handler(CREATE_ROUTE1_COMMAND)
        expected_response = {
            'action': 'create_route',
            'data': {
                'message': 'Route added',
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_route(self):
        self.cargo._handler(CREATE_WAREHOUSE1_COMMAND)
        self.cargo._handler(CREATE_WAREHOUSE2_COMMAND)
        self.cargo._handler(CREATE_ROUTE1_COMMAND)
        cmd = {
            'action': 'read_route',
            'time': 1.1,
            'data': {'route': {'id': 1}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_route',
            'data': {
                'message': 'Route read',
                'route': {
                    'id': 1,
                    'from_warehouse_id': 1,
                    'to_warehouse_id': 2,
                    'load_id': None,
                    'person_id': None,
                    'vehicle_id': None,
                },
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_route_wrong_data(self):
        self.cargo._handler(CREATE_ROUTE1_COMMAND)
        cmd = {
            'action': 'read_route',
            'time': 1.1,
            'data': {'route': {'id': 999}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_route',
            'data': {
                'message': 'Route with id=999 not found',
            },
            'response': 404,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_route_wrong_request(self):
        self.cargo._handler(CREATE_ROUTE1_COMMAND)
        cmd = {
            'action': 'read_route',
            'time': 1.1,
            'data': {'route': {}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_route',
            'data': {
                'message': 'No id or data specified',
            },
            'response': 400,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_all_routes_empty(self):
        cmd = {
            'action': 'read_all_routes',
            'time': 1.1,
            'data': dict(),
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_all_routes',
            'data': {
                'message': 'Routes read',
                'routes': []
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_all_routes(self):
        self.cargo._handler(CREATE_CITY1_COMMAND)
        self.cargo._handler(CREATE_CITY2_COMMAND)
        self.cargo._handler(CREATE_CITY3_COMMAND)
        self.cargo._handler(CREATE_WAREHOUSE1_COMMAND)
        self.cargo._handler(CREATE_WAREHOUSE2_COMMAND)
        self.cargo._handler(CREATE_WAREHOUSE3_COMMAND)
        self.cargo._handler(CREATE_ROUTE1_COMMAND)
        self.cargo._handler(CREATE_ROUTE2_COMMAND)
        cmd = {
            'action': 'read_all_routes',
            'time': 1.1,
            'data': dict(),
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_all_routes',
            'data': {
                'message': 'Routes read',
                'routes': [
                    {
                        'id': 1,
                        'from_warehouse_id': 1,
                        'to_warehouse_id': 2,
                        'load_id': None,
                        'person_id': None,
                        'vehicle_id': None,
                    },
                    {
                        'id': 2,
                        'from_warehouse_id': 3,
                        'to_warehouse_id': 2,
                        'load_id': None,
                        'person_id': None,
                        'vehicle_id': None,
                    },
                ]
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_update_route(self):
        self.cargo._handler(CREATE_CITY3_COMMAND)
        self.cargo._handler(CREATE_WAREHOUSE3_COMMAND)
        self.cargo._handler(CREATE_ROUTE1_COMMAND)
        cmd = {
            'action': 'update_route',
            'time': 1.1,
            'data': {'route': {
                'id': 1,
                'from_warehouse_id': 3,
            }},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'update_route',
            'data': {
                'message': 'Route updated',
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)
        cmd = {
            'action': 'read_route',
            'time': 1.1,
            'data': {'route': {'id': 1}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_route',
            'data': {
                'message': 'Route read',
                'route': {
                    'id': 1,
                    'from_warehouse_id': 3,
                    'to_warehouse_id': 2,
                    'load_id': None,
                    'person_id': None,
                    'vehicle_id': None,
                },
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_update_route_wrong_data(self):
        self.cargo._handler(CREATE_ROUTE1_COMMAND)
        cmd = {
            'action': 'update_route',
            'time': 1.1,
            'data': {'route': {
                'id': 999,
                'from_warehouse_id': 3,
            }},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'update_route',
            'data': {
                'message': 'Route with id=999 not found',
            },
            'response': 404,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_delete_route(self):
        self.cargo._handler(CREATE_ROUTE1_COMMAND)
        cmd = {
            'action': 'delete_route',
            'time': 1.1,
            'data': {'route': {'id': 1}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'delete_route',
            'data': {
                'message': 'Route deleted',
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)


if __name__ == "__main__":
    unittest.main()
