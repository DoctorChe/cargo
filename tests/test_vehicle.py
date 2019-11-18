import os
import sys
import unittest

from cargo.utils.config import DATABASE
from cargo.utils.db import Base
from cargo.utils.handlers import handler

sys.path.append(os.path.join(os.getcwd(), "../cargo"))

from cargo.app import Cargo
from cargo.vehicle.models import Vehicle

VEHICLE = {
    'model': 'KAMAZ-65207-87',
    'plate': 'a000aa00',
    'payload': 14725,
    'volume': 48.3
}

CREATE_VEHICLE_COMMAND = {
    'action': 'create_vehicle',
    'time': 1.1,
    'data': {'vehicle': VEHICLE},
}


class TestVehicle(unittest.TestCase):

    def setUp(self):
        Base.metadata.create_all()

        self.cargo = Cargo(handler=handler)

    def tearDown(self):
        os.remove(os.path.basename(DATABASE))

    def test_read_all_vehicles(self):
        cmd = {
            'action': 'read_all_vehicles',
            'time': 1.1,
            'data': dict(),
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_all_vehicles',
            'data': {
                'message': 'Vehicles read',
                'vehicles': []
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_create_vehicle(self):
        response = self.cargo._handler(CREATE_VEHICLE_COMMAND)
        expected_response = {
            'action': 'create_vehicle',
            'data': {
                'message': 'Vehicle added',
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_vehicle(self):
        self.cargo._handler(CREATE_VEHICLE_COMMAND)
        cmd = {
            'action': 'read_vehicle',
            'time': 1.1,
            'data': {'vehicle': {'id': 1}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_vehicle',
            'data': {
                'message': 'Vehicle read',
                'vehicle': {
                    'id': 1,
                    'model': 'KAMAZ-65207-87',
                    'plate': 'a000aa00',
                    'year': None,
                    'payload': 14725,
                    'run': None,
                    'fuel_consumption': None,
                    'volume': 48.3,
                },
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_vehicle_wrong_data(self):
        self.cargo._handler(CREATE_VEHICLE_COMMAND)
        cmd = {
            'action': 'read_vehicle',
            'time': 1.1,
            'data': {'vehicle': {'id': 999}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_vehicle',
            'data': {
                'message': 'Vehicle with id=999 not found',
            },
            'response': 404,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_vehicle_wrong_request(self):
        self.cargo._handler(CREATE_VEHICLE_COMMAND)
        cmd = {
            'action': 'read_vehicle',
            'time': 1.1,
            'data': {'vehicle': {}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_vehicle',
            'data': {
                'message': 'No id or data specified',
            },
            'response': 400,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_update_vehicle(self):
        self.cargo._handler(CREATE_VEHICLE_COMMAND)
        cmd = {
            'action': 'update_vehicle',
            'time': 1.1,
            'data': {'vehicle': {'id': 1, 'plate': 'a0001aa00'}},
        }
        self.cargo._handler(cmd)
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'update_vehicle',
            'data': {
                'message': 'Vehicle updated',
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)
        cmd = {
            'action': 'read_vehicle',
            'time': 1.1,
            'data': {'vehicle': {'id': 1}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_vehicle',
            'data': {
                'message': 'Vehicle read',
                'vehicle': {
                    'id': 1,
                    'model': 'KAMAZ-65207-87',
                    'plate': 'a0001aa00',
                    'year': None,
                    'payload': 14725,
                    'run': None,
                    'fuel_consumption': None,
                    'volume': 48.3,
                },
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_update_vehicle_wrong_data(self):
        self.cargo._handler(CREATE_VEHICLE_COMMAND)
        cmd = {
            'action': 'update_vehicle',
            'time': 1.1,
            'data': {'vehicle': {'id': 999, 'plate': 'a0001aa00'}},
        }
        self.cargo._handler(cmd)
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'update_vehicle',
            'data': {
                'message': 'Vehicle with id=999 not found',
            },
            'response': 404,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_delete_vehicle(self):
        self.cargo._handler(CREATE_VEHICLE_COMMAND)
        cmd = {
            'action': 'delete_vehicle',
            'time': 1.1,
            'data': {'vehicle': {'id': 1}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'delete_vehicle',
            'data': {
                'message': 'Vehicle deleted',
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)


if __name__ == "__main__":
    unittest.main()
