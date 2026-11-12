import json
from Modules.Product import Product
from Modules.DigitalProduct import DigitalProduct
from Modules.PhysicalProduct import PhysicalProduct
from Modules.Inventory import Inventory
from Modules.Supplier import Supplier
from Modules.Order import Order

print("\n2.2 Associate Supplier with Product")
print("=====================================================")
supplier = Supplier("1", "acer", "a@mail.net")

product = PhysicalProduct("P001", "Laptop", 1234.00, 100, supplier, "physical", 120)

del supplier

print(product.supplier.supplier_id, product.supplier.name, product.supplier.contact_email)
print("=====================================================")

print("\n3.2 Add and remove product")
print("=====================================================")
supplier = Supplier("1", "acer", "a@mail.net")

product = PhysicalProduct("P001", "Laptop", 1234.00, 100, supplier, "physical", 120)

inventoryA = Inventory()
inventoryA.add_product(product)
inventoryA.remove_product(product.product_id)
product.display_information()

inventoryB = Inventory()
inventoryB.add_product(product)
inventoryB.remove_product(product.product_id)
product.display_information
print("=====================================================")

print("\n4.3 Test Composition")
print("=====================================================")
supplier1 = Supplier("1", "acer", "a@mail.net")
product1 = PhysicalProduct("P001", "Laptop", 1234.00, 100, supplier1, "physical", 120)

supplier2 = Supplier("2", "Disney", "d@mail.net")
product2 = DigitalProduct("P002", "Movie1", 3.99, 150, supplier2, "digital", 3500)

order1 = Order(1)
order1.add_order_line(product1, 3)
order1.add_order_line(product2, 50)

order2 = Order(2)
order2.add_order_line(product1, 3)

order1.remove_order_line("P001")
order1.view_order()

order2.view_order()
print("=====================================================")

print("\n6.1 Work with the Product abstraction")
print("=====================================================")
def display_all_products(self) -> None:
    for product in self.products:
        product.display_information()

supplier1 = Supplier("1", "acer", "a@mail.net")
product1 = PhysicalProduct("P001", "Laptop", 1234.00, 100, supplier1, "physical", 120)

supplier2 = Supplier("2", "Disney", "d@mail.net")
product2 = DigitalProduct("P002", "Movie1", 3.99, 150, supplier2, "digital", 3500)

inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)

display_all_products(inventory)
print("=====================================================")

print("\n6.2 Test suitability")
print("=====================================================")
def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfillment_info())

supplier1 = Supplier("1", "acer", "a@mail.net")
product1 = PhysicalProduct("P001", "Laptop", 1234.00, 100, supplier1, "physical", 120)

supplier2 = Supplier("2", "Disney", "d@mail.net")
product2 = DigitalProduct("P002", "Movie1", 3.99, 150, supplier2, "digital", 3500)

show_product_details(product1)
show_product_details(product2)
# # NOTE: IT OUTPUTS ONLY "physical" AND "digital" AS I LATER USE THAT OUTPUT TO PRINT 
# # FURTHER IN DETAIL (NEEDS HANDLING / DELIVERED DIGITALLY)
print("=====================================================")

print("\n7.2 Demonstrate polymorphism")
print("=====================================================")

supplier1 = Supplier("1", "acer", "a@mail.net")
product1 = PhysicalProduct("P001", "Laptop", 1234.00, 100, supplier1, "physical", 120)

supplier2 = Supplier("2", "Disney", "d@mail.net")
product2 = DigitalProduct("P002", "Movie1", 3.99, 150, supplier2, "digital", 3500)

inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)

for product in inventory.products:
    product.display_information()
    print(product.get_fulfillment_info())
# # NOTE: IT OUTPUTS ONLY "physical" AND "digital" AS I LATER USE THAT OUTPUT TO PRINT 
# # FURTHER IN DETAIL (NEEDS HANDLING / DELIVERED DIGITALLY)
print("=====================================================")