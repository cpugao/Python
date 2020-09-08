class BankAccount:
    def __init__(self, int_rate, account):
        self.int_rate = int_rate
        self.account = account

    def deposit(self, amount):
        self.account += amount
        return self

    def withdraw(self, amount):
        if self.account<amount:
            print("No Money")
            return False
        self.account -= amount
        return self

    def display_account_info(self):
        return self.account

    def yield_interest(self):
        self.account += self.account*self.int_rate
        return self

class User:
    def __init__(self, name, account, int_rate, deposit, withdrawal):
        self.name = name
        self.account = account
        self.int_rate = int_rate
        self.make_deposit = deposit
        self.make_withdrawal = withdrawal

    def deposit(self, deposit):
        self.account += deposit
        return self

    def withdrawal(self, withdrawal):
        if self.account<withdrawal:
            print("Not Enough")
            return False
        self.account -= withdrawal
        return self

    def show_account(self, account):
        self.account
        return self
    
    def yield_interest(self):
        self.account += self.account*self.int_rate
        return self

carlo = User("Carlo", 0, 0.01, 0, 0)
mike = User("Mike", 0, 0.02, 0, 0)

carlo.deposit(20).deposit(20).deposit(20).withdrawal(10).yield_interest().show_account
mike.deposit(100).deposit(100).withdrawal(20).withdrawal(10).withdrawal(20).yield_interest().show_account

print(carlo.account)
print(mike.account)




