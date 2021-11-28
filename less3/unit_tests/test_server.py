import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from common.const import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from server import process_client_msg


class TestServer(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    error_dict = {
        RESPONSE: 400,
        ERROR: 'request error',
    }
    ok_dict = {RESPONSE:200}

    def test_ok_check(self):
        self.assertEqual(process_client_msg(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.ok_dict)

    def test_no_action(self):
        self.assertEqual(process_client_msg(
            {TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.error_dict)

    def test_wrong_action(self):
        self.assertEqual(process_client_msg(
            {ACTION: 'Wrong', TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.error_dict)

    def test_no_time(self):
        self.assertEqual(process_client_msg(
            {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}), self.error_dict)

    def test_no_user(self):
        self.assertEqual(process_client_msg(
            {ACTION: PRESENCE, TIME: '1.1'}), self.error_dict)

    def test_unknown_user(self):
        self.assertEqual(process_client_msg(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest1'}}), self.error_dict)


if __name__ == '__main__':
    unittest.main()
