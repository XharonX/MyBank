from conf import get_rtc
from conf import deta_time_by_months as dt


class Account:
    account_type = None

    def __init__(self, account_id: int, account_name: str, account_type='', balance=0.0, secret_phrase=""):
        self.joined_date = None
        self.account_id = account_id
        self.account_name = account_name
        self.account_type = account_type
        self.annual_interest = 0.00  # percent
        self.balance = balance
        self.password = secret_phrase

    def deposits(self, deposit_amount):

        if self.balance == 0.0:
            if self.account_type == 'saving':
                if deposit_amount < 10000:
                    print("You must deposit 10000Ks at first.")
                else:
                    self.balance += deposit_amount
        elif self.balance > 0.0:
            if self.account_type is not None:
                self.balance = self.add_interest(self.joined_date, self.balance, self.annual_interest)
                self.balance += deposit_amount
        else:
            raise ValueError("Deposit Amount must be greater than 0.")
        return self.balance

    def withdrawals(self, withdrawals_amount):
        if 0 < withdrawals_amount < self.balance:
            if self.account_type is None:
                pass
        elif self.balance == 0:
            print("This class was not connected with DB.")
        elif self.balance < withdrawals_amount:
            print("You withdrawals amount is greate than your main balance. \n Your main balance is %d" % self.balance)
        elif self.balance == withdrawals_amount:
            print("\n You must leave 1000 Ks for your deposit insurance.")
        else:
            pass

    def profile(self):
        print("* " * 20)
        print("* Account ID: %d\t*" % self.account_id)
        print("* Account Name: %s\t*" % self.account_name)
        print("* Account balance: %s\t*" % self.balance)
        print("* Account password: %s\t*" % self.password)
        print("* " * 20)

    def add_interest(self, joined_date, main_balance, _interest):
        if self.account_type == 'saving':
            m = dt(joined_date)
            if 3 < dt():
                if int(get_rtc()[5:7]) % 3 == 0:
                    monthly_percent = _interest / 1200  # it will be percentage
                    _interest = monthly_percent * m
                else:
                    _interest = 1.0
                main_balance += (_interest * main_balance)
                return main_balance
            else:
                if int(get_rtc()[5:7]) % 3 == 0:
                    monthly_percent = _interest / 1200  # it will be percentage
                    _interest = monthly_percent * m
                else:
                    _interest = 0.0
                main_balance += (_interest * main_balance)
                return main_balance

    def __str__(self):
        return '[ ' + str(self.account_id) + ' ]' + self.account_name


class SavingAccount(Account):
    ANNUAL_INTEREST = 0.007
    INITIAL_DEPOSIT = 10000.0
    ACCOUNT_TYPE = 'saving'

    def __init__(self, account_id, account_name, balance, password=None):
        super().__init__(account_id, account_name, self.ACCOUNT_TYPE, balance, password)
        self.joined_date = None
        self.balance = balance
        self.annual_interest = 7.00

    def withdrawals(self, withdrawals_amount):
        if 0 < withdrawals_amount < self.balance:
            balance = self.add_interest(self.joined_date, self.balance, self.annual_interest)
            print(balance)
            balance -= withdrawals_amount
            if balance < 9000:
                print("You have no permit to overdrawn.")
                print("Please deposit an amount of insurance for your deposit. ")
                return self.balance
            else:
                self.balance = balance
                return self.balance

    # Transaction
    # sub class -
    #   youngsaver - for edu
    #   investment account
    #   retirees - အငြိမ်းစား


class EmployeeAccount(Account):
    pass


class FixedAccount(Account):
    ACCOUNT_TYPE = 'fixed'

    def __init__(self, account_id, account_name, balance, annual_interest, password=None):
        super().__init__(account_id, account_name, self.ACCOUNT_TYPE, balance, password)
        self.annual_interest = annual_interest

    def withdrawals(self, withdrawals_amount):
        if 0 < withdrawals_amount < self.balance:
            balance = self.add_interest(self.joined_date, self.balance, self.annual_interest)
            print(balance)
            balance -= withdrawals_amount
            if balance < 9000:
                print("You have no permit to overdrawn.")
                print("Please deposit an amount of insurance for your deposit. ")
                return self.balance
            else:
                self.balance = balance
                return self.balance
    # no limit
    # 30 days - 7.00 %
    # 60 days - 7.10 %
    # 90 - 7.35 %
    # 180 - 7.6 %
    # 270 - 7.8 %
    # 365 - 8 % (below 100 millions)
    # 365 - 8.25% ( 100 million << 500 million)
    # 365 - 8.5 % (above 500 millions)
    # can be joined with two or more account holders
    # အပ်နှံထားသော ကာလပြည့်ရင် အတိုးကောအရင်းကောရမယ်
    # can loan
    # holder can be 1 or 2
    # if a person die the second person can be closed the account.

    pass
