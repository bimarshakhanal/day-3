from abc import ABC, abstractmethod

class Product(ABC):
  """
  Abstract Product class representing all kinds of product.
  """
  def __init__(self, price):
    self.price = price

  @abstractmethod
  def get_final_price(self):
    """
    Abstract class for price calculations, to be implemented by base class.
    """
    pass

class GeneralProduct(Product):
    def __init__(self, price):
       super().__init__(price)
    
    def get_final_price(self):
       return self.price

class DiscountedProduct(Product):
   def __init__(self, price,discount):
      super().__init__(price)
      self.discount = discount
    
   def get_final_price(self):
      return self.price - self.price*(self.discount/100)

def calculate_total_price(products):
    total_price = 0
    for product in products:
        total_price += product.get_final_price()
    return total_price

products = [GeneralProduct(100), GeneralProduct(50), DiscountedProduct(125,25), DiscountedProduct(1000,50)]
print("Total Price:", calculate_total_price(products))