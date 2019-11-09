import os
import sys
import unittest

from cargo.utils.config import DATABASE
from cargo.utils.db import Base
from cargo.utils.handlers import handler

sys.path.append(os.path.join(os.getcwd(), "../cargo"))

from cargo.app import Cargo


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


if __name__ == "__main__":
    unittest.main()
