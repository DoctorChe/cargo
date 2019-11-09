import os
import sys
import unittest

from cargo.utils.handlers import handler
from cargo.utils.protocol import common_check_command

sys.path.append(os.path.join(os.getcwd(), "../cargo"))

from cargo.app import Cargo


class TestCargoInstance(unittest.TestCase):

    # test the creation of an instance of the Cargo class without passing the required parameter handle
    def test_instant_creation_no_handle(self):
        with self.assertRaises(TypeError):
            Cargo()


class TestProtocolCreateCommand(unittest.TestCase):

    def test_long_command(self):
        cmd = {
            'action': 'create_person',
            'time': 1000.10,
            'data': 'A' * 640,
        }
        self.assertEqual(common_check_command(cmd), False)


class TestProtocolCreateResponse(unittest.TestCase):

    def setUp(self):
        self.cargo = Cargo(handler=handler)

    def test_action_response(self):
        cmd = {
            'time': 1000.10,
            'data': {},
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': None,
            'data': {'message': 'Command is incorrect'},
            'response': 400,
            'time': 1000.1
        }
        self.assertEqual(response, expected_response)

    def test_time_response(self):
        cmd = {
            'action': 'create_person',
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'create_person',
            'data': {'message': 'Command is incorrect'},
            'response': 400,
            'time': None
        }
        self.assertEqual(response, expected_response)


class TestHandler(unittest.TestCase):

    def setUp(self):
        self.cargo = Cargo(handler=handler)

    def test_incorrect_command(self):
        cmd = {
            'action': 'create_person',
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'create_person',
            'data': {'message': 'Command is incorrect'},
            'response': 400,
            'time': None
        }
        self.assertEqual(response, expected_response)

    def test_unsupported_action(self):
        cmd = {
            'action': 'unsupported_action',
            'time': 1.1,
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'unsupported_action',
            'data': {'message': 'Action with name unsupported_action not supported'},
            'response': 404,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)


if __name__ == '__main__':
    unittest.main()
