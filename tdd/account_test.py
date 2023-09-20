import unittest
from unittest import TestCase

from tdd.account import Account


class Test_Account(TestCase):
    def test_deposit_money(self):
        favour_Account = Account()
        self.assertEqual(0, favour_Account.get_balance())
        favour_Account.deposit(2000)
        self.assertEqual(2000, favour_Account.get_balance())

    def test_cannot_deposit_negative_amount(self):
        favour_Account = Account()
        self.assertEqual(0, favour_Account.get_balance())
        favour_Account.deposit(-2000)
        self.assertEqual(0, favour_Account.get_balance())
