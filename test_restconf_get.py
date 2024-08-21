import unittest
from restconf_get_qn import *

class test_restconf(unittest.TestCase):
    def test_is_a_dict(self):
        '''should return a dict'''
        self .assertIsInstance(response_json,dict)

if __name__ == '__main__':
    unittest.main()
