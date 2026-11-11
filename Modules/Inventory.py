from Modules.DigitalProduct import DigitalProduct
from Modules.PhysicalProduct import PhysicalProduct

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
            itemType = input("Product Type (Physical/Digital): ").strip().lower()
            if itemType == "physical":
                itemWeight = float(input("Weight in Kgs: "))
            elif itemType == "digital":
                itemDownloadSize = float(input("Download Size in MB: "))
        except ValueError:
            return "fail"
        fullPrice = f"${itemPrice:.2f}"  
        if itemType == "physical":
            self.products[fullID] = PhysicalProduct(fullID, itemName, fullPrice, itemStock, itemType, itemWeight)
        elif itemType == "digital":
            self.products[fullID] = DigitalProduct(fullID, itemName, fullPrice, itemStock, itemType, itemDownloadSize)
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

    def display_information(self):
        for product in self.products.values():
            product.display_information()