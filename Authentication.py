import hashlib
from my_db import MyDataBase


def get_password(passwd: str):
    b_str = passwd.encode()
    passwd = hashlib.md5(b_str).hexdigest()
    return passwd


def auth(accountID, accountName):
    tables = ['SavingAccount', 'FixedAccount']
    for tb_name in tables:
        dbms = MyDataBase('Account.db', tb_name)
        if dbms.check_id_name(accountID, accountName):
            password = input("Enter password: ")
            fetch = dbms.fetch_records_by_id(accountID)
            if accountName == fetch[3] and get_password(password) == fetch[7]:
                return True
            return False
        else:
            print(f"We can't find your account at {accountID} with {accountName}.")
