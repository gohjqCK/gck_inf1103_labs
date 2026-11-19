import csv
from Modules.Product import Product
from Modules.DigitalProduct import DigitalProduct
from Modules.PhysicalProduct import PhysicalProduct
from Modules.Inventory import Inventory
from Modules.Supplier import Supplier
from Modules.Order import Order
from Modules.PercentageDiscount import PercentageDiscount
from Modules.BulkDiscount import BulkDiscount
from Modules.NoDiscount import NoDiscount
from Modules.ProductFactory import ProductFactory

print("\n2.3 Use a strategy in Order")
print("=====================================================")
supplier1 = Supplier("1", "acer", "a@mail.net")
product1 = PhysicalProduct("P001", "Laptop", 1, 100, supplier1, "physical", 120) # Price set to 1 for easier reading

supplier2 = Supplier("2", "Disney", "d@mail.net")
product2 = DigitalProduct("P002", "Movie1", 1, 150, supplier2, "digital", 3500) # Price set to 1 for easier reading

orders = {}
order = Order(1)
orders[1] = order
order.add_order_line(product1, 150) # 150 items
order.add_order_line(product2, 100) # 250 items total

print("Bulk Discount")
order.set_discount(BulkDiscount(200, 20))
order.calculate_total()
order.view_order()

print("Percentage Discount")
order.set_discount(PercentageDiscount(10))
order.calculate_total()
order.view_order()
print("=====================================================")

print("\n2.4 Extend Without Modifying")
print("=====================================================")
supplier1 = Supplier("1", "acer", "a@mail.net")
product1 = PhysicalProduct("P001", "Laptop", 1, 100, supplier1, "physical", 120) # Price set to 1 for easier reading

orders = {}
order1 = Order(1)
orders[1] = order1
order1.add_order_line(product1, 100)

order2 = Order(2)
orders[2] = order2
order2.add_order_line(product1, 50)

order1.set_discount(PercentageDiscount(10))
order1.calculate_total()
order1.view_order()

order2.set_discount(PercentageDiscount(10))
order2.calculate_total()
order2.view_order()
print("=====================================================")

print("\n3.2 Create a ProductFactory")
print("=====================================================")
supplier2 = Supplier("2", "Disney", "d@mail.net")

factory = ProductFactory.create("service", "P002", "Movie1", 1, 150, supplier2, "digital", 3500)
# product_type is set to "service", ValueError is raised
print("=====================================================")

print("\n4.0 Validation")
print("=====================================================")
supplier2 = Supplier("2", "Disney", "d@mail.net")

store = Inventory()
Inventory.add_product(store, ProductFactory.create("digital", "P002", "Movie1", 1, -1, supplier2, "digital", 3500))
# Stock is set to negative, ValueError is raised
print("=====================================================")

print("\n5.1 User Input")
print("=====================================================")
def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, e.g. 12.50")

get_positive_float("Prompt: ")

print("=====================================================")

print("\n5.2 Loading products from a file")
print("=====================================================")
def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    try:
        file = open(path, newline="")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        with file:
            # read rows with csv.reader and skip the header row
            read = csv.reader(file)
            next(read, None)
            loaded = 0
            # for each row: try to create and add the product,
            for line, row in enumerate(read, start=2):
                try:
                    product_type, product_id, name, price, stock = row
                    product = ProductFactory.create(product_type, product_id, name, float(price), int(stock), supplier, product_type, 1000.00)
                    inventory.add_product(product)
                    loaded += 1
                # except ValueError: report the row and continue
                except ValueError:
                    print(f"Row {line} skipped")
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")

store = Inventory()
supplier2 = Supplier("2", "Disney", "d@mail.net")
load_products("products.csv", store, supplier2)
    
print("=====================================================")