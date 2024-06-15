# 测试用例：新建文件test_bank_system.py，在 test_bank_system.py 中，使用 unittest 模块编写测试用例：
import unittest
from bank_system import BankAccount, BankSystem


class TestBankSystem(unittest.TestCase):
    def setUp(self):
        self.bank_system = BankSystem()
        self.bank_system.create_account('Alice', 1000)
        self.bank_system.create_account('Bob', 500)

    def test_deposit(self):
        alice_account = self.bank_system.get_account('Alice')
        alice_account.deposit(200)
        self.assertEqual(alice_account.balance, 1200)

    def test_withdraw(self):
        alice_account = self.bank_system.get_account('Alice')
        self.assertTrue(alice_account.withdraw(100))
        self.assertEqual(alice_account.balance, 900)

    def test_transfer(self):
        alice_account = self.bank_system.get_account('Alice')
        bob_account = self.bank_system.get_account('Bob')
        self.assertTrue(alice_account.transfer(bob_account, 50))
        self.assertEqual(alice_account.balance, 950)
        self.assertEqual(bob_account.balance, 550)

    def test_save_and_load(self):
        self.bank_system.get_account('Alice').deposit(100)
        self.bank_system.save_to_csv('temp.csv')
        self.bank_system = BankSystem()
        self.bank_system.load_from_csv('temp.csv')
        self.assertEqual(self.bank_system.get_account('Alice').balance, 1100)


if __name__ == '__main__':
    unittest.main()