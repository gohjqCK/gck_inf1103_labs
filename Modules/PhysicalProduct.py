from Modules.CanBeShipped import CanBeShipped
from Modules.Product import Product

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, itemType, other_info):
        super().__init__(product_id, name, price, stock)
        self.itemType = itemType
        self.other_info = other_info

    def display_information(self):
        super().display_information()
        print(f" | Type: {self.itemType} | Weight: {self.other_info} kg")

    def get_fulfillment_info(self):
        return "physical"

    def calculate_shipping_cost(self):
        cost_per_kg = 2.0
        return self.other_info * cost_per_kg