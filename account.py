class Account:
    def __init__(self, accountID, accountName, balance=0, secretPhrase=""):
        self.accountID = accountID
        self.accountName = accountName
        self.Balance = balance
        self.Password = secretPhrase

    def Deposit(self, depositAmount):
        if self.Balance < 0:
            raise ValueError("Deposit Amount must be greater than 0.")
        elif self.Balance == 0:
            print("This class was not connected with DB.")
        else:
            self.Balance += depositAmount
        return self.Balance

    def Withdraw(self, withdrawAmount):
        if self.Balance < 0:
            raise ValueError("Withdraw Amount must be greater than 0.")
        elif self.Balance == 0:
            raise ValueError("This class was not connected with DB.")
        else:
            self.Balance -= withdrawAmount
        return self.Balance

    def Profile(self):
        print("* "* 20)
        print("* Account ID: %d\t*" %self.accountID)
        print("* Account Name: %s\t*" %self.accountName)
        print("* Account Balance: %s\t*" %self.Balance)
        print("* Account Password: %s\t*" %self.Password)
        print("* "* 20)

    def get_balance(self):
        pass

    def get_Password(self):
        pass

    def __str__(self):
        return '[ '+ str(self.accountID) + ' ]' + self.accountName
