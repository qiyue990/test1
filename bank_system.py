# 银行系统的Python实现，包括创建账户、存款、提款、转账以及保存和加载账户状态到CSV文件的功能；
# 代码实现：新建文件bank_system.py
import csv


class BankAccount:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount > 0:
            self.balance -= amount
            return True
        return False

    def transfer(self, other_account, amount):
        if self.withdraw(amount):
            other_account.deposit(amount)
            return True
        return False


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_balance=0):
        if name not in self.accounts:
            self.accounts[name] = BankAccount(name, initial_balance)

    def get_account(self, name):
        return self.accounts.get(name)

    def save_to_csv(self, filename='bank_data.csv'):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for name, account in self.accounts.items():
                writer.writerow([name, account.balance])

    def load_from_csv(self, filename='bank_data.csv'):
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for name, balance in reader:
                self.create_account(name, int(balance))


# 示例用法
if __name__ == "__main__":
    bank_system = BankSystem()
    bank_system.create_account('Alice', 1000)
    bank_system.create_account('Bob', 500)
    bank_system.get_account('Alice').deposit(200)
    if bank_system.get_account('Alice').withdraw(150):
        print(f"Alice's balance: {bank_system.get_account('Alice').balance}")
    if bank_system.get_account('Alice').transfer(bank_system.get_account('Bob'), 100):
        print(f"Bob's balance: {bank_system.get_account('Bob').balance}")
    bank_system.save_to_csv()
    bank_system.load_from_csv()
    