from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price, stock):
            self.product_id = product_id
            self.name = name
            self.price = price
            self.stock = stock
        
    def update_stock(self, itemStock):
        self.stock = itemStock

    def display_information(self):
        print(f"Product ID: {self.product_id} | Name: {self.name} | Price: {self.price} | Stock: {self.stock} units", end="")

    @abstractmethod
    def get_fulfillment_info(self):
        pass