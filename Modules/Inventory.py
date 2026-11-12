from Modules.Product import Product

class Inventory:
    def __init__(self):
        self.products: list[Product] = []

    def add_product(self, product: Product):
        self.products[product.product_id] = product

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
        for product in self.products:
            product.display_information()