import hashlib
from DataConnection import connectDB

def get_password(passwd:str):
    b_str = passwd.encode()
    passwd = hashlib.md5(b_str).hexdigest()
    return passwd
def auth(accountID, accountName):
    BKDB = connectDB('Account.db')
    if BKDB.check_ID_Name(accountID, accountName):
        password = input("Enter password: ")
        hash_digest = get_password(password)
        if BKDB.is_auth(accountID, accountName, hash_digest):
            return True
        return False