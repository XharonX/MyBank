import hashlib
from DataConnection import connectDB

def get_password(passwd:str):
    b_str = passwd.encode()
    passwd = hashlib.md5(b_str).digest()
    # return passwd.encode()
    return None
def auth(accountID, accountName):
    BKDB = connectDB('Account.db')
    if BKDB.check_ID_Name(accountID, accountName):
        password = input("Enter password: ")
        if BKDB.is_auth(accountID, accountName, password):
            return True
        return False