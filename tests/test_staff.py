import os
import sys
import unittest

from cargo.utils.config import DATABASE
from cargo.utils.db import Base
from cargo.utils.handlers import handler

sys.path.append(os.path.join(os.getcwd(), "../cargo"))

from cargo.app import Cargo
from cargo.staff.models import Person

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
    'person_id': 1,
}

ROUTE2 = {
    'from_warehouse_id': 3,
    'to_warehouse_id': 2,
    'person_id': 1,
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


class TestStaff(unittest.TestCase):

    def setUp(self):
        Base.metadata.create_all()

        self.cargo = Cargo(handler=handler)

    def tearDown(self):
        os.remove(os.path.basename(DATABASE))

    def test_read_all_persons(self):
        cmd = {
            'action': 'read_all_persons',
            'time': 1.1,
            'data': dict(),
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_all_persons',
            'data': {
                'message': 'Persons read',
                'persons': []
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_create_person(self):
        cmd = {
            'action': 'create_person',
            'time': 1.1,
            'data': {'person': {'name': 'Duncan', 'surname': 'MacLeod'}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'create_person',
            'data': {
                'message': 'Person added',
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_person(self):
        cmd = {
            'action': 'create_person',
            'time': 1.1,
            'data': {'person': {'name': 'Duncan', 'surname': 'MacLeod'}},
        }
        self.cargo._handler(cmd)
        cmd = {
            'action': 'read_person',
            'time': 1.1,
            'data': {'person': {'id': 1}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_person',
            'data': {
                'message': 'Person read',
                'person': {
                    'id': 1,
                    'name': 'Duncan',
                    'surname': 'MacLeod',
                    'patronymic': None,
                    'phone': None,
                    'info': None,
                },
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_person_wrong_data(self):
        cmd = {
            'action': 'create_person',
            'time': 1.1,
            'data': {'person': {'name': 'Duncan', 'surname': 'MacLeod'}},
        }
        self.cargo._handler(cmd)
        cmd = {
            'action': 'read_person',
            'time': 1.1,
            'data': {'person': {'id': 999}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_person',
            'data': {
                'message': 'Person with id=999 not found',
            },
            'response': 404,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_person_wrong_request(self):
        cmd = {
            'action': 'create_person',
            'time': 1.1,
            'data': {'person': {'name': 'Duncan', 'surname': 'MacLeod'}},
        }
        self.cargo._handler(cmd)
        cmd = {
            'action': 'read_person',
            'time': 1.1,
            'data': {'person': {}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_person',
            'data': {
                'message': 'No id or data specified',
            },
            'response': 400,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_update_person(self):
        cmd = {
            'action': 'create_person',
            'time': 1.1,
            'data': {'person': {'name': 'Duncan', 'surname': 'MacLeod'}},
        }
        self.cargo._handler(cmd)
        cmd = {
            'action': 'update_person',
            'time': 1.1,
            'data': {'person': {'id': 1, 'name': 'Scotch', 'surname': 'MacLeod'}},
        }
        self.cargo._handler(cmd)
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'update_person',
            'data': {
                'message': 'Person updated',
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)
        cmd = {
            'action': 'read_person',
            'time': 1.1,
            'data': {'person': {'id': 1}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_person',
            'data': {
                'message': 'Person read',
                'person': {
                    'id': 1,
                    'name': 'Scotch',
                    'surname': 'MacLeod',
                    'patronymic': None,
                    'phone': None,
                    'info': None,
                },
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_update_person_wrong_data(self):
        cmd = {
            'action': 'create_person',
            'time': 1.1,
            'data': {'person': {'name': 'Duncan', 'surname': 'MacLeod'}},
        }
        self.cargo._handler(cmd)
        cmd = {
            'action': 'update_person',
            'time': 1.1,
            'data': {'person': {'id': 999, 'name': 'Scotch', 'surname': 'MacLeod'}},
        }
        self.cargo._handler(cmd)
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'update_person',
            'data': {
                'message': 'Person with id=999 not found',
            },
            'response': 404,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_delete_person(self):
        cmd = {
            'action': 'create_person',
            'time': 1.1,
            'data': {'person': {'name': 'Duncan', 'surname': 'MacLeod'}},
        }
        self.cargo._handler(cmd)
        cmd = {
            'action': 'delete_person',
            'time': 1.1,
            'data': {'person': {'id': 1}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'delete_person',
            'data': {
                'message': 'Person deleted',
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_all_routes_by_person(self):
        self.cargo._handler(CREATE_CITY1_COMMAND)
        self.cargo._handler(CREATE_CITY2_COMMAND)
        self.cargo._handler(CREATE_CITY3_COMMAND)
        self.cargo._handler(CREATE_WAREHOUSE1_COMMAND)
        self.cargo._handler(CREATE_WAREHOUSE2_COMMAND)
        self.cargo._handler(CREATE_WAREHOUSE3_COMMAND)
        self.cargo._handler(CREATE_ROUTE1_COMMAND)
        self.cargo._handler(CREATE_ROUTE2_COMMAND)
        self.cargo._handler(CREATE_PERSON1_COMMAND)
        cmd = {
            'action': 'read_routes_of_person',
            'time': 1.1,
            'data':  {'person': {'id': 1}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_routes_of_person',
            'data': {
                'message': 'Routes read',
                'routes': [
                    {
                        'id': 1,
                        'from_warehouse_id': 1,
                        'to_warehouse_id': 2,
                        'load_id': None,
                        'person_id': 1,
                        'vehicle_id': None,
                    },
                    {
                        'id': 2,
                        'from_warehouse_id': 3,
                        'to_warehouse_id': 2,
                        'load_id': None,
                        'person_id': 1,
                        'vehicle_id': None,
                    },
                ]
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)


if __name__ == "__main__":
    unittest.main()
