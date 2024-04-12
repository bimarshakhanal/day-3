'''
Build a Python class to represent a simple banking system. Create a class for a BankAccount, and another for Customer.
The BankAccount class should have a constructor to initialize the account details (account number, balance, account type).
The Customer class should have a constructor to set the customer's details (name, age, address) and create a BankAccount
object for each customer. Implement a destructor for both classes to display a message when objects are destroyed.
'''

import logging

logging.basicConfig(filename='log.txt', level=logging.DEBUG)

class BankAccount:
    def __init__(self, ac_no,balance, ac_type):
        self.ac_no = ac_no
        self.balance = balance
        self.ac_type = ac_type
    
    def __del__(self):
        print('Parent destructors called.')
        logging.info(f'Bank Account: {self.ac_no}, deleted sucessfully.')

class Customer(BankAccount):
    def __init__(self, name, age, address, ac_no, balance, ac_type):
        super().__init__(ac_no, balance, ac_type)
        self.name = name
        self.age = age
        self.address = address

    def __del__(self):
        logging.info(f'Customer: {self.ac_no}, removed sucessfully.')


customer1 = Customer('Ram Singh', 22, 'Pokahra', 'PA1234B', 999999.22, 'SAVING')

del customer1
