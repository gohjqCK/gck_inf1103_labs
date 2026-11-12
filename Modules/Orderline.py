class Orderline:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity