from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    '''Abstract base class representing a payment processor.'''

    @abstractmethod
    def process_payment(self, amount):
        '''Abstract method to process a payment.'''


class RefundProcessor(ABC):
    '''Abstract base class representing a refund processor.'''

    @abstractmethod
    def process_refund(self, amount):
        '''Abstract method to process a refund.'''


class NormalPaymentProcessor(PaymentProcessor):
    '''Concrete class for processing normal payments.'''

    def process_payment(self, amount):
        '''Process a payment of the specified amount.'''
        print(f"Processing payment of ${amount}")


class ComplexPaymentProcessor(PaymentProcessor, RefundProcessor):
    '''Concrete class for processing complex payments and refunds.'''

    def process_payment(self, amount):
        '''Process a payment of the specified amount.'''
        print(f"Processing payment of ${amount}")

    def process_refund(self, amount):
        '''Process a refund of the specified amount.'''
        print(f"Processing refund of ${amount}")


normal_tx = NormalPaymentProcessor()
normal_tx.process_payment(1000)

complex_txn = ComplexPaymentProcessor()
complex_txn.process_payment(1000)
complex_txn.process_refund(100)
