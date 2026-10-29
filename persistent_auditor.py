class product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity

    def display_information(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock: {self.stock} units")

class inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def search_product(self, product_id):
        return self.products.get(product_id, None)

    def display_all(self):
        for product in self.products.values():
            product.display_information()
            print("-" * 20)


def get_valid_input(inventoryI):
    try:
        if inventoryI.isdigit() and int(inventoryI) > 0:
            inventoryI = inventoryI
        elif inventoryI.lower() == "quit":
            inventoryI = "quit"
        elif inventoryI.lower() == "report":
            inventoryI = "report"
        elif inventoryI.lower() == "load":
            inventoryI = "load"
        elif inventoryI.lower() == "save":
            inventoryI = "save"
        else:
            inventoryI = "fail"
    except ValueError:
        inventoryI = "fail"
    return inventoryI

def process_delivery(current_total, new_value):
    new_value += current_total
    return new_value

def calculate_tax(amount):
    price = 0.50
    full_cost = amount * price
    tax = full_cost * 1.1
    return tax

def generate_reports(total_units, failed_attempts):
    chit = print(str(total_units) + " amount of units total, " + str(failed_attempts) + " times failed during this request")
    return chit

def load_inventory():
    file.seek(0)
    status = file.readlines()
    print(status)

def save_inventory(newlist):
    file.writelines(newlist)
    file.seek(0)
    print("Orders saved.")
    print(file.readlines())

inventory = 0
total = 0
fail = 0
counter = 0
totalOrder = []
file = open("inventory.json", 'r+')
orderlist = list(file.readlines())
for order in orderlist:
        counter += 1

while True:
    inventoryI = input("Enter Product Name: ")

    if get_valid_input(inventoryI).lower() == "quit":
        print("Quitting..")
        break
    elif get_valid_input(inventoryI) == "load":
        print("All orders:")
        load_inventory()

    elif get_valid_input(inventoryI) == "save":
        save_inventory(totalOrder)

    else:
        quantity = input("Enter Quantity: ")
        if get_valid_input(quantity).isdigit():
            inventory = int(get_valid_input(quantity))
            total = int(process_delivery(inventory, total))
            price = calculate_tax(total)
            #print(str(total) + " amount of units, total price is: $" + str(price))
            print("New order added:")
            newOrder = [str(counter + 1001), " " + inventoryI, " " +str(inventory) + "\n"]
            totalOrder += newOrder
            print(','.join(map(str,totalOrder)))
            counter += 1

        elif get_valid_input(inventoryI) == "fail":
            fail += 1
            print("Please input a valid number!")

        elif get_valid_input(inventoryI) == "report":
            generate_reports(total, fail)
            break