
from abc import ABC, abstractmethod


class Account(ABC):
    """
    Abstract base class representing a generic bank account.
    """

    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def withdraw(self, amount):
        """
        Abstract method for withdrawing funds, to be implemented by subclasses.
        """
        pass


class SavingsAccount(Account):
    '''Concrete class representing saving account'''

    def __init__(self, balance) -> None:
        super().__init__(balance)

    def withdraw(self, amount):
        # Savings account does not allow overdrafts
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")

        else:
            print("Insufficient funds!")


class CheckingAccount(Account):
    '''Concrete class representing checking account'''

    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # Checking account allows overdrafts but with a limit
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Exceeds overdraft limit or insufficient funds!")


def perform_bank_actions(account):
    '''Function to perform bank actions'''
    account.withdraw(100)
    account.withdraw(200)
    account.withdraw(500)


if __name__ == "__main__":
    # Creating instances of SavingsAccount and CheckingAccount
    savings_account = SavingsAccount(500)
    checking_account = CheckingAccount(1000, overdraft_limit=200)

    # Performing actions on both accounts
    perform_bank_actions(savings_account)
    perform_bank_actions(checking_account)
