from Modules.Product import Product

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, itemType, download_size):
        super().__init__(product_id, name, price, stock)
        self.itemType = itemType
        self.download_size = download_size

    def display_information(self):
        super().display_information()
        print(f" | Type: {self.itemType} | Size: {self.download_size} MB")

    def get_fulfillment_info(self):
        return "Product is delivered digitally."