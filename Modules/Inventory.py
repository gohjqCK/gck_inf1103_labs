from Modules.DigitalProduct import DigitalProduct
from Modules.PhysicalProduct import PhysicalProduct
from Modules.Product import Product
from Modules.Supplier import Supplier

class Inventory:
    def __init__(self):
        self.products: dict[str, Product] = {}

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
            supplyID = input("Supplier ID: ")
            supplyName = input("Supplier Name: ")
            supplyEmail = input("Supplier Contact Email: ")
            supplier = Supplier(supplyID, supplyName, supplyEmail)

        except ValueError:
            return "fail"
        fullPrice = f"${itemPrice:.2f}"  
        if itemType == "physical":
            self.products[fullID] = PhysicalProduct(fullID, itemName, fullPrice, itemStock, supplier, itemType, itemWeight)
        elif itemType == "digital":
            self.products[fullID] = DigitalProduct(fullID, itemName, fullPrice, itemStock, supplier, itemType, itemDownloadSize)
        return "success"

    def remove_product(self, productID):
        if productID in self.products:
            del self.products[productID]
            return "success"
        else:
            return "fail"

    def search_product(self, fullID):
        if fullID in self.products:
            print("\nProduct Found:")
            print("==========================")
            print(f"Product ID: {self.products[fullID].product_id} | Name: {self.products[fullID].name} | "
                  f"Price: {self.products[fullID].price} | Stock: {self.products[fullID].stock}")
            print("==========================\n")
            choice = input("Press 1 to view shipping and supplier information, or any other key to continue: ")
            if choice == "1":
                if self.products[fullID].get_fulfillment_info() == "physical":
                    print(f"\nFulfillment Info: {self.products[fullID].get_fulfillment_info()}")
                    print(f"Shipping Cost: ${self.products[fullID].calculate_shipping_cost():.2f}")
                else:
                    print("This product is digital and does not require shipping.")
                print(f"Supplier ID: {self.products[fullID].supplier.supplier_id}")
                print(f"Supplier Name: {self.products[fullID].supplier.name}")
                print(f"Supplier Email: {self.products[fullID].supplier.contact_email}\n")

        elif fullID not in self.products:
            return "exist"
        else:
            return "fail"
        return None

    def display_information(self) -> None:
        for product in self.products.values():
            product.display_information()