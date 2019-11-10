import os
import sys
import unittest

from cargo.utils.config import DATABASE
from cargo.utils.db import Base
from cargo.utils.handlers import handler

sys.path.append(os.path.join(os.getcwd(), "../cargo"))

from cargo.app import Cargo

LOAD = {
    'length': 1.1,
    'height': 1.1,
    'width': 1.1,
    'weight': 1.1,
    'load_from': 'Москва',
    'load_to': 'СПб',
}

CREATE_LOAD_COMMAND = {
    'action': 'create_load',
    'time': 1.1,
    'data': {'load': LOAD},
}


class TestLoad(unittest.TestCase):

    def setUp(self):
        Base.metadata.create_all()

        self.cargo = Cargo(handler=handler)

    def tearDown(self):
        os.remove(os.path.basename(DATABASE))

    def test_read_all_loads(self):
        cmd = {
            'action': 'read_all_loads',
            'time': 1.1,
            'data': dict(),
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_all_loads',
            'data': {
                'message': 'Loads read',
                'loads': []
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_create_load(self):
        response = self.cargo._handler(CREATE_LOAD_COMMAND)
        expected_response = {
            'action': 'create_load',
            'data': {
                'message': 'Load added',
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_load(self):
        self.cargo._handler(CREATE_LOAD_COMMAND)
        cmd = {
            'action': 'read_load',
            'time': 1.1,
            'data': {'load': {'id': 1}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_load',
            'data': {
                'message': 'Load read',
                'load': {
                    'id': 1,
                    'length': 1.1,
                    'height': 1.1,
                    'width': 1.1,
                    'weight': 1.1,
                    'load_from': 'Москва',
                    'load_to': 'СПб',
                    'info': None,
                },
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_load_wrong_data(self):
        self.cargo._handler(CREATE_LOAD_COMMAND)
        cmd = {
            'action': 'read_load',
            'time': 1.1,
            'data': {'load': {'id': 999}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_load',
            'data': {
                'message': 'Load with id=999 not found',
            },
            'response': 404,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_read_load_wrong_request(self):
        self.cargo._handler(CREATE_LOAD_COMMAND)
        cmd = {
            'action': 'read_load',
            'time': 1.1,
            'data': {'load': {}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_load',
            'data': {
                'message': 'No id or data specified',
            },
            'response': 400,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_update_load(self):
        self.cargo._handler(CREATE_LOAD_COMMAND)
        cmd = {
            'action': 'update_load',
            'time': 1.1,
            'data': {'load': {'id': 1, 'length': 2.2}},
        }
        self.cargo._handler(cmd)
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'update_load',
            'data': {
                'message': 'Load updated',
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)
        cmd = {
            'action': 'read_load',
            'time': 1.1,
            'data': {'load': {'id': 1}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'read_load',
            'data': {
                'message': 'Load read',
                'load': {
                    'id': 1,
                    'length': 2.2,
                    'height': 1.1,
                    'width': 1.1,
                    'weight': 1.1,
                    'load_from': 'Москва',
                    'load_to': 'СПб',
                    'info': None,
                },
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_update_load_wrong_data(self):
        self.cargo._handler(CREATE_LOAD_COMMAND)
        cmd = {
            'action': 'update_load',
            'time': 1.1,
            'data': {'load': {'id': 999, 'length': 2.2}},
        }
        self.cargo._handler(cmd)
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'update_load',
            'data': {
                'message': 'Load with id=999 not found',
            },
            'response': 404,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)

    def test_delete_load(self):
        self.cargo._handler(CREATE_LOAD_COMMAND)
        cmd = {
            'action': 'delete_load',
            'time': 1.1,
            'data': {'load': {'id': 1}},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'delete_load',
            'data': {
                'message': 'Load deleted',
            },
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)


if __name__ == "__main__":
    unittest.main()
