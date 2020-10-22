#!/usr/bin/env python

class BankAccount(object):
    next_account_no = 16555232
    acc_type = "General"

    def __init__(self, forename="", surname="", balance=0):
        self.forename = forename
        self.surname = surname
        self.balance = float(balance)
        self.acc_no = int(BankAccount.next_account_no)

        BankAccount.next_account_no += 1

    def lodge(self, other):
        self.balance += int(other)

    def withdraw(self, other):
        if self.balance < other:
            print ("Insufficient funds available")
        else:
            self.balance -= other

    def __str__(self):
        l = []
        l.append("Name: {} {}".format(self.forename, self.surname))
        l.append("Account number: {}".format(self.acc_no))
        l.append("Account type: {}".format(self.acc_type))
        l.append("Balance: {:.2f}".format(self.balance))
        return "\n".join(l)

class CurrentAccount(BankAccount):
    overdraft = -1000
    acc_type = "Current"

    def withdraw(self, other):
        if self.balance < int(other) + CurrentAccount.overdraft:
            print ("Insufficient funds available")
        else:
            self.balance -= int(other)

    def __str__(self):
        l = []
        l.append("Name: {} {}".format(self.forename, self.surname))
        l.append("Account number: {}".format(self.acc_no))
        l.append("Account type: {}".format(self.acc_type))
        l.append("Balance: {:.2f}".format(self.balance))
        l.append("Overdraft: {:.2f}".format(self.overdraft))
        return "\n".join(l)

class SavingsAccount(BankAccount):
    interest_rate = 0.01
    acc_type = "Savings"

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return self

    def __str__(self):
        l = []
        l.append("Name: {} {}".format(self.forename, self.surname))
        l.append("Account number: {}".format(self.acc_no))
        l.append("Account type: {}".format(self.acc_type))
        l.append("Balance: {:.2f}".format(self.balance))
        l.append("Interest rate: {}".format(self.interest_rate))
        return "\n".join(l)

def main():
    a1 = CurrentAccount('Joe', 'Murphy', 100)
    a2 = SavingsAccount('Mandy', 'Murray', 100)
    a3 = SavingsAccount('Jimmy', 'Smith', 200)
    a4 = BankAccount('Frank', 'Wrigley', 500)

    # Print base classes
    print('Base classes...')
    print(a1.__class__.__bases__)
    print(a2.__class__.__bases__)

    # Print account details
    print('Account details...')
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print('-' * 20)

    # Call some methods
    a1.lodge(50)
    a1.withdraw(100)
    a1.withdraw(100)
    a1.withdraw(1000)
    a2.withdraw(10)
    a2.withdraw(100)
    a2.lodge(20)
    a2.apply_interest()
    a4.lodge(20)
    a4.withdraw(20)
    a4.withdraw(1000)

    # Some methods should not exist
    try:
        a1.apply_interest()
    except AttributeError:
        print('No such method')
    try:
        a4.apply_interest()
    except AttributeError:
        print('No such method')
    print('-' * 20)

    # Print account details
    print('Account details...')
    print(a1)
    print(a2)
    print(a3)
    print(a4)

if __name__ == '__main__':
    main()
