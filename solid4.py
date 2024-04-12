from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class RefundProcessor(ABC):
    @abstractmethod
    def process_refund(self, amount):
        pass

class NormalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

class ComplexPaymentProcessor(PaymentProcessor,RefundProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

    def process_refund(self, amount):
        print(f"Processing refund of ${amount}")

normal_tx = NormalPaymentProcessor()
normal_tx.process_payment(1000)

complex_txn = ComplexPaymentProcessor()
complex_txn.process_payment(1000)
complex_txn.process_refund(100)
