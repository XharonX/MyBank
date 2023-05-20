import os.path
import sqlite3
from account import Account as acc


class connectDB:
    UNIQUE_TABLE = 'BankAccount'

    def __init__(self, dbName):
        self.dbName = dbName
        _path = os.getcwd() + '/db/%s'%self.dbName # '/home/kakashi/PycharmProjects/pythonProject/BankProject' % self.dbName
        self.conn = sqlite3.connect(_path)
        self.c = self.conn.cursor()

    def createTable(self,tbName=UNIQUE_TABLE):

        cmd = "CREATE TABLE IF NOT EXISTS {} (ID INTEGER PRIMARY KEY AUTOINCREMENT, accountID INTEGER, accountName CHAR, Balance INTEGER, Password CHAR);".format(tbName)
        self.c.execute(cmd)
        self.conn.commit()

    def CreateAccount(self, Account):
        self.c = self.conn.cursor()
        data = (Account.accountID, Account.accountName, Account.Balance, Account.Password)
        cmd = '''INSERT INTO {} (AccountID, AccountName, Balance, Password) VALUES(?, ?, ?, ?)'''.format(self.UNIQUE_TABLE)
        self.c.execute(cmd, data)
        self.conn.commit()
        self.conn.close()

    def UpdateBalance(self, Account):
        data = (Account.accountID, Account.accountName, Account.Balance)
        cmd = "UPDATE BankAccount SET Balance={} WHERE AccountID={} AND AccountName='{}';".format(data[2], data[0], data[1])
        self.c.execute(cmd)
        self.conn.commit()
        self.conn.close()

    def ckeck_ID_Name(self, accountID, EnterName):
        cmd = "SELECT * FROM BankAccount WHERE AccountID={} AND AccountName={}".format(accountID, EnterName)
        self.c.execute(cmd)
        if self.c.fetchone() is not None:
            return True
        else:
            print("You have no match with account ID and account Name. Please Try Later.")
            return False

    def is_auth(self, id, enterName, Password):
        cmd = "SELECT Password FROM BankAccount WHERE AccountID={} AND AccountName='{}'".format(id, enterName)
        self.c.execute(cmd)
        if self.c.fetchone()[0] == Password:
            return True
        return False

    def ChangePassword(self):
        pass

    def getIDs(self):
        cmd = "SELECT AccountID FROM BankAccount;"
        self.c.execute(cmd)
        if self.c.fetchall() is not None:
            return self.c.fetchall() # It return a tuple

    def getBalance(self, valid_ID):
        cmd = "SELECT Balance FROM BankAccount WHERE AccountID={}".format(valid_ID)
        self.c.execute(cmd)
        return self.c.fetchone()[0]

    def deleteAccount(self, inputID, accountName):
        cmd = "SELECT * FROM BankAccount WHERE AccountID={} AND AccountName='{}'".format(inputID, accountName)
        self.c.execute(cmd)
        if self.c.fetchone() is not None:
            cmd = "DELETE FROM BankAccount WHERE AccountID={}".format(inputID)
            self.c.execute()
        self.conn.commit()
        self.conn.close()

    def check_ID_Name(self, accountID, accountName):
        cmd = "SELECT AccountID, AccountName FROM BankAccount WHERE AccountID={} AND AccountName='{}'".format(accountID, accountName)
        self.c.execute(cmd)
        if self.c.fetchone() is not None:
            return True
        return False

    def is_auth(self, accountID, accountName, password):
        cmd = "SELECT Password FROM BankAccount WHERE AccountID={} AND AccountName='{}'".format(accountID, accountName)
        self.c.execute(cmd)
        if self.c.fetchone()[0] == password:
            return True
        return False
