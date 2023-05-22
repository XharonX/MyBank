from datetime import datetime
from conf import get_rtc


class Account:
    def __init__(self, accountID: int, accountName: str, balance=0, secretPhrase=""):
        self.joinDate = get_rtc()
        self.accountID = accountID
        self.accountName = accountName
        self.Balance = balance
        self.Password = secretPhrase
        self.account_type = None
        self.annual_interest = 0.00  # percent


    def Deposits(self, depositAmount):
        if self.Balance < 0:
            raise ValueError("Deposit Amount must be greater than 0.")
        elif self.Balance == 0:
            if self.account_type == 'saving':
                if depositAmount < 10000:
                    raise ValueError("You must deposit 10000Ks at first.")
                else:
                    self.Balance += depositAmount
        else:
            if self.account_type is None:
                pass
            elif self.account_type == 'saving':
                self.Balance += depositAmount
                self.get_interest(self.Balance, self.annual_interest)

        return self.Balance

    def Withdrawals(self, withdrawals_amount):

        if self.Balance < 0:
            raise ValueError("Withdraw Amount must be greater than 0.")
        elif self.Balance == 0:
            raise ValueError("This class was not connected with DB.")
        elif self.Balance < withdrawals_amount:
            raise ValueError("You withdrawals amount is greate than your main balance. \n Your main balance is %d" %withdrawals_amount)
        elif self.Balance == withdrawals_amount:
            raise ValueError("\n You must leave 1000Ks for your deposit insurance.")
        else:
            if self.account_type is None:
                pass
            # After adding joined date and datetime management
            elif self.account_type == 'saving':
                balance = self.Balance
                balance -= withdrawals_amount
                if balance <= 1000:
                    print("Please deposit an amount of insurance for your deposit. ")
                    return self.Balance
                else:
                    self.Balance = self.get_interest(balance, self.annual_interest)
                    return self.Balance


    def Profile(self):
        print("* " * 20)
        print("* Account ID: %d\t*" % self.accountID)
        print("* Account Name: %s\t*" % self.accountName)
        print("* Account Balance: %s\t*" % self.Balance)
        print("* Account Password: %s\t*" % self.Password)
        print("* " * 20)

    def get_balance(self):
        pass

    def get_interest(self, main_balance, _interest):

        if self.account_type == 'saving':
            if not _interest <= 1.0:
                if  int(get_rtc()[5:7]) % 3 == 0:
                    _interest = _interest * main_balance
                    main_balance += _interest
                else:
                    _interest = 1.0
                    _interest *= main_balance
            else:
                print("You have something wrong.")
            return main_balance

    def get_Password(self):
        pass

    def __str__(self):
        return '[ ' + str(self.accountID) + ' ]' + self.accountName


class SavingAccount(Account):
    ANNUAL_INTEREST = 7.00
    def __init__(self, accountID, accountName):
        super().__init__(accountID, accountName)
        self.account_type = 'saving'
        self.initial_deposit = 10000.0
        self.month = ('June', 'Sep', 'Dec', 'Mar')  # month % 3 == 0
        self.deposit_insurance = 1000
        self.Balance = 0
        self.annual_interest = 7.00

    def first_deopsit(self, DP):
        pass
    # Limit number of withdrawals
    # Limit Transfer options
    # inability to be overdrawn
    # Transaction
    # funds = အပ်ငွေ(ရန်ပုံငွေ)
    # annual interest - 7.00 % p.a
    # June, Sep, Dec, March
    # deposit insurance - ငွေအပ်အာမခံ
    # sub class -
    #   youngsaver - for edu
    #   investment account
    #   retirees - အငြိမ်းစား
    #   money market account
    #   initial deposits - must larger than 1000 ks
    #   deposit must regular
    #   notices of withdrawals
    #


class EmployeeAccount(Account):
    pass


class FixedAccount(Account):
    # initial deposit - 100,000Ks
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
