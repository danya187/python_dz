import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from common.const import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from client import create_presence, process_ans


class TestClass(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_def_presence(self):
        test = create_presence()
        test[TIME] = 1.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER:{ACCOUNT_NAME: 'Guest'}})

    def test_200_ans(self):
        self.assertEqual(process_ans({RESPONSE: 200}), '200 : ok')

    def test_400_ans(self):
        self.assertEqual(process_ans({RESPONSE: 400, ERROR: 'request error'}), '400 : request error')

    def test_no_response(self):
        self.assertRaises(ValueError, process_ans, {ERROR: 'request error' })


if __name__ == '__name__':
    unittest.main()
