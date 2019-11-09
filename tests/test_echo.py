import os
import sys
import unittest

from cargo.utils.handlers import handler

sys.path.append(os.path.join(os.getcwd(), "../cargo"))

from cargo.app import Cargo


class TestEcho(unittest.TestCase):

    def setUp(self):
        self.cargo = Cargo(handler=handler)

    def test_echo(self):
        cmd = {
            'action': 'echo',
            'time': 1.1,
        }
        response = self.cargo._handler(cmd)
        expected_response = {
            'action': 'echo',
            'data': None,
            'response': 200,
            'time': 1.1
        }
        self.assertEqual(response, expected_response)


if __name__ == "__main__":
    unittest.main()
