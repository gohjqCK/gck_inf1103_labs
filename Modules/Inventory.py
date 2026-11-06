import Modules.Product as Product

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self):
        try:
            itemID = int(input("Product ID: "))
            fullID = f"P{itemID:03d}"
            if fullID in self.products:
                    return "exist"  
            itemName = input("Product Name: ")
            itemPrice = float(input("Price: "))
            itemStock = int(input("Stock Quantity: "))
        except ValueError:
            return "fail"
        fullPrice = f"${itemPrice:.2f}"  
        self.products[fullID] = Product.Product(fullID, itemName, fullPrice, itemStock)   
        return "success"

    def search_product(self, productID):
        if productID in self.products:
            print("\nProduct Found:")
            print("-----------------------")
            print(f"ID: {self.products[productID].product_id} | Name: {self.products[productID].name} | "
                  f"Price: {self.products[productID].price} | Stock: {self.products[productID].stock}")
            print("-----------------------\n")
        elif productID not in self.products:
            return "exist"
        else:
            return "fail"
        return None

    def display_all(self):
        for product in self.products.values():
            print(f"ID: {product.product_id} | Name: {product.name} | "
                  f"Price: {product.price} | Stock: {product.stock}")