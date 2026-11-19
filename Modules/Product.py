from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price, stock, supplier):
            self.product_id = product_id
            self.name = name
            self.price = price
            self.stock = stock
            self.supplier = supplier
            if self.price <= 0:
                raise ValueError("Price must be greater than zero.")
            if self.stock <= 0:
                raise ValueError("Quantity cannot be negative.")
        
    def update_stock(self, itemStock: int) -> None:
        if itemStock <= 0:
             raise ValueError("Quantity cannot be negative.")
        self.stock = itemStock

    def display_information(self) -> None:
        print(f"Product ID: {self.product_id} | Name: {self.name} | Price: ${self.price:.2f} | Stock: {self.stock} units", end="")

    @abstractmethod
    def get_fulfillment_info(self):
        pass