from Modules.Product import Product

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, itemType, other_info):
        super().__init__(product_id, name, price, stock)
        self.itemType = itemType
        self.other_info = other_info

    def display_information(self):
        super().display_information()
        print(f" | Type: {self.itemType} | Size: {self.other_info} MB")

    def get_fulfillment_info(self):
        return "digital"