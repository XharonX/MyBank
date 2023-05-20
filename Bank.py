from random import randint
import sqlite3
from Authentication import get_password, auth
from DataConnection import *
from account import Account


class Bank:
    def __init__(self):
        pass

    def createAccount(self, get_ID, accountName, firstDeposit, Password):
        hash_password = get_password(Password)
        print(hash_password)
        oAccount = Account(get_ID, accountName, firstDeposit, Password)
        Bank_DB = connectDB('Account.db')
        Bank_DB.createTable('BankAccount')
        Bank_DB.CreateAccount(oAccount)

    def openAccount(self):
        print()
        print("* * *  O P E N   A C C O U N T  * * *")
        print()
        name = input("Enter your name: ")
        firstDeposit = int(input("Enter First Deposit: "))
        password = input("Enter your account password (for secure): ")
        accountID = self._getID()
        self.createAccount(accountID, name, firstDeposit, password)
        print("Please be remain your ID is: -> %d" %accountID)

    def _getID(self):
        id = int(randint(10000, 99999))
        BankDB = connectDB('Account.db')
        accountID_Tuple = (10000, 99999) # BankDB.getIDs()
        if id in accountID_Tuple:
            id = int(randint(10000, 99999))
        return id

    def depositAccount(self):
        BankDB = connectDB('Account.db')
        print(" * * * A C C 0 U N T  D E P 0 S ! T * * * ")
        print()
        inputID = int(input("Enter account ID: "))
        inputName = input("Enter account Name: ")

        if auth(inputID, inputName):
            depositAmount = int(input("Enter your deposit amount: "))
            myBalance = BankDB.getBalance(inputID)
            print("my balance: %d" %myBalance)
            userAcc = Account(inputID, inputName, myBalance)
            tt_balance = userAcc.Deposit(depositAmount)
            print(tt_balance)
            print(userAcc.Balance)
            BankDB.UpdateBalance(userAcc)

        else:
            count = 1
            print("Wrong Password or Account Name or Wrong Account ID number. Please Try Again")
            self.depositAccount()
            count += 1

    def withdrawAccount(self):
        BankDB = connectDB('Account.db')
        print(" * * * A C C 0 U N T  D E P 0 S ! T * * * ")
        print()
        inputID = int(input("Enter account ID: "))
        inputName = input("Enter account Name: ")
        if auth(inputID, inputName):
            withdrawAmount = int(input("Enter withdraw amount: "))
            myBalance = BankDB.getBalance(inputID)
            print("my balance: %d" % myBalance)
            userAcc = Account(inputID, inputName, myBalance)
            tt_balance = userAcc.Withdraw(withdrawAmount)
            print(tt_balance, userAcc.Balance)
            BankDB.UpdateBalance(userAcc)
        else:
            pass

    def closeAccount(self):
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

    def transactionAccount(self):
        pass


def Menu():
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


def Selection(opt):
    AYA = Bank()
    opt = opt.lower()[0]
    if opt == '1':
        AYA.openAccount()
    elif opt == '2':
        AYA.withdrawAccount()
    elif opt == '3':
        AYA.depositAccount()
    elif opt == '4':
        AYA.closeAccount()
    elif opt == '5':
        AYA.transactionAccount()
    elif opt == 'q':
        quit()
