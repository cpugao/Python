class User:
    def __init__(self, name, deposit, withdrawal, balance, email, age):
        self.name = name
        self.deposit = deposit
        self.withdrawal = withdrawal
        self.balance = balance
        self.email = email
        self.age = age

    def __str__(self):
        return f"Name: {self.name}; Balance: {self.balance}"

    def make_deposit(self, deposit):
        self.balance += deposit
        return self

    def make_withdrawal(self, withdrawal):
        self.balance -= withdrawal
        return self

    def show_balance(self, balance):
        self.balance
        return self

Mike = User("Mike", 0, 0, 20, "m@u.com", 30)
Sara = User("Sara", 0, 0, 40, "s@u.com", 27)
Jon = User("Jon", 0, 0, 60, "j@u.com", 32)

Mike.make_deposit(20).make_deposit(5).make_deposit(10).make_withdrawal(10).show_balance

print(Mike.balance)

Sara.make_deposit(40).make_deposit(40).make_withdrawal(80).make_withdrawal(40).show_balance

print(Sara.balance)

Jon.make_deposit(40).make_withdrawal(10).make_withdrawal(10).make_withdrawal(10).show_balance

print(Jon.balance)
