import json

class product:
    def __init__(self, product_id, name, price, stock):
            self.product_id = product_id
            self.name = name
            self.price = price
            self.stock = stock
    
    def update_stock():
        if store == []:
            return "empty"
        else:
            id = input("Enter Product ID: ")
            try:
                selectID = int(id.replace("P", "")) - 1
                try:
                    print("\nProduct Found:\nName: " + store[selectID]["NAME"])
                    print("Current Stock: " + str(store[selectID]["STOCK"]))
                except:
                    return "exist"
                newStock = int(input("\nNew stock quantity: "))         
                try:
                    store[selectID]["STOCK"] = newStock
                except:
                    return "fail"
            except ValueError:
                return "fail"

    def display_information(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Stock: {self.stock} units")

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
        self.products[fullID] = product(fullID, itemName, fullPrice, itemStock)   
        return "success"

    def calculate_tax(self, amount):
        tax_rate = 0.07  # 7% sales tax
        tax_amount = amount * tax_rate
        total_with_tax = amount + tax_amount
        return total_with_tax

    def process_delivery(self, product_id, quantity):
        product = self.search_product(product_id)
        if product:
            product.update_stock(quantity)
            return product.price * quantity
        else:
            print("Product not found.")
            return 0
        
    def search_product(self, product_id):
        return self.products.get(product_id, None)

    def display_all(self):
        for product in self.products.values():
            print(f"ID: {product.product_id} | Name: {product.name} | "
                  f"Price: {product.price} | Stock: {product.stock}")
            
def choiceValidator(choice):
    try:
        choice = int(choice)
        if choice < 1 or choice > 6:
            choice = "fail"
            return choice
        else:
            choice = choice
            return choice

    except ValueError:
        choice = "fail"
        return choice

def load_inventory():
    try:
        open('inventory.json', 'r+')
        print("\ninventory.json found.\nInventory loaded successfully.\n")
        data = json.load(open('inventory.json', 'r+'))
        for item in data:
            store.products[item["ID"]] = product(
                item["ID"],
                item["NAME"],
                float(item["PRICE"].replace("$", "")),
                item["STOCK"],
            )
    except FileNotFoundError:
        print("\nFile does not exist! Generating a new inventory file.\n")
        open('inventory.json', 'w+')
    except json.JSONDecodeError:
        print("\nError decoding JSON. Please check the inventory.json file.\n")

def search_product():
    id = input("Enter Product ID: ")
    try:
        selectID = int(id.replace("P", "")) - 1
        try:
            print("\nProduct Found:")
            print("-----------------------")
            print("ID: " + str(store[selectID]["ID"]))
            print("NAME: " + str(store[selectID]["NAME"]))
            print("PRICE: " + str(store[selectID]["PRICE"]))
            print("STOCK: " + str(store[selectID]["STOCK"]))
            print("-----------------------\n")

        except:
            return "exist"
    except ValueError:
        return "fail"

def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file)
    print("Inventory saved successfully.\n")


def menu():
    print(
    "-----------MENU-----------\n" + 
    "1. Display all products\n" +
    "2. Add product\n" +
    "3. Update Stock\n" +
    "4. Search Product\n" +
    "5. Save inventory\n" +
    "6. Exit\n" +
    "--------------------------\n"
    )

print("==================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("==================================")

store = Inventory()
load_inventory()

while True:
    menu()
    option = choiceValidator(input("Enter Option: "))
    if option == "fail":
        print("WARNING: Please input a valid option")
    if option == 1:
        print("Current Inventory:\n")
        print("----------------------------------------------------")
        Inventory.display_all(store)
        print("----------------------------------------------------\n")
        input("Press any key to continue...")

    if option == 2:
        print("\nAdd New Product")
        newprod = Inventory.add_product(store)
        if newprod == "fail":
            print("One or more options invalid. Please try again.")
        elif newprod == "exist":
            print("Item ID already exists. Please try again.")
        elif newprod == "success":
            print("\nProduct Added Successfully!\n")
            input("Press any key to continue...")

    if option == 3:
        print("\nUpdate Stock")
        upd = product.update_stock()
        if upd == "empty":
            print("\nNo products in stock\n")
        elif upd == "fail":
            print("\nInvalid input. Please try again.\n")
        elif upd == "exist":
            print("\nSpecified ID does not exist. Please try again.\n")
        else:
            print("\nStock Updated Successfully!\n")
            input("Press any key to continue...")

    if option == 4:
        print("\nSearch Product")
        search = Inventory.search_product()
        if search == "fail":
            print("Invalid input. Please try again\n")
        elif search == "exist":
            print("Product not found. Please try again\n")
            input("Press any key to continue...")

    if option == 5:
        Inventory.save_inventory(store)

    if option == 6:
        print("\nSaving inventory before exit...")
        # Inventory.save_inventory(store)
        print("\nInventory saved successfully.\n")
        print("Thank you for using the Inventory Management System\nProgram Terminated.")
        break