import unittest
from client import *

class NamesTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_로그인(self):
        self.assertTrue(self.client.isLogin)

    def test_구매(self):
        start_money = self.client.get_account()
        self.client.buy()
        end_money = self.client.get_account()
        self.assertTrue(end_money < start_money)

