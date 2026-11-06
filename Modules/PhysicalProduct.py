from Modules.CanBeShipped import CanBeShipped
from Modules.Product import Product

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, itemType, weight):
        super().__init__(product_id, name, price, stock)
        self.itemType = itemType
        self.weight = weight

    def display_information(self):
        super().display_information()
        print(f" | Type: {self.itemType} | Weight: {self.weight} kg")

    def get_fulfillment_info(self):
        return "Product requires physical shipping."

    def calculate_shipping_cost(self):
        cost_per_kg = 2.0
        return self.weight * cost_per_kg