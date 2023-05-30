from random import randint
from Authentication import get_password, auth
from DataConnection import *
from account import SavingAccount, FixedAccount
from my_db import MyDataBase
from conf import get_rtc


class Bank:
    # business transaction
    #   merchant system, payroll system
    # business loan -> 145
    #
    def __init__(self):
        pass

    @staticmethod
    def create_account(account_id, account_name, account_type, initial_deposit, password):
        bank_db = None
        dbname = 'Account.db'
        new_user = None
        password = get_password(password)
        cols = ['id INTEGER PRIMARY KEY AUTOINCREMENT',
                'joined_date DATETIME NULL',
                'account_id INTEGER NOT NULL',
                'account_name CHAR NOT NULL',
                'account_type CHAR NOT NULL',
                'annual_interest FLOAT',
                'balance FLOAT',
                'password CHAR'
                ]
        if account_type == 'saving':
            cols += ['withdrawal_times INTEGER NULL']
            bank_db = MyDataBase(dbname, 'SavingAccount')
            new_user = SavingAccount(account_id, account_name, initial_deposit, password)
            if initial_deposit < 10000:
                print("Your initial deposit must be above 10,000 Ks.")
                return 0
        elif account_type == 'fixed':
            bank_db = MyDataBase(dbname, 'FixedAccount')
            new_user = FixedAccount(account_id, account_name, initial_deposit, password)
            if initial_deposit < 100000:
                print("Your initial deposit must be 100,000 Ks. ")
                return 0
        bank_db.create_table(cols)
        if account_type == 'saving':
            new_user.joined_date = get_rtc()
            records = {}
            for keys, values in new_user.__dict__.items():
                records[str(keys)] = values
            bank_db.insert_record(records)
            print("Your account has been successfully created.")
            print(f"Please be remain your ID is: -> {account_id}")

    def open_account(self):
        print()
        print("* * *  0 P E N   A C C 0 U N T  * * *")
        print()
        name = input("Enter your name: ")
        initial_deposit = int(input("Enter First Deposit: "))
        press = input("Press [1] - Saving Deposit Account\nPress [2] - Fixed Deposit Account \nDefault [1] ")
        if press == '\n' or press == '1':
            account_type = 'saving'

        else:
            account_type = 'fixed'
        password = input("Enter your account password (for secure): ")
        code_id = self.generate_id
        self.create_account(code_id, name, account_type, initial_deposit, password)

    @staticmethod
    def generate_id():
        rand_id = int(randint(1000, 999999))
        dbms = MyDataBase('Account.db', 'SavingAccount')
        rec = dbms.fetch_all_records()
        account_id_list = [i[2] for i in rec]
        if rand_id in account_id_list:
            rand_id = int(randint(1000, 999999))
        return rand_id

    @staticmethod
    def deposit_account():
        dbms = MyDataBase('Account.db', 'SavingAccount')
        print(" * * * A C C 0 U N T  D E P 0 S ! T * * * ")
        print()
        input_id = int(input("Enter account ID: "))
        input_name = input("Enter account Name: ")

        if auth(input_id, input_name):
            dbms.fetch_acc_type(input_id)
            deposit_amount = int(input("Enter your deposit amount: "))
            record = dbms.fetch_records_by_id(input_id, ['joined_date', 'balance', ])
            my_balance = record[1]
            user = SavingAccount(input_id, input_name, my_balance)
            user.joined_date = record[0]
            tt_balance = user.deposits(deposit_amount)
            dbms.update_record(['balance'], [tt_balance], 'account_id', input_id)
        else:
            print("Please enter your account id, name and password.")

    @staticmethod
    def withdraw_account():
        dbms = MyDataBase('Account.db', 'SavingAccount')
        # withdrawal_dbms = MyDataBase('Account.db', 'WithdrawalsLogs')
        print(" * * * A C C 0 U N T   W ! T H D R A W * * * ")
        print()
        input_id = int(input("Enter account ID: "))
        input_name = input("Enter account Name: ")
        if auth(input_id, input_name):
            withdrawals = int(input("Enter withdraw amount: "))
            record = dbms.fetch_records_by_id(input_id, ['balance', 'withdrawal_times'])
            my_balance = record[0]
            if record[1] is not None:
                count = record[1]
                count += 1
            else:
                count = 1
            user = SavingAccount(input_id, input_name, my_balance)
            tt_balance = user.withdrawals(withdrawals)
            print(user.balance)
            dbms.update_record(['balance', 'withdrawal_times'], [tt_balance, count], 'account_id', input_id)
            # columns = [get_rtc(), userAcc.account_id, myBalance]  # foreign_key should be reanalysis
            # filters = {'column': 'account_id', 'value': userAcc.account_id}
            # Withdrawal_DB.update_record(columns, filters)
        else:
            print("Please enter your account id, name and password.")

    @staticmethod
    def close_account():
        BankDB = connectDB('Account.db')
        print(" * * * C L () S E  A C C 0 U N T  * * * ")
        print()
        inputID = int(input("Enter account ID: "))
        inputName = input("Enter account Name: ")
        if auth(inputID, inputName):
            yes = False
            is_sure = input('Are you sure to close your account [N] or [y] (Default is NO): ')
            if is_sure.lower()[0] == 'y':
                yes = True
            elif is_sure.lower()[0] == '':
                yes = False
                return None
            else:
                raise ValueError("Enter N or Y")
            if not yes:
                return None
            else:
                BankDB.deleteAccount(inputID, inputName)
            return None

    def transaction_account(self):
        pass


def menu():
    print("", end=' ')
    print('_ ' * 24)
    print("| Press an option to choose your opportunity.")
    print("| [1] Open an account")
    print("| [2] Withdraw")
    print("| [3] Deposit")
    print("| [4] Close Account ")
    print("| [q] Quit")
    print(" ", end="")
    print('_ ' * 24)


def selection(opt):
    AYA = Bank()
    opt = opt.lower()[0]
    if opt == '1':
        AYA.open_account()
    elif opt == '2':
        AYA.withdraw_account()
    elif opt == '3':
        AYA.deposit_account()
    elif opt == '4':
        AYA.close_account()
    elif opt == '5':
        AYA.__str__()
    elif opt == '6':
        AYA.transaction_account()
    elif opt == 'q':
        quit()


class Manager:
    pass
class Transcation(Bank):
    pass
class Payroll(Transcation):
    pass
class Merchant(Transcation):
    pass
class Loan:
    # type of loans, annual interest, valid term
    pass


class ShortTeam(Loan):

    __doc__ = '''
    10 % , 1 yr
    '''
    pass


class LongTeam(Loan):
    '''
    10 % , 1yr
    '''
