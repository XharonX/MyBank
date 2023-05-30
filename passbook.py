from account import Account
from conf import get_rtc
from my_db import MyDataBase

class PassBook(Account):
    CODE = [
        ('AAT', 'Account To Account Transfer'),
        ('CHD', 'Cash Deposit'),
        ('CHW', 'Cash Withdrawal'),
        ('CQW', 'Clearing Credit Deliver'),
        ('ICC', 'Interest Post Credit Customer'),
    ]

    def __init__(self, acc_id, name, code, deposit=0.0, withdrawal=0.0, balance=0.0):
        super().__init__(acc_id, name)
        self.date = get_rtc()
        self.code = code
        self.deposit = deposit
        self.withdrawal = withdrawal
        self.balance = balance

    def list_passbook(self, acc_id, name):
        cols = [
            'id Integer Primary Key AutoIncrement',
            'account_name CHAR NOT NULL',
            'account_id INTEGER 0',
            'Date DATETIME NULL',
            'Deposit FLOAT DEFAULT 0',
            'Withdrawal FLOAT DEFAULT 0',
            'Balance FLOAT DEFAULT 0',
        ]
        passbook_dbms = MyDataBase('Account.db', 'Passbook')
        passbook_dbms.create_table(cols)

    def create_passbook(self, name):
        cols = [
            'id Integer Primary Key AutoIncrement',
            'account_name CHAR NOT NULL',
            'Date DATETIME NULL',
            'Deposit FLOAT DEFAULT 0',
            'Withdrawal FLOAT DEFAULT 0',
            'Balance FLOAT DEFAULT 0',
        ]
    def update_passbook(self):
        pass
