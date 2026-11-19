from Modules import Product

class Orderline:
    def __init__(self, product: Product, quantity):
        self.product = product
        self.quantity = quantity
        if quantity <= 0:
            raise ValueError("Quantity cannot be negative.")

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity