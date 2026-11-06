class Product:
    def __init__(self, product_id, name, price, stock):
            self.product_id = product_id
            self.name = name
            self.price = price
            self.stock = stock
    
    def update_stock(self, itemStock):
        self.stock = itemStock

    def display_information(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Stock: {self.stock} units")