from Modules.Product import Product

class Inventory:
    def __init__(self):
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, fullID : str) -> Product | None:
        product = self.find_product(fullID)
        if product is None:
            return "fail"
        self.products.remove(product)
        return "success" 

    def find_product(self, fullID : str) -> Product | None:
        for product in self.products:
            if product.product_id == fullID:
                return product
        return None

    def search_product(self, fullID, type):
        product = self.find_product(fullID)
        if product is None:
            return "fail"

        print("\n==========================")
        print("Product Found:")
        print("==========================")
        print(f"Product ID: {product.product_id} | Name: {product.name} | "
                f"Price: {product.price} | Stock: {product.stock}")
        if type == "search":
            if product.get_fulfillment_info() == "physical":
                print("Product requires shipping handler")
                print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")
            else:
                print("This product is delivered digitally.")
            print(f"Supplier ID: {product.supplier.supplier_id}")
            print(f"Supplier Name: {product.supplier.name}")
            print(f"Supplier Email: {product.supplier.contact_email}")
            print("==========================\n")
        return "success" 

    def display_information(self) -> None:
        for product in self.products:
            product.display_information()